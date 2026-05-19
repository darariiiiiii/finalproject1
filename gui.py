import tkinter as tk
from tkinter import ttk, messagebox

# ================= WINDOW =================

window = tk.Tk()
window.title("Online Store Simulation")
window.geometry("1600x900")
window.configure(bg="#D4D7D5")

# ================= COLORS =================

BG = "#D4D7D5"
WHITE = "#FFFFFF"
BLUE = "#6E86B3"
DARK = "#082567"
RED = "#C00000"
GREEN = "#3B9C5D"
TEXT = "#082567"
SIDEBAR = "#B4BECF"

# ================= DATA =================

products = [
    [1, "iPhone 15", "Electronics", 450000, 5, 4.8],
    [2, "Samsung S24", "Electronics", 420000, 4, 4.7],
    [3, "Nike Hoodie", "Clothing", 35000, 8, 4.6]
]

cart = []
orders = []

# ================= STYLE =================

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background=WHITE,
    foreground=TEXT,
    fieldbackground=WHITE,
    rowheight=45,
    font=("Trebuchet MS", 11)
)

style.configure(
    "Treeview.Heading",
    background=BLUE,
    foreground=WHITE,
    font=("Trebuchet MS", 11, "bold")
)

# ================= HEADER =================

header = tk.Frame(window, bg=BLUE, height=80)
header.pack(fill="x")

logo = tk.Label(
    header,
    text="👜 Online Store Simulation",
    bg=BLUE,
    fg=WHITE,
    font=("Trebuchet MS", 24, "bold")
)

logo.pack(side="left", padx=30, pady=20)

# ================= MAIN =================

main = tk.Frame(window, bg=BG)
main.pack(fill="both", expand=True)

# ================= SIDEBAR =================

sidebar = tk.Frame(main, bg=SIDEBAR, width=240)
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
    font=("Trebuchet MS", 18, "bold")
)

cart_title.pack(pady=20)

cart_listbox = tk.Listbox(
    cart_panel,
    bg=WHITE,
    fg=TEXT,
    font=("Trebuchet MS", 11),
    height=15
)

cart_listbox.pack(fill="x", padx=20)

total_label = tk.Label(
    cart_panel,
    text="Total: 0 KZT",
    bg=SIDEBAR,
    fg=TEXT,
    font=("Trebuchet MS", 15, "bold")
)

total_label.pack(pady=20)

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

def update_total():

    total = 0

    for item in cart:
        total += item[3]

    total_label.config(
        text=f"Total: {total} KZT"
    )

def refresh_dashboard():

    for item in dashboard_table.get_children():
        dashboard_table.delete(item)

    for product in products:

        dashboard_table.insert(
            "",
            tk.END,
            values=product
        )

def get_selected_product():

    selected = dashboard_table.focus()

    if not selected:
        return None

    return dashboard_table.item(selected)["values"]

def add_to_cart():

    product = get_selected_product()

    if not product:
        return

    cart.append(product)

    cart_listbox.insert(
        tk.END,
        f"{product[1]} - {product[3]} KZT"
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
        return

    total = 0

    for item in cart:
        total += item[3]

    orders.append([
        len(orders) + 1,
        "Completed",
        total
    ])

    refresh_orders()

    cart.clear()

    cart_listbox.delete(0, tk.END)

    update_total()

    messagebox.showinfo(
        "Success",
        "Checkout completed!"
    )

def view_details():

    product = get_selected_product()

    if not product:
        return

    messagebox.showinfo(
        "Details",
        f"""
Product: {product[1]}
Category: {product[2]}
Price: {product[3]}
Stock: {product[4]}
Rating: {product[5]}
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

# ================= SIDEBAR BUTTONS =================

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
        padx=25,
        pady=18,
        font=("Trebuchet MS", 13, "bold")
    )

tk.Label(
    sidebar,
    text="MENU",
    bg=SIDEBAR,
    fg=TEXT,
    font=("Trebuchet MS", 12, "bold")
).pack(anchor="w", padx=25, pady=(30, 10))

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
    font=("Trebuchet MS", 25, "bold")
)

title.pack(anchor="w", padx=20, pady=20)

card = tk.Frame(dashboard_page, bg=WHITE)
card.pack(fill="both", expand=True, padx=20, pady=10)

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
    height=10
)

for col in columns:

    dashboard_table.heading(col, text=col)

    dashboard_table.column(col, width=140, anchor="center")

dashboard_table.pack(fill="both", expand=True, padx=20, pady=20)

# ================= BUTTONS =================

buttons_frame = tk.Frame(card, bg=WHITE)
buttons_frame.pack(pady=20)

def action_button(text, color, command):

    return tk.Button(
        buttons_frame,
        text=text,
        bg=color,
        fg=WHITE,
        relief="flat",
        width=16,
        height=2,
        font=("Trebuchet MS", 12, "bold"),
        command=command
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

# ================= ADMIN =================

admin_title = tk.Label(
    admin_page,
    text="⚙ Admin Panel",
    bg=BG,
    fg=TEXT,
    font=("Trebuchet MS", 24, "bold")
)

admin_title.pack(anchor="w", padx=20, pady=20)

admin_card = tk.Frame(admin_page, bg=WHITE)
admin_card.pack(fill="both", expand=True, padx=20, pady=20)

form = tk.Frame(admin_card, bg=WHITE)
form.pack(pady=20)

name_entry = tk.Entry(form, width=20)
name_entry.grid(row=0, column=0, padx=10)

category_entry = tk.Entry(form, width=20)
category_entry.grid(row=0, column=1, padx=10)

price_entry = tk.Entry(form, width=15)
price_entry.grid(row=0, column=2, padx=10)

def add_product():

    try:

        new_product = [
            len(products) + 1,
            name_entry.get(),
            category_entry.get(),
            int(price_entry.get()),
            10,
            5.0
        ]

        products.append(new_product)

        refresh_dashboard()

        admin_table.insert(
            "",
            tk.END,
            values=new_product
        )

    except:
        pass

tk.Button(
    form,
    text="Add Product",
    bg=DARK,
    fg=WHITE,
    relief="flat",
    padx=20,
    pady=10,
    command=add_product
).grid(row=0, column=3, padx=10)

admin_table = ttk.Treeview(
    admin_card,
    columns=columns,
    show="headings",
    height=8
)

for col in columns:

    admin_table.heading(col, text=col)

    admin_table.column(col, width=120, anchor="center")

admin_table.pack(fill="x", padx=20, pady=20)

for product in products:

    admin_table.insert("", tk.END, values=product)

# ================= ORDERS =================

orders_title = tk.Label(
    orders_page,
    text="📄 Order History",
    bg=BG,
    fg=TEXT,
    font=("Trebuchet MS", 24, "bold")
)

orders_title.pack(anchor="w", padx=20, pady=20)

orders_card = tk.Frame(orders_page, bg=WHITE)
orders_card.pack(fill="both", expand=True, padx=20, pady=20)

orders_table = ttk.Treeview(
    orders_card,
    columns=("ID", "Status", "Total"),
    show="headings",
    height=10
)

orders_table.heading("ID", text="Order ID")
orders_table.heading("Status", text="Status")
orders_table.heading("Total", text="Total")

orders_table.pack(fill="x", padx=20, pady=20)

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
    command=return_product
).pack(pady=10)

# ================= PROFILE =================

profile_title = tk.Label(
    profile_page,
    text="👤 My Profile",
    bg=BG,
    fg=TEXT,
    font=("Trebuchet MS", 24, "bold")
)

profile_title.pack(anchor="w", padx=20, pady=20)

profile_card = tk.Frame(profile_page, bg=WHITE)
profile_card.pack(fill="both", expand=True, padx=20, pady=20)

tk.Label(
    profile_card,
    text="Name: Symbat",
    bg=WHITE,
    fg=TEXT,
    font=("Trebuchet MS", 16)
).pack(pady=20)

tk.Label(
    profile_card,
    text="Email: symbat@aitu.kz",
    bg=WHITE,
    fg=TEXT,
    font=("Trebuchet MS", 16)
).pack()

tk.Label(
    profile_card,
    text="Role: Admin",
    bg=WHITE,
    fg=TEXT,
    font=("Trebuchet MS", 16)
).pack(pady=10)

# ================= START =================

refresh_dashboard()

show_page(dashboard_page)

window.mainloop()