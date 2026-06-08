import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

try:
    client = genai.Client()
    print("Available models:")
    for m in client.models.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print("Error listing models:", e)
