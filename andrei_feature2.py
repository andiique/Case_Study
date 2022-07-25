import tkinter as tk
import tkinter.font as font
from tkinter import ttk
import sqlite3

# connect to database , "conn" means connection
conn = sqlite3.connect('product.db')

# create a cursor "c"
c = conn.cursor()

# commit our command
conn.commit()
many_products = [
    ('Barbie Doll', '$19.99', 'In stock', 'dolls'),
    ('Ken Doll', '$18.99', 'In stock', 'dolls'),
    ('Nerf Gun', '$7.99', 'Low stock', 'gun toys'),
    ('Race Car', '$23.99', 'Out of stock', 'cars')
]
c.executemany("INSERT INTO products VALUES (?,?,?,?)", many_products)
categories = [
    "dolls",
    "gun toys",
    "cars"
]
# Query the database
c.execute("SELECT * FROM products")
product_list = c.fetchall()
print(product_list)


def put():
    c.execute("INSERT INTO reviews VALUES('%s')" % review.get())
    conn.commit()
    status.set('Review submitted.')


def display_products(list_box):
    # product_list.sort(key=lambda e: e[1], reverse=True)

    for i, (name, price, quantity, category) in enumerate(product_list, start=1):
        list_box.insert("", "end", values=(i, name, price, quantity, category))


def product_lookup(entry, lookup_box):
    c.execute("SELECT rowid, * FROM products WHERE item_name LIKE '%" + entry + "%'")
    for row in c:
        print(row)  # this print's purpose is to test if everything works fine before implementing the lookup box.
        lookup_box.insert("", "end", values=(row[0], row[1], row[2], row[3]))


def category_lookup(selection, lookup_box):
    c.execute("SELECT rowid, * FROM products WHERE category LIKE '%" + selection + "%'")
    for row in c:
        print(row)
        lookup_box.insert("", "end", values=(row[0], row[1], row[2], row[3]))


def catalogue():
    window2 = tk.Toplevel(customer_page)
    window2.geometry("1000x500")
    window2.configure(bg='#CDD7A4')
    window2.title("Toys Catalogue")
    title2 = tk.Label(window2,
                      text="Toys Catalogue",
                      font=("Georgia", 26, 'bold'))
    title2.grid(row=2, column=4)
    # create tree view with 4 columns
    cols = ('Item code', 'Item name', 'Price', 'Quantity', 'Category')
    list_box = ttk.Treeview(window2, columns=cols, show='headings')
    for col in cols:
        list_box.heading(col, text=col)
    list_box.grid(rowspan=5, column=0, columnspan=8)
    display_products(list_box)
    list_box.bind('<ButtonRelease-1>', select_item)


def select_item(self):  # added self and a (event)
    test_str_library = self.list_box.item(self.list_box.selection())  # gets all the values of the selected row
    print('The test_str = ', type(test_str_library), test_str_library,
          '\n')  # prints a dictionary of the selected row
    item = self.list_box.selection()[0]  # which row did you click on
    print('item clicked ', item)  # variable that represents the row you clicked on
    print(self.list_box.item(item)['values'][0])  # prints the first value of the values (the id value)


def search():
    window3 = tk.Toplevel(customer_page)
    window3.geometry("1000x500")
    window3.configure(bg='#CDD7A4')
    window3.title("Search")
    title3 = tk.Label(window3,
                      text="Searching Engine",
                      font=("Georgia", 26, 'bold'))
    title3.grid(row=2, column=12)
    #  entry_frame = tk.Frame(window3)
    entry_label = tk.Label(window3,
                           text='Search for a product.',
                           font=lbl_font)
    # product_lookup()
    entry_label.grid(row=5, column=12)
    entry_entry = tk.Entry(window3,
                           font=lbl_font)
    entry_entry.grid(row=16, column=12)
    lookup_button = tk.Button(master=window3,
                              text='search',
                              command=lambda: product_lookup(entry_entry.get(), lookup_box))
    cols = ('Item code', 'Item name', 'Price', 'Quantity', 'Category')
    lookup_box = ttk.Treeview(window3, columns=cols, show='headings')
    for col in cols:
        lookup_box.heading(col, text=col)
    lookup_box.grid(row=20, column=12)
    blank_label1 = tk.Label(window3)
    blank_label1.grid(row=4, column=12)
    lookup_button.grid(row=17, column=12)


def category():
    window4 = tk.Toplevel(customer_page)
    window4.geometry("1000x500")
    window4.configure(bg='#CDD7A4')
    window4.title("Search")
    title4 = tk.Label(window4,
                      text="Searching Engine",
                      font=("Georgia", 26, 'bold'))
    title4.grid(row=2, column=12)
    entry_label = tk.Label(window4,
                           text='Search by category.',
                           font=lbl_font)
    entry_label.grid(row=5, column=12)

    category_combo = ttk.Combobox(window4, value=categories)
    category_combo.grid(row=6, column=12)
    lookup_button = tk.Button(master=window4,
                              text='search',
                              command=lambda: category_lookup(category_combo.get(), lookup_box))

    cols = ('Item code', 'Item name', 'Price', 'Quantity', 'Category')
    lookup_box = ttk.Treeview(window4, columns=cols, show='headings')
    for col in cols:
        lookup_box.heading(col, text=col)
    lookup_box.grid(row=20, column=12)
    blank_label1 = tk.Label(window4)
    blank_label1.grid(row=4, column=12)
    lookup_button.grid(row=17, column=12)


def reviews():
    window5 = tk.Toplevel(customer_page)
    window5.geometry("800x400")
    window5.configure(bg='#CDD7A4')
    window5.title("Review Page")
    title5 = tk.Label(window5,
                      text="Review Section",
                      font=("Georgia", 26, 'bold'))
    title5.grid(row=2, column=12)
    review_label = tk.Label(window5,
                            text="Enter your review here.")
    review_label.grid(row=3, column=12)
    review_entry = tk.Entry(window5,
                            textvariable=review)
    review_entry.grid(row=4, column=12)
    review_button = tk.Button(window5,
                              text='Submit',
                              command=put)
    review_button.grid(row=5, column=12)


def center_window_on_screen(window):
    """This centres the window when it is not maximised.  It
    uses the screen and window height and width variables
    defined in the program below."""

    x_cord = int((screen_width / 2) - (width / 2))
    y_cord = int((screen_height / 2) - (height / 2))
    window.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


customer_page = tk.Tk()
customer_page.title('AllAboutToys Ltd.')
width, height = 800, 400
screen_width = customer_page.winfo_screenwidth()
screen_height = customer_page.winfo_screenheight()
center_window_on_screen(customer_page)
customer_page.minsize(width="600", height="300")
lbl_font = font.Font(family='Arial', size=16)
title = tk.Label(customer_page,
                 text="Customer's Page",
                 font=("Georgia", 26, 'bold'))
title.grid(row=2, column=5)
review = tk.StringVar()
status = tk.StringVar()
search_button = tk.Button(customer_page,
                          text='Search',
                          command=search)
search_button.grid(row=5, column=3)
search_button.config(height="2", width="12")
catalogue_button = tk.Button(customer_page,
                             text='Catalogue',
                             command=catalogue)
catalogue_button.grid(row=6, column=3)
catalogue_button.config(height="2", width="12")
category_button = tk.Button(customer_page,
                            text='Category',
                            command=category)
category_button.grid(row=7, column=3)
category_button.config(height="2", width="12")
reviews_button = tk.Button(customer_page,
                           text='Review Section',
                           command=reviews)
reviews_button.grid(row=8, column=3)
reviews_button.config(height="2", width="12")
blank_label = tk.Label(customer_page)
blank_label.grid(row=2, column=1)

customer_page.mainloop()

# close connection
conn.close()
