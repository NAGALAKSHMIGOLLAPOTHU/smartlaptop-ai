def calculate_score(sentiment, performance, price_score, brand_score):
    try:
        sentiment = float(sentiment)
        performance = float(performance)
        price_score = float(price_score)
        brand_score = float(brand_score)
    except:
        return 5

    # Normalize sentiment (-1 to 1 → 0 to 10)
    sentiment = (sentiment + 1) * 5
    brand_score = (brand_score + 1) * 5

    final_score = (
        0.35 * sentiment +
        0.30 * performance +
        0.20 * price_score +
        0.15 * brand_score
    )

    return round(max(0, min(10, final_score)), 2)
