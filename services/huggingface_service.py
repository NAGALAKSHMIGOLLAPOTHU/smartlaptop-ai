import requests
import os
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def analyze_sentiment(text):
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": text},
            timeout=10
        )
        result = response.json()

        if isinstance(result, list):
            label = result[0][0]["label"]
            score = result[0][0]["score"]
            return score if label == "POSITIVE" else -score

        return 0
    except Exception as e:
        print("HF Error:", e)
        return 0
