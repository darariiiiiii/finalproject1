import json

from products import (
    Electronics,
    Clothing,
    Food
)

# ================= SAVE =================

def save_products(products, filename):

    product_data = []

    for product in products:

        item = {
            "id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "category": product.category,
            "rating": product.rating
        }

        # Electronics
        if isinstance(product, Electronics):
            item["warranty"] = product.warranty_months

        # Clothing
        elif isinstance(product, Clothing):
            item["size"] = product.size

        # Food
        elif isinstance(product, Food):
            item["expiry_date"] = product.expiry_date

        product_data.append(item)

    with open(filename, "w") as file:
        json.dump(product_data, file, indent=4)

# ================= LOAD =================

def load_products(filename):

    products = []

    try:

        with open(filename, "r") as file:

            data = json.load(file)

            for item in data:

                category = item["category"]

                # Electronics
                if category == "Electronics":

                    product = Electronics(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["rating"],
                        item["warranty"]
                    )

                # Clothing
                elif category == "Clothing":

                    product = Clothing(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["rating"],
                        item["size"]
                    )

                # Food
                elif category == "Food":

                    product = Food(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["rating"],
                        item["expiry_date"]
                    )

                else:
                    continue

                products.append(product)

    except FileNotFoundError:

        print("File not found.")

    return products