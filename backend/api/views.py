import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import anthropic
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Load CodeT5 model
CODET5_MODEL_NAME = "Salesforce/codet5-base"
codeT5_tokenizer = AutoTokenizer.from_pretrained(CODET5_MODEL_NAME)
codeT5_model = AutoModelForSeq2SeqLM.from_pretrained(CODET5_MODEL_NAME)


anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

genai.configure(api_key=GEMINI_API_KEY)


def fix_java_code_codet5(buggy_code):
    """Fix Java code using CodeT5 model."""
    input_text = f"Fix this Java code:\n{buggy_code}"
    input_ids = codeT5_tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    with torch.no_grad():
        output_ids = codeT5_model.generate(input_ids, max_length=512, num_return_sequences=1, do_sample=False)

    fixed_code = codeT5_tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()

    # Generate explanation
    explanation_prompt = (
        f"Explain the fix in simple terms:\nBuggy Code:\n{buggy_code}\nFixed Code:\n{fixed_code}\nExplanation:"
    )
    explanation_ids = codeT5_tokenizer.encode(explanation_prompt, return_tensors="pt", max_length=512, truncation=True)

    with torch.no_grad():
        explanation_output_ids = codeT5_model.generate(explanation_ids, max_length=512, num_return_sequences=1, do_sample=False)

    explanation = codeT5_tokenizer.decode(explanation_output_ids[0], skip_special_tokens=True).strip()

    return fixed_code, explanation


def fix_java_code_claude(buggy_code):
    """Fix Java code using Anthropic Claude model."""
    fix_prompt = f"You are an expert Java developer. Fix the following buggy Java code:\n{buggy_code}\nProvide only the corrected Java code."

    response_fix = anthropic_client.messages.create(
        model="claude-3-5-haiku-latest",
        max_tokens=1024,
        messages=[{"role": "user", "content": fix_prompt}]
    )
    fixed_code = response_fix.content[0].text.strip()

    # Generate explanation
    explanation_prompt = f"You are an expert Java developer. Explain the fix in simple terms within 100 words.\nBuggy Code:\n{buggy_code}\nFixed Code:\n{fixed_code}\nExplanation:"
    
    response_explanation = anthropic_client.messages.create(
        model="claude-3-5-haiku-latest",
        max_tokens=150,
        messages=[{"role": "user", "content": explanation_prompt}]
    )
    
    explanation = response_explanation.content[0].text.strip()

    return fixed_code, explanation


def fix_java_code_gemini(buggy_code):
    """Fix Java code using Google Gemini model."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    fix_prompt = f"You are an expert Java developer. Fix the following buggy Java code:\n{buggy_code}\nProvide only the corrected Java code."
    response_fix = model.generate_content(fix_prompt)
    fixed_code = response_fix.text.strip()

    explanation_prompt = f"You are an expert Java developer. Explain the fix in simple terms within 100 words.\nBuggy Code:\n{buggy_code}\nFixed Code:\n{fixed_code}\nExplanation:"
    response_explanation = model.generate_content(explanation_prompt)

    explanation = response_explanation.text.strip()

    return fixed_code, explanation


@csrf_exempt
def fix_code(request):
    """API to fix Java code based on the selected model."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            buggy_code = data.get("buggy_code", "")
            model_choice = data.get("model", "codet5")  # Default to CodeT5

            if not buggy_code:
                return JsonResponse({"error": "Buggy code is required"}, status=400)

            # Select model based on dropdown input
            if model_choice == "codet5":
                fixed_code, explanation = fix_java_code_codet5(buggy_code)
            elif model_choice == "claude":
                fixed_code, explanation = fix_java_code_claude(buggy_code)
            elif model_choice == "gemini":
                fixed_code, explanation = fix_java_code_gemini(buggy_code)
            else:
                return JsonResponse({"error": "Invalid model choice"}, status=400)

            return JsonResponse({"fixed_code": fixed_code, "explanation": explanation})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)
