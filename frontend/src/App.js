import React, { useState } from "react";
import QueryForm from "./components/QueryForm";
import ResponseBox from "./components/ResponseBox";
import SourcesBox from "./components/SourcesBox";
import { sendQuery } from "./api";

function App() {
  const [response, setResponse] = useState("");
  const [sources, setSources] = useState([]);

  const handleQuery = async (data) => {
    try {
      const res = await sendQuery(data);
      setResponse(res.data.response);
      setSources(res.data.sources);
    } catch (err) {
      console.error(err);
      alert("Error connecting to backend");
    }
  };

  return (
    <div style={{ maxWidth: "800px", margin: "auto" }}>
      <h1>AI Customer Support Assistant</h1>

      <QueryForm onSubmit={handleQuery} />
      <ResponseBox response={response} />
      <SourcesBox sources={sources} />
    </div>
  );
  
}

export default App;
console.log(QueryForm, ResponseBox, SourcesBox);