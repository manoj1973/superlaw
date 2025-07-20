# ai_engine.py

import os
import requests
import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlaw_django_project.settings")

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

TOGATHER_MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"
OPENAI_MODEL = "gpt-3.5-turbo"

'''def call_openai(prompt):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are a legal assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content'''
def call_openai(prompt):
    #openai.api_key = OPENAI_API_KEY
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are a legal assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

def call_together_ai(prompt):
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": TOGATHER_MODEL,
        "messages": [
            {"role": "system", "content": "You are a legal assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "top_p": 0.9,
        "max_tokens": 1024,
    }

    response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"[Error from Together API] Status {response.status_code}: {response.text}"

def generate_legal_document(prompt, use_openai=False):
    return call_openai(prompt) if use_openai else call_together_ai(prompt)
