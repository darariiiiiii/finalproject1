from datetime import datetime


class Order:
    def __init__(self, order_id, customer_name, items, total_price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_price = total_price

        self.status = "Completed"

        self.order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display_order(self):
        print("=" * 40)

        print("Order ID:", self.order_id)
        print("Customer:", self.customer_name)
        print("Date:", self.order_date)
        print("Status:", self.status)

        print("\nItems:")

        for item in self.items:
            print(
                item["product_name"],
                "- Quantity:",
                item["quantity"],
                "- Price:",
                item["price"]
            )

        print("\nTotal Price:", self.total_price, "KZT")

        print("=" * 40)

    def cancel_order(self):
        self.status = "Cancelled"

        print("Order cancelled.")

    def complete_order(self):
        self.status = "Completed"

        print("Order completed.")

def checkout(customer, orders):
    if len(customer.cart) == 0:
        print("Cart is empty.")
        return None

    total_price = 0

    for item in customer.cart:
        product = item["product"]
        quantity = item["quantity"]

        if quantity > product.stock:
            print(product.name, "does not have enough stock.")
            return None

        total_price += product.price * quantity

    order_items = []

    for item in customer.cart:
        product = item["product"]
        quantity = item["quantity"]

        product.reduce_stock(quantity)

        order_items.append({
            "product_id": product.product_id,
            "product_name": product.name,
            "quantity": quantity,
            "price": product.price
        })

    order = Order(
        len(orders) + 1,
        customer.name,
        order_items,
        total_price
    )

    orders.append(order)

    customer.order_history.append(order)

    customer.clear_cart()

    print("Checkout completed successfully.")

    order.display_order()

    return order