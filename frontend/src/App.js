import React, { useState } from "react";
import "./App.css"; // Import CSS file

const App = () => {
    const [buggyCode, setBuggyCode] = useState("");
    const [fixedCode, setFixedCode] = useState("");
    const [explanation, setExplanation] = useState("");
    const [selectedModel, setSelectedModel] = useState("codet5");
    const [loading, setLoading] = useState(false);

    const handleFixCode = async () => {
        setLoading(true);
        setFixedCode("");
        setExplanation("");

        try {
            const response = await fetch("http://localhost:8000/api/fix_code/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    buggy_code: buggyCode,
                    model: selectedModel,
                }),
            });

            const data = await response.json();
            setFixedCode(data.fixed_code);
            setExplanation(data.explanation);
        } catch (error) {
            console.error("Error fixing code:", error);
        }
        setLoading(false);
    };

    return (
        <div className="container">
            <h1>ExplainLLama</h1>

            <textarea
                placeholder="Enter buggy Java code here..."
                value={buggyCode}
                onChange={(e) => setBuggyCode(e.target.value)}
            />

            <div className="select-container">
                <select value={selectedModel} onChange={(e) => setSelectedModel(e.target.value)}>
                    <option value="codet5">CodeT5</option>
                    <option value="claude">Claude</option>
                    <option value="gemini">Gemini</option>
                </select>

                <button onClick={handleFixCode} disabled={loading}>
                    {loading ? "Fixing..." : "Fix & Explain"}
                </button>
            </div>

            <div className="output-container">
                <h2>Fixed Code</h2>
                <pre className="output-box fixed-code">{fixedCode || "No fixed code yet."}</pre>

                <h2>Explanation</h2>
                <pre className="output-box explanation">{explanation || "No explanation yet."}</pre>
            </div>
        </div>
    );
};

export default App;
