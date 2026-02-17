from backend.scoring import calculate_score


def generate_performance_score(use_case):
    mapping = {
        "Student": 7.5,
        "Business": 8,
        "Programming": 9,
        "Gaming": 9.5,
        "Video Editing": 9.5
    }
    return mapping.get(use_case, 7)


def generate_price_score(price, budget):
    try:
        price = float(price)
        budget = float(budget)
    except:
        return 6

    if price <= budget:
        return 10
    elif price <= budget * 1.15:
        return 8
    else:
        return 6


def recommend_laptops(laptops, use_case, budget, brand_score):

    recommendations = []

    for laptop in laptops:

        performance = generate_performance_score(use_case)
        price_score = generate_price_score(laptop["price"], budget)

        final_score = calculate_score(
            laptop["sentiment"],
            performance,
            price_score,
            brand_score
        )

        laptop["performance_score"] = performance
        laptop["price_score"] = price_score
        laptop["brand_score"] = round((brand_score + 1) * 5, 2)
        laptop["final_score"] = final_score
        laptop["use_case"] = use_case
        laptop["explanation"] = (
            f"{laptop['name']} is recommended for {use_case} "
            f"due to strong sentiment and good value within your budget."
        )

        recommendations.append(laptop)

    recommendations.sort(key=lambda x: x["final_score"], reverse=True)

    return recommendations
