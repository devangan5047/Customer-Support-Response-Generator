import requests
from app.config import SARVAM_API_KEY, SARVAM_API_URL

def call_llm(prompt, temperature, max_tokens):

    headers = {
        "Authorization": f"Bearer {SARVAM_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sarvam-m",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    response = requests.post(SARVAM_API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"LLM Error: {response.text}")

    data = response.json()

    reply = data["choices"][0]["message"]["content"]

    # 👇 NEW: token usage
    usage = data.get("usage", {})

    return reply, usage