import React, { useState } from "react";
import axios from "axios";

function App() {
  const [buggyCode, setBuggyCode] = useState("");
  const [fixedCode, setFixedCode] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fixCode = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/fix_code/", {
        buggy_code: buggyCode,
      });
      setFixedCode(response.data.fixed_code);
    } catch (err) {
      setError("Error fixing code. Please try again.");
    }
    setLoading(false);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>ExplainLlama Bug Fixer</h1>
      <textarea
        rows="8"
        cols="50"
        placeholder="Enter buggy Java code here..."
        value={buggyCode}
        onChange={(e) => setBuggyCode(e.target.value)}
        style={{ fontSize: "16px", padding: "10px" }}
      />
      <br />
      <button
        onClick={fixCode}
        disabled={loading}
        style={{ marginTop: "10px", padding: "10px 20px", fontSize: "18px" }}
      >
        {loading ? "Fixing..." : "Fix This"}
      </button>
      <br />
      {error && <p style={{ color: "red" }}>{error}</p>}
      <h2>Fixed Code:</h2>
      <pre style={{ backgroundColor: "#f4f4f4", padding: "10px", fontSize: "16px" }}>
        {fixedCode || "Fixed code will appear here..."}
      </pre>
    </div>
  );
}

export default App;
