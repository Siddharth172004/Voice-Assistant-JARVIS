import requests
import json

API_KEY = "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"

def get_ai_response(prompt):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "HTTP-Referer": "http://localhost",
            "X-Title": "Jarvis Assistant"
        },
        json={
            "model": "deepseek/deepseek-r1:free", 
            "messages": [
                {"role": "user", "content": prompt}
            ]
        },
        timeout=10
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}. {response.text}"
