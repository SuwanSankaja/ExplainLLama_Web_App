import torch
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load CodeT5 Model
model_name = "Salesforce/codet5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

@api_view(['POST'])
def fix_code(request):
    """
    API Endpoint to fix buggy Java code
    """
    data = request.data
    buggy_code = data.get("buggy_code", "")

    if not buggy_code:
        return Response({"error": "No code provided"}, status=400)

    # Prepare input for CodeT5
    input_text = f"Fix this Java code: {buggy_code}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate fixed code
    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_length=512,
            num_return_sequences=1,
            do_sample=False
        )

    fixed_code = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()

    return Response({"fixed_code": fixed_code})
