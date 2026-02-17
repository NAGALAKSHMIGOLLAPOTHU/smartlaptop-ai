from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_reviews(reviews):

    if not isinstance(reviews, list) or len(reviews) == 0:
        return {
            "average_score": 0,
            "positive": 0,
            "negative": 0,
            "neutral": 0
        }

    scores = []
    positive = negative = neutral = 0

    for review in reviews:
        if not isinstance(review, str):
            continue

        score = analyzer.polarity_scores(review)["compound"]
        scores.append(score)

        if score >= 0.05:
            positive += 1
        elif score <= -0.05:
            negative += 1
        else:
            neutral += 1

    if not scores:
        avg_score = 0
    else:
        avg_score = sum(scores) / len(scores)

    return {
        "average_score": round(avg_score, 2),
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    }
