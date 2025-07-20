# superlaw_ai/ai_providers.py
import requests

USE_OPENAI = False  # Change to True if needed

TOGETHER_API_KEY = "your_together_api_key"
TOGETHER_MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"
TOGETHER_URL = "https://api.together.xyz/v1/chat/completions"

def ask_ai(prompt):
    if USE_OPENAI:
        return "[OpenAI not implemented]"
    else:
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": TOGETHER_MODEL,
            "messages": [
                {"role": "system", "content": "You are a legal expert."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1500
        }
        response = requests.post(TOGETHER_URL, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        return f"❌ Error {response.status_code}: {response.text}"
