import React from "react";

const SourcesBox = ({ sources }) => {
  if (!sources || sources.length === 0) return null;

  return (
    <div>
      <h3>Retrieved Policies</h3>
      {sources.map((src, index) => (
        <div key={index} style={{ marginBottom: "10px" }}>
          <strong>{src.title}</strong>
          <p>{src.content}</p>
          <small>Score: {src.score}</small>
        </div>
      ))}
    </div>
  );
};

export default SourcesBox;