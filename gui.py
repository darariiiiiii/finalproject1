import tkinter as tk
from tkinter import ttk, messagebox

# ================= COLORS =================

BG = "#D4D7D5"
SIDEBAR = "#B4BECF"
CARD = "#FFFFFF"
BLUE = "#6E86B3"
DARK = "#082567"
RED = "#C00000"
GREEN = "#3B9C5D"
TEXT = "#082567"
WHITE = "#FFFFFF"

# ================= DATA =================

products = [
    [1, "iPhone 15", "Electronics", 450000, 5, 4.8],
    [2, "Samsung Galaxy S24", "Electronics", 420000, 3, 4.7],
    [3, "Nike Hoodie", "Clothing", 35000, 8, 4.6],
    [4, "Chocolate Box", "Food", 7000, 20, 4.9]
]

cart = []
orders = []

# ================= WINDOW =================

window = tk.Tk()
window.title("Online Store Simulation")
window.geometry("1600x900")
window.configure(bg=BG)

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

sidebar = tk.Frame(main, bg=SIDEBAR, width=250)
sidebar.pack(side="left", fill="y")

# ================= CONTENT =================

content = tk.Frame(main, bg=BG)
content.pack(side="left", fill="both", expand=True)

# ================= CART PANEL =================

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
    relief="flat",
    height=16
)

cart_listbox.pack(fill="x", padx=20)

total_label = tk.Label(
    cart_panel,
    text="Total: 0 KZT",
    bg=SIDEBAR,
    fg=TEXT,
    font=("Trebuchet MS", 14, "bold")
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

        messagebox.showwarning(
            "Warning",
            "Select a product"
        )

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

        messagebox.showwarning(
            "Warning",
            "Cart is empty"
        )

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
        "Order completed successfully!"
    )

def view_details():

    product = get_selected_product()

    if not product:

        messagebox.showwarning(
            "Warning",
            "Select a product"
        )

        return

    info = (
        f"Product: {product[1]}\n"
        f"Category: {product[2]}\n"
        f"Price: {product[3]} KZT\n"
        f"Stock: {product[4]}\n"
        f"Rating: {product[5]}"
    )

    messagebox.showinfo(
        "Product Details",
        info
    )

def refresh_orders():

    for item in orders_table.get_children():
        orders_table.delete(item)

    for order in orders:

        tag = "completed"

        if order[1] == "Cancelled":
            tag = "cancelled"

        orders_table.insert(
            "",
            tk.END,
            values=order,
            tags=(tag,)
        )

# ================= SIDEBAR BUTTONS =================

def menu_button(text, command):

    return tk.Button(
        sidebar,
        text=text,
        command=command,
        bg=SIDEBAR,
        fg=TEXT,
        activebackground=DARK,
        activeforeground=WHITE,
        relief="flat",
        anchor="w",
        padx=25,
        pady=15,
        font=("Trebuchet MS", 12, "bold"),
        cursor="hand2"
    )

tk.Label(
    sidebar,
    text="MENU",
    bg=SIDEBAR,
    fg=TEXT,
    font=("Trebuchet MS", 11, "bold")
).pack(anchor="w", padx=25, pady=(30, 10))

menu_button(
    "🏠 Dashboard",
    lambda: show_page(dashboard_page)
).pack(fill="x")

menu_button(
    "⚙ Admin Panel",
    lambda: show_page(admin_page)
).pack(fill="x")

menu_button(
    "📄 Order History",
    lambda: show_page(orders_page)
).pack(fill="x")

menu_button(
    "👤 My Profile",
    lambda: show_page(profile_page)
).pack(fill="x")

# ================= DASHBOARD PAGE =================

dashboard_title = tk.Label(
    dashboard_page,
    text="👜 Dashboard",
    bg=BG,
    fg=TEXT,
    font=("Trebuchet MS", 24, "bold")
)

dashboard_title.pack(anchor="w", padx=20, pady=20)

dashboard_card = tk.Frame(
    dashboard_page,
    bg=WHITE
)

dashboard_card.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

columns = (
    "ID",
    "Product",
    "Category",
    "Price",
    "Stock",
    "Rating"
)

dashboard_table = ttk.Treeview(
    dashboard_card,
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
    padx=20,
    pady=20
)

buttons_frame = tk.Frame(
    dashboard_card,
    bg=WHITE
)

buttons_frame.pack(
    pady=(0, 20)
)

def action_button(text, color, command):

    return tk.Button(
        buttons_frame,
        text=text,
        bg=color,
        fg=WHITE,
        relief="flat",
        padx=25,
        pady=12,
        font=("Trebuchet MS", 11, "bold"),
        cursor="hand2",
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

# ================= ADMIN PAGE =================

admin_title = tk.Label(
    admin_page,
    text="⚙ Admin Panel",
    bg=BG,
    fg=TEXT,
    font=("Trebuchet MS", 24, "bold")
)

admin_title.pack(anchor="w", padx=20, pady=20)

admin_card = tk.Frame(
    admin_page,
    bg=WHITE
)

admin_card.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

form_frame = tk.Frame(
    admin_card,
    bg=WHITE
)

form_frame.pack(fill="x", padx=30, pady=30)

# NAME

tk.Label(
    form_frame,
    text="Product Name",
    bg=WHITE,
    fg=TEXT,
    font=("Trebuchet MS", 11, "bold")
).grid(row=0, column=0, sticky="w", pady=(0, 8))

name_entry = tk.Entry(
    form_frame,
    font=("Trebuchet MS", 11),
    width=20
)

name_entry.grid(row=1, column=0, padx=10)

# CATEGORY

tk.Label(
    form_frame,
    text="Category",
    bg=WHITE,
    fg=TEXT,
    font=("Trebuchet MS", 11, "bold")
).grid(row=0, column=1, sticky="w", pady=(0, 8))

category_entry = tk.Entry(
    form_frame,
    font=("Trebuchet MS", 11),
    width=18
)

category_entry.grid(row=1, column=1, padx=10)

# PRICE

tk.Label(
    form_frame,
    text="Price",
    bg=WHITE,
    fg=TEXT,
    font=("Trebuchet MS", 11, "bold")
).grid(row=0, column=2, sticky="w", pady=(0, 8))

price_entry = tk.Entry(
    form_frame,
    font=("Trebuchet MS", 11),
    width=12
)

price_entry.grid(row=1, column=2, padx=10)

# ADD PRODUCT FUNCTION

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

        admin_table.insert(
            "",
            tk.END,
            values=new_product
        )

        refresh_dashboard()

        name_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)

        messagebox.showinfo(
            "Success",
            "Product added successfully!"
        )

    except:

        messagebox.showwarning(
            "Error",
            "Enter valid data"
        )

add_btn = tk.Button(
    form_frame,
    text="Add Product",
    bg=DARK,
    fg=WHITE,
    relief="flat",
    padx=25,
    pady=10,
    font=("Trebuchet MS", 11, "bold"),
    cursor="hand2",
    command=add_product
)

add_btn.grid(row=1, column=3, padx=20)

# ADMIN TABLE

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
    fill="both",
    expand=True,
    padx=30,
    pady=(0, 30)
)

for product in products:

    admin_table.insert(
        "",
        tk.END,
        values=product
    )

# ================= ORDERS PAGE =================

orders_title = tk.Label(
    orders_page,
    text="📄 Order History",
    bg=BG,
    fg=TEXT,
    font=("Trebuchet MS", 24, "bold")
)

orders_title.pack(anchor="w", padx=20, pady=20)

orders_card = tk.Frame(
    orders_page,
    bg=WHITE
)

orders_card.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
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

orders_table.column("ID", width=150, anchor="center")
orders_table.column("Status", width=200, anchor="center")
orders_table.column("Total", width=200, anchor="center")

orders_table.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

orders_table.tag_configure(
    "completed",
    foreground="green"
)

orders_table.tag_configure(
    "cancelled",
    foreground="red"
)

# ================= PROFILE PAGE =================

profile_title = tk.Label(
    profile_page,
    text="👤 My Profile",
    bg=BG,
    fg=TEXT,
    font=("Trebuchet MS", 24, "bold")
)

profile_title.pack(anchor="w", padx=20, pady=20)

profile_card = tk.Frame(
    profile_page,
    bg=WHITE
)

profile_card.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

tk.Label(
    profile_card,
    text="Name: Aruzhan",
    bg=WHITE,
    fg=TEXT,
    font=("Trebuchet MS", 15)
).pack(pady=20)

tk.Label(
    profile_card,
    text="Email: aru@aitu.kz",
    bg=WHITE,
    fg=TEXT,
    font=("Trebuchet MS", 15)
).pack(pady=20)

tk.Label(
    profile_card,
    text="Role: Customer",
    bg=WHITE,
    fg=TEXT,
    font=("Trebuchet MS", 15)
).pack(pady=20)

# ================= START =================

refresh_dashboard()

show_page(dashboard_page)

window.mainloop()