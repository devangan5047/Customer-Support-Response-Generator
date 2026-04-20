import React, { useState } from "react";

const QueryForm = ({ onSubmit }) => {
  const [query, setQuery] = useState("");
  const [prompt, setPrompt] = useState("");
  const [temperature, setTemperature] = useState(0.5);
  const [maxTokens, setMaxTokens] = useState(150);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      query,
      prompt,
      temperature,
      max_tokens: maxTokens
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      
      <h3>Customer Query</h3>
      <textarea
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        rows={3}
        style={{ width: "100%" }}
      />

      <h3>Custom Prompt</h3>
      <textarea
        placeholder="Write your prompt here..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        rows={5}
        style={{ width: "100%" }}
      />

      <br /><br />

      <label>Temperature: {temperature}</label>
      <input
        type="range"
        min="0"
        max="1"
        step="0.1"
        value={temperature}
        onChange={(e) => setTemperature(parseFloat(e.target.value))}
      />

      <br /><br />

      <label>Max Tokens:</label>
      <input
        type="number"
        value={maxTokens}
        onChange={(e) => setMaxTokens(parseInt(e.target.value))}
      />

      <br /><br />

      <button type="submit">Generate Response</button>
    </form>
  );
};

export default QueryForm;