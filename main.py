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


products = [
    Electronics(1, "iPhone 15", 450000, 5, 4.8, 12),
    Electronics(2, "Samsung Galaxy S24", 420000, 3, 4.7, 12),
    Electronics(3, "Wireless Mouse", 12000, 15, 4.5, 6),
    Clothing(4, "Nike Hoodie", 35000, 8, 4.6, "M"),
    Clothing(5, "Adidas T-Shirt", 18000, 10, 4.3, "L"),
    Food(6, "Chocolate Box", 7000, 20, 4.9, "2026-12-01"),
    Food(7, "Coffee Pack", 8500, 0, 4.4, "2026-10-15")
]


while True:
    print("\n===== PRODUCT MENU =====")
    print("1. Show all products")
    print("2. Search product")
    print("3. Filter by category")
    print("4. Show available products")
    print("5. Sort by price")
    print("6. Sort by rating")
    print("7. Recommend products")
    print("8. Apply promo code")
    print("9. Reduce stock")
    print("0. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            show_all_products(products)

        elif choice == "2":
            keyword = input("Enter product name: ")
            result = search_product(products, keyword)
            show_all_products(result)

        elif choice == "3":
            category = input("Enter category: ")
            result = filter_by_category(products, category)
            show_all_products(result)

        elif choice == "4":
            result = filter_available_products(products)
            show_all_products(result)

        elif choice == "5":
            result = sort_by_price(products)
            show_all_products(result)

        elif choice == "6":
            result = sort_by_rating(products)
            show_all_products(result)

        elif choice == "7":
            category = input("Enter category: ")
            result = recommend_products(products, category)
            show_all_products(result)

        elif choice == "8":
            product_id = int(input("Enter product ID: "))
            promo_code = input("Enter promo code: ")

            product = find_product_by_id(products, product_id)

            if product is not None:
                final_price = apply_promo_code(product.price, promo_code)
                print("Original price:", product.price, "KZT")
                print("Final price:", final_price, "KZT")
            else:
                print("Product not found.")

        elif choice == "9":
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))

            product = find_product_by_id(products, product_id)

            if product is not None:
                product.reduce_stock(quantity)
            else:
                print("Product not found.")

        elif choice == "0":
            print("Program finished.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input. Please enter a number.")