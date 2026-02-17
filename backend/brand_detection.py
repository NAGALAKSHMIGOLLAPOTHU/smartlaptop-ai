def detect_brand(product_name):
    brands = ["Dell", "HP", "Apple", "Lenovo", "Asus", "Acer", "MSI"]

    if not product_name:
        return "Unknown"

    product_lower = product_name.lower()

    for brand in brands:
        if brand.lower() in product_lower:
            return brand

    return "Unknown"
