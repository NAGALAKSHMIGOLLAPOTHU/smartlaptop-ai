from flask import Flask, request, jsonify
from backend.brand_detection import detect_brand
from backend.sentiment import analyze_reviews
from backend.recommendation import recommend_laptops
from services.review_service import fetch_reviews
from services.news_service import fetch_brand_news
from services.huggingface_service import analyze_sentiment
import traceback

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"status": "SmartLaptop AI Backend Running 🚀"})


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        product = data.get("product")
        use_case = data.get("use_case", "Student")
        budget = data.get("budget", 50000)

        if not product:
            return jsonify({"error": "Product name required"}), 400

        # 1️⃣ Detect Brand
        brand = detect_brand(product) or "Unknown"

        # 2️⃣ Fetch Reviews Safely
        try:
            reviews, price = fetch_reviews(product)
        except:
            reviews = []
            price = budget

        reviews = reviews or []
        price = price or budget

        # 3️⃣ Sentiment Analysis
        try:
            sentiment_data = analyze_reviews(reviews)
        except:
            sentiment_data = {
                "average_score": 0,
                "positive": 0,
                "negative": 0,
                "neutral": 0
            }

        # 4️⃣ Brand News Sentiment
        try:
            headlines = fetch_brand_news(brand)
            headlines = headlines or []
            brand_scores = [analyze_sentiment(h) for h in headlines if h]
            brand_score = sum(brand_scores)/len(brand_scores) if brand_scores else 0
        except:
            brand_score = 0

        # 5️⃣ Recommendation Engine
        laptop_data = [{
            "name": product,
            "price": price,
            "sentiment": sentiment_data["average_score"]
        }]

        try:
            recommendation = recommend_laptops(
                laptop_data,
                use_case,
                budget,
                brand_score
            )
            recommendation = recommendation[0] if recommendation else {}
        except:
            recommendation = {
                "decision": "Insufficient Data",
                "score": 0
            }

        # FINAL RESPONSE (Always JSON)
        return jsonify({
            "brand": brand,
            "price": price,
            "sentiment_summary": sentiment_data,
            "brand_score": round(brand_score, 2),
            "recommendation": recommendation
        })

    except Exception as e:
        print("❌ Backend Error:")
        traceback.print_exc()
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    print("🚀 Starting SmartLaptop AI Backend...")
    app.run(port=5000, debug=True)
