from datetime import datetime


class Order:
    def __init__(self, order_id, customer_name, items, total_price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_price = total_price
        self.order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display_order(self):
        print("=" * 40)
        print("Order ID:", self.order_id)
        print("Customer:", self.customer_name)
        print("Date:", self.order_date)

        print("\nItems:")

        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]

            print(product.name, "-", quantity)

        print("\nTotal Price:", self.total_price, "KZT")
        print("=" * 40)


def checkout(customer, orders):
    if len(customer.cart) == 0:
        print("Cart is empty.")
        return

    total_price = 0

    for item in customer.cart:
        product = item["product"]
        quantity = item["quantity"]

        if quantity > product.stock:
            print(product.name, "does not have enough stock.")
            return

        total_price += product.price * quantity

    for item in customer.cart:
        product = item["product"]
        quantity = item["quantity"]

        product.reduce_stock(quantity)

    order = Order(
        len(orders) + 1,
        customer.name,
        customer.cart,
        total_price
    )

    orders.append(order)

    customer.order_history.append(order)

    customer.clear_cart()

    print("Checkout completed successfully.")

    order.display_order()