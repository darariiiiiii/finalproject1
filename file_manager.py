import json


def save_products(products, filename):
    product_data = []

    for product in products:
        product_info = {
            "id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "category": product.category,
            "rating": product.rating
        }

        product_data.append(product_info)

    with open(filename, "w") as file:
        json.dump(product_data, file, indent=4)

    print("Products saved successfully.")


def load_products(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("File not found.")
        return []


def save_orders(orders, filename):
    order_data = []

    for order in orders:
        order_info = {
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "total_price": order.total_price,
            "date": order.order_date
        }

        order_data.append(order_info)

    with open(filename, "w") as file:
        json.dump(order_data, file, indent=4)

    print("Orders saved successfully.")


def load_orders(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("File not found.")
        return []