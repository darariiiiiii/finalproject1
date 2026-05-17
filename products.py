class Product:
    def __init__(self, product_id, name, price, stock, category, rating):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.rating = rating

    def display_info(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price, "KZT")
        print("Stock:", self.stock)
        print("Category:", self.category)
        print("Rating:", self.rating)
        print("Shipping Cost:", self.calculate_shipping(), "KZT")

    def is_available(self):
        return self.stock > 0

    def reduce_stock(self, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
        elif quantity > self.stock:
            print("Not enough stock available.")
        else:
            self.stock -= quantity
            print("Stock updated successfully.")

    def calculate_shipping(self):
        return 1500


class Electronics(Product):
    def __init__(self, product_id, name, price, stock, rating, warranty_months):
        super().__init__(product_id, name, price, stock, "Electronics", rating)
        self.warranty_months = warranty_months

    def display_info(self):
        super().display_info()
        print("Warranty:", self.warranty_months, "months")

    def calculate_shipping(self):
        return 2000


class Clothing(Product):
    def __init__(self, product_id, name, price, stock, rating, size):
        super().__init__(product_id, name, price, stock, "Clothing", rating)
        self.size = size

    def display_info(self):
        super().display_info()
        print("Size:", self.size)

    def calculate_shipping(self):
        return 1000


class Food(Product):
    def __init__(self, product_id, name, price, stock, rating, expiry_date):
        super().__init__(product_id, name, price, stock, "Food", rating)
        self.expiry_date = expiry_date

    def display_info(self):
        super().display_info()
        print("Expiry Date:", self.expiry_date)

    def calculate_shipping(self):
        return 500


def show_all_products(products):
    if len(products) == 0:
        print("No products found.")
    else:
        for product in products:
            print("-" * 30)
            product.display_info()


def search_product(products, keyword):
    found_products = []

    for product in products:
        if keyword.lower() in product.name.lower():
            found_products.append(product)

    return found_products


def filter_by_category(products, category):
    filtered_products = []

    for product in products:
        if product.category.lower() == category.lower():
            filtered_products.append(product)

    return filtered_products


def filter_available_products(products):
    available_products = list(filter(lambda product: product.stock > 0, products))
    return available_products


def sort_by_price(products):
    sorted_products = sorted(products, key=lambda product: product.price)
    return sorted_products


def sort_by_rating(products):
    sorted_products = sorted(products, key=lambda product: product.rating, reverse=True)
    return sorted_products


def recommend_products(products, category):
    same_category = []

    for product in products:
        if product.category.lower() == category.lower() and product.stock > 0:
            same_category.append(product)

    recommended = sorted(same_category, key=lambda product: product.rating, reverse=True)

    return recommended[:3]


def find_product_by_id(products, product_id):
    for product in products:
        if product.product_id == product_id:
            return product

    return None