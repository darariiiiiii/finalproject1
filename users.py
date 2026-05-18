class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def display_info(self):
        print("User ID:", self.user_id)
        print("Name:", self.name)
        print("Email:", self.email)


class Customer(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

        self.cart = []
        self.order_history = []

    def add_to_cart(self, product, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if quantity > product.stock:
            print("Not enough stock available.")
            return

        item = {
            "product": product,
            "quantity": quantity
        }

        self.cart.append(item)

        print(product.name, "added to cart.")

    def view_cart(self):
        if len(self.cart) == 0:
            print("Cart is empty.")
            return

        total = 0

        print("=" * 40)
        print("SHOPPING CART")
        print("=" * 40)

        for item in self.cart:
            product = item["product"]
            quantity = item["quantity"]

            subtotal = product.price * quantity

            print("Product:", product.name)
            print("Quantity:", quantity)
            print("Price:", product.price)
            print("Subtotal:", subtotal)
            print("-" * 30)

            total += subtotal

        print("Total:", total, "KZT")

    def calculate_cart_total(self):
        total = 0

        for item in self.cart:
            product = item["product"]
            quantity = item["quantity"]

            total += product.price * quantity

        return total

    def clear_cart(self):
        self.cart.clear()

        print("Cart cleared.")

    def view_order_history(self):
        if len(self.order_history) == 0:
            print("No orders found.")
            return

        print("=" * 40)
        print("ORDER HISTORY")
        print("=" * 40)

        for order in self.order_history:
            order.display_order()


class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    def add_product(self, products, product):
        products.append(product)

        print("Product added successfully.")

    def remove_product(self, products, product_id):
        for product in products:
            if product.product_id == product_id:
                products.remove(product)

                print("Product removed successfully.")
                return True

        print("Product not found.")
        return False

    def view_all_products(self, products):
        print("=" * 40)
        print("ALL PRODUCTS")
        print("=" * 40)

        for product in products:
            product.display_info()
            print("-" * 30)

    def view_all_customers(self, customers):
        if len(customers) == 0:
            print("No customers found.")
            return

        print("=" * 40)
        print("CUSTOMERS")
        print("=" * 40)

        for customer in customers:
            customer.display_info()
            print("-" * 30)