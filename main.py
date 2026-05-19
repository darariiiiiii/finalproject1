from file_manager import save_products

from products import (
    Electronics,
    Clothing,
    Food,
    show_all_products,
    search_product,
    filter_by_category,
    filter_available_products,
    sort_by_price,
    sort_by_rating,
    recommend_products,
    find_product_by_id
)

from discounts import apply_promo_code

from users import Customer, Admin

from orders import checkout


from file_manager import load_products

products = load_products("products.json")


customer = Customer(
    1,
    "Moldir",
    "moldir@example.com",
    "1234"
)

admin = Admin(
    1,
    "Admin",
    "admin@example.com",
    "admin123"
)

orders = []


while True:

    print("\n===== ONLINE STORE =====")
    print("1. Admin")
    print("2. Customer")
    print("0. Exit")

    main_choice = input("Choose role: ")

    # ================= ADMIN =================

    if main_choice == "1":

        while True:

            print("\n===== ADMIN MENU =====")

            print("1. Show all products")
            print("2. Add product")
            print("3. Remove product")
            print("4. Reduce stock")
            print("5. Show available products")
            print("0. Back")

            admin_choice = input("Enter choice: ")

            try:

                if admin_choice == "1":

                    show_all_products(products)

                elif admin_choice == "2":

                    print("\nChoose category:")
                    print("1. Electronics")
                    print("2. Clothing")
                    print("3. Food")

                    category_choice = input("Enter category: ")

                    product_id = len(products) + 1

                    name = input("Enter product name: ")

                    price = float(input("Enter price: "))

                    stock = int(input("Enter stock quantity: "))

                    rating = float(input("Enter rating: "))

                    if category_choice == "1":

                        warranty = int(
                            input("Enter warranty months: ")
                        )

                        new_product = Electronics(
                            product_id,
                            name,
                            price,
                            stock,
                            rating,
                            warranty
                        )

                    elif category_choice == "2":

                        size = input("Enter size: ")

                        new_product = Clothing(
                            product_id,
                            name,
                            price,
                            stock,
                            rating,
                            size
                        )

                    elif category_choice == "3":

                        expiry_date = input(
                            "Enter expiry date: "
                        )

                        new_product = Food(
                            product_id,
                            name,
                            price,
                            stock,
                            rating,
                            expiry_date
                        )

                    else:
                        print("Invalid category.")
                        continue

                    admin.add_product(products, new_product)

                    save_products(products, "products.json")

                elif admin_choice == "3":

                    product_id = int(
                        input("Enter product ID: ")
                    )

                    admin.remove_product(
                        products,
                        product_id
                    )

                    save_products(products, "products.json")

                elif admin_choice == "4":

                    product_id = int(
                        input("Enter product ID: ")
                    )

                    quantity = int(
                        input("Enter quantity: ")
                    )

                    product = find_product_by_id(
                        products,
                        product_id
                    )

                    if product is not None:

                        product.reduce_stock(quantity)

                        save_products(
                            products,
                            "products.json"
                        )

                    else:
                        print("Product not found.")

                elif admin_choice == "5":

                    result = filter_available_products(
                        products
                    )

                    show_all_products(result)

                elif admin_choice == "0":
                    break

                else:
                    print("Invalid choice.")

            except ValueError:
                print("Invalid input.")

    # ================= CUSTOMER =================

    elif main_choice == "2":

        while True:

            print("\n===== CUSTOMER MENU =====")

            print("1. Show all products")
            print("2. Search product")
            print("3. Filter by category")
            print("4. Sort by price")
            print("5. Sort by rating")
            print("6. Recommend products")
            print("7. Add to cart")
            print("8. View cart")
            print("9. Checkout")
            print("10. Apply promo code")
            print("11. View order history")
            print("0. Back")

            customer_choice = input("Enter choice: ")

            try:

                if customer_choice == "1":

                    show_all_products(products)

                elif customer_choice == "2":

                    keyword = input(
                        "Enter product name: "
                    )

                    result = search_product(
                        products,
                        keyword
                    )

                    show_all_products(result)

                elif customer_choice == "3":

                    category = input(
                        "Enter category: "
                    )

                    result = filter_by_category(
                        products,
                        category
                    )

                    show_all_products(result)

                elif customer_choice == "4":

                    result = sort_by_price(products)

                    show_all_products(result)

                elif customer_choice == "5":

                    result = sort_by_rating(products)

                    show_all_products(result)

                elif customer_choice == "6":

                    category = input(
                        "Enter category: "
                    )

                    result = recommend_products(
                        products,
                        category
                    )

                    show_all_products(result)

                elif customer_choice == "7":

                    product_id = int(
                        input("Enter product ID: ")
                    )

                    quantity = int(
                        input("Enter quantity: ")
                    )

                    product = find_product_by_id(
                        products,
                        product_id
                    )

                    if product is not None:

                        customer.add_to_cart(
                            product,
                            quantity
                        )

                    else:
                        print("Product not found.")

                elif customer_choice == "8":

                    customer.view_cart()

                elif customer_choice == "9":

                    checkout(customer, orders)

                    save_products(
                        products,
                        "products.json"
                    )

                elif customer_choice == "10":

                    product_id = int(
                        input("Enter product ID: ")
                    )

                    promo_code = input(
                        "Enter promo code: "
                    )

                    product = find_product_by_id(
                        products,
                        product_id
                    )

                    if product is not None:

                        final_price = apply_promo_code(
                            product.price,
                            promo_code
                        )

                        print(
                            "Original price:",
                            product.price
                        )

                        print(
                            "Final price:",
                            final_price
                        )

                    else:
                        print("Product not found.")

                elif customer_choice == "11":

                    customer.view_order_history()

                elif customer_choice == "0":
                    break

                else:
                    print("Invalid choice.")

            except ValueError:
                print("Invalid input.")

    elif main_choice == "0":

        print("Program finished.")

        break

    else:
        print("Invalid choice.")