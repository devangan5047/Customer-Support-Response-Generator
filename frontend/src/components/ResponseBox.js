const ResponseBox = ({ response, usage }) => {
  if (!response) return null;

  return (
    <div>
      <h3>AI Response</h3>
      <p>{response}</p>

      {usage && (
        <div>
          <h4>Token Usage</h4>
          <p>Prompt Tokens: {usage.prompt_tokens}</p>
          <p>Completion Tokens: {usage.completion_tokens}</p>
          <p>Total Tokens: {usage.total_tokens}</p>
        </div>
      )}
    </div>
  );
};

export default ResponseBox