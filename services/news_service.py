import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWSAPI_KEY")

def fetch_brand_news(brand):
    url = "https://newsapi.org/v2/everything"
    params = {"q": brand, "language": "en", "sortBy": "publishedAt", "pageSize": 5, "apiKey": NEWS_API_KEY}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        return [a["title"] for a in articles if a.get("title")]
    except:
        return []
