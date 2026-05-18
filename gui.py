import tkinter as tk
from tkinter import messagebox, ttk
from products import Electronics, Clothing, Food, show_all_products
from discounts import apply_promo_code
from users import Customer, Admin

products = [
    Electronics(1, "iPhone 15", 450000, 5, 4.8, 12),
    Electronics(2, "Samsung Galaxy S24", 420000, 3, 4.7, 12),
    Clothing(4, "Nike Hoodie", 35000, 8, 4.6, "M"),
    Food(6, "Chocolate Box", 7000, 20, 4.9, "2026-12-01")
]

current_customer = Customer(101, "Aruzhan", "aru@aitu.kz", "password123")
current_admin = Admin(1, "Erasyl", "admin@aitu.kz", "admin777")

def refresh_product_list():
    product_listbox.delete(0, tk.END)
    for prod in products:
        product_listbox.insert(tk.END, f"[{prod.product_id}] {prod.name} — {prod.price} KZT (Stock: {prod.stock})")


def show_product_details():
    try:
        selected_index = product_listbox.curselection()[0]
        product = products[selected_index]

        info = (
            f"Name: {product.name}\n"
            f"Price: {product.price} KZT\n"
            f"Stock: {product.stock} pcs\n"
            f"Category: {product.category}\n"
            f"Rating: {product.rating} ⭐\n"
            f"Shipping: {product.calculate_shipping()} KZT"
        )

        if isinstance(product, Electronics):
            info += f"\nWarranty: {product.warranty_months} months"
        elif isinstance(product, Clothing):
            info += f"\nSize: {product.size}"
        elif isinstance(product, Food):
            info += f"\nExpiry Date: {product.expiry_date}"

        messagebox.showinfo("Product Details", info)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a product from the list!")


def add_to_cart_gui():
    try:
        selected_index = product_listbox.curselection()[0]
        product = products[selected_index]

        if product.stock > 0:
            current_customer.add_to_cart(product, 1)
            messagebox.showinfo("Cart", f"Product {product.name} added to cart!")
        else:
            messagebox.showerror("Error", "Product is out of stock!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a product to add!")


def view_cart_gui():
    if not current_customer.cart:
        messagebox.showinfo("Cart", "Your cart is empty.")
        return

    cart_window = tk.Toplevel(window)
    cart_window.title("Your Cart")
    cart_window.geometry("350x300")

    cart_text = tk.Text(cart_window, width=40, height=10)
    cart_text.pack(pady=10)

    total = 0
    for item in current_customer.cart:
        prod = item["product"]
        qty = item["quantity"]
        cart_text.insert(tk.END, f"{prod.name} x{qty} — {prod.price * qty} KZT\n")
        total += prod.price * qty

    cart_text.insert(tk.END, f"\nTotal without discount: {total} KZT")
    cart_text.config(state=tk.DISABLED)

    tk.Label(cart_window, text="Enter promo code (SALE10 or WELCOME5000):").pack()
    promo_entry = tk.Entry(cart_window)
    promo_entry.pack(pady=5)

    def check_promo():
        code = promo_entry.get()
        final_price = apply_promo_code(total, code)
        if final_price < total:
            messagebox.showinfo("Success", f"Promo code applied!\nNew price: {final_price} KZT")
        else:
            messagebox.showwarning("Notice", "Promo code not found or not applicable.")

    tk.Button(cart_window, text="Apply Promo Code", command=check_promo, bg="#FF9800", fg="white").pack(pady=5)


def add_product_by_admin():
    admin_window = tk.Toplevel(window)
    admin_window.title("Admin Panel")
    admin_window.geometry("300x250")

    tk.Label(admin_window, text="Product Name:").pack()
    name_entry = tk.Entry(admin_window)
    name_entry.pack()

    tk.Label(admin_window, text="Price:").pack()
    price_entry = tk.Entry(admin_window)
    price_entry.pack()

    tk.Label(admin_window, text="Stock:").pack()
    stock_entry = tk.Entry(admin_window)
    stock_entry.pack()

    def save_new_product():
        try:
            name = name_entry.get()
            price = int(price_entry.get())
            stock = int(stock_entry.get())

            new_prod = Electronics(len(products) + 1, name, price, stock, 5.0, 12)
            current_admin.add_product(products, new_prod)

            refresh_product_list()
            messagebox.showinfo("Success", f"Product {name} successfully added by admin!")
            admin_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for price and stock!")

    tk.Button(admin_window, text="Add to Database", command=save_new_product, bg="#4CAF50", fg="white").pack(pady=10)

window = tk.Tk()
window.title("AITU Smart Store")
window.geometry("500x500")
window.configure(bg="#f5f5f5")

notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True, fill="both")

customer_frame = tk.Frame(notebook, bg="#f5f5f5")
admin_frame = tk.Frame(notebook, bg="#f5f5f5")

notebook.add(customer_frame, text=f"Customer ({current_customer.name})")
notebook.add(admin_frame, text="Admin Mode")

tk.Label(customer_frame, text="Available Products:", font=("Arial", 12, "bold"), bg="#f5f5f5").pack(pady=5)

product_listbox = tk.Listbox(customer_frame, width=50, height=10, font=("Courier", 10))
product_listbox.pack(pady=5)

btn_layout = tk.Frame(customer_frame, bg="#f5f5f5")
btn_layout.pack(pady=10)

tk.Button(btn_layout, text="ℹ️ Product Info", command=show_product_details, width=18).grid(row=0, column=0, padx=5)
tk.Button(btn_layout, text="🛒 Add to Cart", command=add_to_cart_gui, bg="#2196F3", fg="white", width=18).grid(row=0,
                                                                                                              column=1,
                                                                                                              padx=5)
tk.Button(customer_frame, text="🛍️ Open Cart & Promo Codes", command=view_cart_gui, bg="#4CAF50", fg="white",
          width=38).pack(pady=5)

tk.Label(admin_frame, text="Store Management", font=("Arial", 12, "bold"), bg="#f5f5f5").pack(pady=10)
tk.Label(admin_frame, text=f"Logged in as: {current_admin.name}", fg="gray", bg="#f5f5f5").pack()

tk.Button(admin_frame, text="➕ Add New Product", command=add_product_by_admin, bg="#9C27B0", fg="white", width=25,
          height=2).pack(pady=20)

refresh_product_list()

window.mainloop()