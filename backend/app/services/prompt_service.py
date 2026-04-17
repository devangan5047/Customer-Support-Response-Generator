def build_prompt(mode, query, docs):

    context = "\n\n".join([d["content"] for d in docs])

    if mode == "strict":
        return f"""
You are a professional customer support assistant.
Use ONLY the provided policy context.
Do not add extra assumptions.

Context:
{context}

Customer Issue:
{query}

Give a clear and concise response.
""", 0.2, 150

    elif mode == "friendly":
        return f"""
You are a polite and empathetic support agent.
Use the policy context but respond in a friendly tone.

Context:
{context}

Customer Issue:
{query}
""", 0.7, 200

    else:
        return None, None, None