from products import (
    Electronics,
    Clothing,
    Food
)

from file_manager import (
    load_products,
    save_products
)

import tkinter as tk
from tkinter import ttk, messagebox

# ================= WINDOW =================

window = tk.Tk()
window.title("Online Store Simulation")
window.geometry("1650x920")
window.configure(bg="#E9EDF5")

# ================= COLORS =================

BG = "#E9EDF5"
WHITE = "#FFFFFF"
BLUE = "#6E86B3"
DARK = "#102B6A"
RED = "#D62828"
GREEN = "#3FA45B"
TEXT = "#102B6A"
SIDEBAR = "#C7D0E0"
CARD = "#F8FAFD"

# ================= DATA =================

products = load_products("products.json")

cart = []
orders = []

discounted_total = 0

# ================= DISCOUNTS =================

class Discount:

    def apply_discount(self, price):
        return price


class PercentageDiscount(Discount):

    def __init__(self, percent):
        self.percent = percent

    def apply_discount(self, price):

        discount_amount = price * self.percent / 100

        return price - discount_amount


class FixedDiscount(Discount):

    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, price):

        final_price = price - self.amount

        if final_price < 0:
            return 0

        return final_price


def apply_promo_code(price, promo_code):

    promo_code = promo_code.upper()

    if promo_code == "SALE10":

        discount = PercentageDiscount(10)

        return discount.apply_discount(price)

    elif promo_code == "WELCOME5000":

        discount = FixedDiscount(5000)

        return discount.apply_discount(price)

    else:
        return price

# ================= STYLE =================

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background=WHITE,
    foreground=TEXT,
    fieldbackground=WHITE,
    rowheight=42,
    font=("Trebuchet MS", 11),
    borderwidth=0
)

style.configure(
    "Treeview.Heading",
    background=BLUE,
    foreground=WHITE,
    font=("Trebuchet MS", 11, "bold")
)

style.map(
    "Treeview",
    background=[("selected", "#4E6D8F")]
)

# ================= HEADER =================

header = tk.Frame(window, bg=BLUE, height=90)
header.pack(fill="x")

logo = tk.Label(
    header,
    text="👜 Online Store Simulation",
    bg=BLUE,
    fg=WHITE,
    font=("Trebuchet MS", 28, "bold")
)

logo.pack(side="left", padx=35, pady=20)

# ================= MAIN =================

main = tk.Frame(window, bg=BG)
main.pack(fill="both", expand=True)

# ================= SIDEBAR =================

sidebar = tk.Frame(main, bg=SIDEBAR, width=250)
sidebar.pack(side="left", fill="y")

# ================= CONTENT =================

content = tk.Frame(main, bg=BG)
content.pack(side="left", fill="both", expand=True)

# ================= CART =================

cart_panel = tk.Frame(main, bg=SIDEBAR, width=320)
cart_panel.pack(side="right", fill="y")

cart_title = tk.Label(
    cart_panel,
    text="🛒 Shopping Cart",
    bg=SIDEBAR,
    fg=TEXT,
    font=("Trebuchet MS", 20, "bold")
)

cart_title.pack(pady=25)

cart_listbox = tk.Listbox(
    cart_panel,
    bg=WHITE,
    fg=TEXT,
    font=("Trebuchet MS", 11),
    height=16,
    bd=0
)

cart_listbox.pack(fill="x", padx=20)

promo_label = tk.Label(
    cart_panel,
    text="Promo Code",
    bg=SIDEBAR,
    fg=TEXT,
    font=("Trebuchet MS", 12, "bold")
)

promo_label.pack(pady=(20, 5))

promo_entry = tk.Entry(
    cart_panel,
    font=("Trebuchet MS", 12),
    justify="center"
)

promo_entry.pack(padx=20, fill="x")

discount_label = tk.Label(
    cart_panel,
    text="Discount: 0 KZT",
    bg=SIDEBAR,
    fg=GREEN,
    font=("Trebuchet MS", 13, "bold")
)

discount_label.pack(pady=(20, 5))

total_label = tk.Label(
    cart_panel,
    text="Total: 0 KZT",
    bg=SIDEBAR,
    fg=TEXT,
    font=("Trebuchet MS", 18, "bold")
)

total_label.pack(pady=10)

# ================= PAGES =================

dashboard_page = tk.Frame(content, bg=BG)
admin_page = tk.Frame(content, bg=BG)
orders_page = tk.Frame(content, bg=BG)
profile_page = tk.Frame(content, bg=BG)

for page in (
    dashboard_page,
    admin_page,
    orders_page,
    profile_page
):
    page.place(relwidth=1, relheight=1)

# ================= FUNCTIONS =================

def show_page(page):
    page.tkraise()


def calculate_total():

    total = 0

    for item in cart:
        total += item.price

    return total


def update_total():

    global discounted_total

    total = calculate_total()

    promo = promo_entry.get()

    discounted_total = apply_promo_code(total, promo)

    discount_amount = total - discounted_total

    discount_label.config(
        text=f"Discount: {discount_amount:.0f} KZT"
    )

    total_label.config(
        text=f"Total: {discounted_total:.0f} KZT"
    )


def refresh_dashboard():

    for item in dashboard_table.get_children():
        dashboard_table.delete(item)

    for product in products:

        dashboard_table.insert(
            "",
            tk.END,
            values=(
                product.product_id,
                product.name,
                product.category,
                product.price,
                product.stock,
                product.rating
            )
        )


def get_selected_product():

    selected = dashboard_table.focus()

    if not selected:
        return None

    values = dashboard_table.item(selected)["values"]

    product_id = values[0]

    for product in products:

        if product.product_id == product_id:
            return product

    return None


def add_to_cart():

    product = get_selected_product()

    if not product:

        messagebox.showwarning(
            "Warning",
            "Please select a product."
        )

        return

    cart.append(product)

    cart_listbox.insert(
        tk.END,
        f"{product.name} — {product.price} KZT"
    )

    update_total()


def remove_from_cart():

    selected = cart_listbox.curselection()

    if not selected:
        return

    index = selected[0]

    cart.pop(index)

    cart_listbox.delete(index)

    update_total()


def checkout():

    if len(cart) == 0:

        messagebox.showwarning(
            "Warning",
            "Cart is empty."
        )

        return

    orders.append([
        len(orders) + 1,
        "Completed",
        discounted_total
    ])

    refresh_orders()

    cart.clear()

    cart_listbox.delete(0, tk.END)

    promo_entry.delete(0, tk.END)

    update_total()

    messagebox.showinfo(
        "Success",
        "Checkout completed successfully!"
    )


def view_details():

    product = get_selected_product()

    if not product:
        return

    messagebox.showinfo(
        "Product Details",
        f"""
Product: {product.name}

Category: {product.category}

Price: {product.price} KZT

Stock: {product.stock}

Rating: {product.rating}
"""
    )


def refresh_orders():

    for item in orders_table.get_children():
        orders_table.delete(item)

    for order in orders:

        tag = "completed"

        if order[1] == "Returned":
            tag = "returned"

        orders_table.insert(
            "",
            tk.END,
            values=order,
            tags=(tag,)
        )


def return_product():

    selected = orders_table.focus()

    if not selected:
        return

    item = orders_table.item(selected)["values"]

    order_id = item[0]

    for order in orders:

        if order[0] == order_id:
            order[1] = "Returned"

    refresh_orders()


def add_product():

    try:

        category = category_entry.get()

        # Electronics
        if category == "Electronics":

            new_product = Electronics(
                len(products) + 1,
                name_entry.get(),
                int(price_entry.get()),
                int(stock_entry.get()),
                float(rating_entry.get()),
                12
            )

        # Clothing
        elif category == "Clothing":

            new_product = Clothing(
                len(products) + 1,
                name_entry.get(),
                int(price_entry.get()),
                int(stock_entry.get()),
                float(rating_entry.get()),
                "M"
            )

        # Food
        elif category == "Food":

            new_product = Food(
                len(products) + 1,
                name_entry.get(),
                int(price_entry.get()),
                int(stock_entry.get()),
                float(rating_entry.get()),
                "2026-12-01"
            )

        else:

            messagebox.showerror(
                "Error",
                "Invalid category."
            )

            return

        products.append(new_product)

        save_products(products, "products.json")

        refresh_dashboard()

        admin_table.insert(
            "",
            tk.END,
            values=(
                new_product.product_id,
                new_product.name,
                new_product.category,
                new_product.price,
                new_product.stock,
                new_product.rating
            )
        )

        name_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        stock_entry.delete(0, tk.END)
        rating_entry.delete(0, tk.END)

        messagebox.showinfo(
            "Success",
            "Product added successfully!"
        )

    except:

        messagebox.showerror(
            "Error",
            "Invalid product data."
        )

# ================= SIDEBAR =================

def sidebar_button(text, command):

    return tk.Button(
        sidebar,
        text=text,
        command=command,
        bg=SIDEBAR,
        fg=TEXT,
        activebackground=DARK,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        anchor="w",
        padx=30,
        pady=18,
        font=("Trebuchet MS", 14, "bold"),
        cursor="hand2"
    )

tk.Label(
    sidebar,
    text="MENU",
    bg=SIDEBAR,
    fg=TEXT,
    font=("Trebuchet MS", 13, "bold")
).pack(anchor="w", padx=30, pady=(35, 15))

sidebar_button(
    "🏠 Dashboard",
    lambda: show_page(dashboard_page)
).pack(fill="x")

sidebar_button(
    "⚙ Admin Panel",
    lambda: show_page(admin_page)
).pack(fill="x")

sidebar_button(
    "📄 Order History",
    lambda: show_page(orders_page)
).pack(fill="x")

sidebar_button(
    "👤 My Profile",
    lambda: show_page(profile_page)
).pack(fill="x")

# ================= DASHBOARD =================

title = tk.Label(
    dashboard_page,
    text="👜 Dashboard",
    bg=BG,
    fg=TEXT,
    font=("Trebuchet MS", 28, "bold")
)

title.pack(anchor="w", padx=30, pady=25)

card = tk.Frame(
    dashboard_page,
    bg=CARD,
    bd=0
)

card.pack(fill="both", expand=True, padx=30, pady=10)

columns = (
    "ID",
    "Product",
    "Category",
    "Price",
    "Stock",
    "Rating"
)

dashboard_table = ttk.Treeview(
    card,
    columns=columns,
    show="headings",
    height=12
)

for col in columns:

    dashboard_table.heading(col, text=col)

    dashboard_table.column(
        col,
        width=150,
        anchor="center"
    )

dashboard_table.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=25
)

# ================= BUTTONS =================

buttons_frame = tk.Frame(card, bg=CARD)
buttons_frame.pack(pady=15)

def action_button(text, color, command):

    return tk.Button(
        buttons_frame,
        text=text,
        bg=color,
        fg=DARK,
        relief="flat",
        width=16,
        height=2,
        font=("Trebuchet MS", 12, "bold"),
        command=command,
        cursor="hand2"
    )

action_button(
    "👁 View Details",
    DARK,
    view_details
).pack(side="left", padx=10)

action_button(
    "🛒 Add To Cart",
    BLUE,
    add_to_cart
).pack(side="left", padx=10)

action_button(
    "❌ Remove",
    RED,
    remove_from_cart
).pack(side="left", padx=10)

action_button(
    "👜 Checkout",
    GREEN,
    checkout
).pack(side="left", padx=10)

# ================= ADMIN PANEL =================

admin_title = tk.Label(
    admin_page,
    text="⚙ Admin Panel",
    bg=BG,
    fg=TEXT,
    font=("Trebuchet MS", 28, "bold")
)

admin_title.pack(anchor="w", padx=30, pady=25)

admin_card = tk.Frame(admin_page, bg=CARD)
admin_card.pack(fill="both", expand=True, padx=30, pady=10)

form = tk.Frame(admin_card, bg=CARD)
form.pack(pady=25)

name_entry = tk.Entry(form, width=20, font=("Trebuchet MS", 11))
name_entry.grid(row=0, column=0, padx=8)

category_entry = tk.Entry(form, width=18, font=("Trebuchet MS", 11))
category_entry.grid(row=0, column=1, padx=8)

price_entry = tk.Entry(form, width=12, font=("Trebuchet MS", 11))
price_entry.grid(row=0, column=2, padx=8)

stock_entry = tk.Entry(form, width=10, font=("Trebuchet MS", 11))
stock_entry.grid(row=0, column=3, padx=8)

rating_entry = tk.Entry(form, width=10, font=("Trebuchet MS", 11))
rating_entry.grid(row=0, column=4, padx=8)

tk.Button(
    form,
    text="Add Product",
    bg=DARK,
    fg=WHITE,
    relief="flat",
    padx=20,
    pady=10,
    font=("Trebuchet MS", 11, "bold"),
    command=add_product,
    cursor="hand2"
).grid(row=0, column=5, padx=10)

admin_table = ttk.Treeview(
    admin_card,
    columns=columns,
    show="headings",
    height=10
)

for col in columns:

    admin_table.heading(col, text=col)

    admin_table.column(
        col,
        width=140,
        anchor="center"
    )

admin_table.pack(
    fill="x",
    padx=25,
    pady=20
)

# ================= ORDERS =================

orders_title = tk.Label(
    orders_page,
    text="📄 Order History",
    bg=BG,
    fg=TEXT,
    font=("Trebuchet MS", 28, "bold")
)

orders_title.pack(anchor="w", padx=30, pady=25)

orders_card = tk.Frame(
    orders_page,
    bg=CARD
)

orders_card.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)

orders_table = ttk.Treeview(
    orders_card,
    columns=("ID", "Status", "Total"),
    show="headings",
    height=12
)

orders_table.heading("ID", text="Order ID")
orders_table.heading("Status", text="Status")
orders_table.heading("Total", text="Total")

orders_table.column("ID", width=180, anchor="center")
orders_table.column("Status", width=250, anchor="center")
orders_table.column("Total", width=250, anchor="center")

orders_table.pack(
    fill="x",
    padx=25,
    pady=25
)

orders_table.tag_configure(
    "completed",
    foreground="green"
)

orders_table.tag_configure(
    "returned",
    foreground="red"
)

tk.Button(
    orders_card,
    text="↩ Return Product",
    bg=RED,
    fg=WHITE,
    relief="flat",
    padx=20,
    pady=10,
    font=("Trebuchet MS", 11, "bold"),
    command=return_product,
    cursor="hand2"
).pack(pady=10)

# ================= PROFILE =================

profile_title = tk.Label(
    profile_page,
    text="👤 My Profile",
    bg=BG,
    fg=TEXT,
    font=("Trebuchet MS", 28, "bold")
)

profile_title.pack(anchor="w", padx=30, pady=25)

profile_card = tk.Frame(
    profile_page,
    bg=CARD
)

profile_card.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)

tk.Label(
    profile_card,
    text="Name: Symbat",
    bg=CARD,
    fg=TEXT,
    font=("Trebuchet MS", 18)
).pack(pady=25)

tk.Label(
    profile_card,
    text="Email: symbat@aitu.kz",
    bg=CARD,
    fg=TEXT,
    font=("Trebuchet MS", 18)
).pack()

tk.Label(
    profile_card,
    text="Role: Admin",
    bg=CARD,
    fg=TEXT,
    font=("Trebuchet MS", 18)
).pack(pady=15)

# ================= START =================

refresh_dashboard()

show_page(dashboard_page)

window.mainloop()