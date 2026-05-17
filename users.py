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
        item = {
            "product": product,
            "quantity": quantity
        }

        self.cart.append(item)

        print(product.name, "added to cart.")

    def view_cart(self):
        if len(self.cart) == 0:
            print("Cart is empty.")

        else:
            total = 0

            for item in self.cart:
                product = item["product"]
                quantity = item["quantity"]

                print("-" * 30)
                print("Product:", product.name)
                print("Quantity:", quantity)
                print("Price:", product.price)

                total += product.price * quantity

            print("Total:", total, "KZT")

    def clear_cart(self):
        self.cart.clear()
        print("Cart cleared.")


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
                return

        print("Product not found.")