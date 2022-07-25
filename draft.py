# create a table
c.execute("""CREATE TABLE products (
        item_name text,
        price integer,
        quantity integer,
        category text
    )""")

c.execute("""CREATE TABLE reviews (
        review text
    )""")

# add products to the table
many_products = [
                    ('Barbie Doll', '$19.99', 'In stock', 'dolls'),
                    ('Ken Doll', '$18.99', 'In stock', 'dolls'),
                    ('Nerf Gun', '$7.99', 'Low stock', 'gun toys'),
                    ('Race Car', '$23.99', 'Out of stock', 'cars')
                ]
c.executemany("INSERT INTO products VALUES (?,?,?,?)", many_products)

# delete records
c.execute("DELETE FROM products WHERE rowid = 8")

# select category
c.execute("SELECT * FROM products WHERE category = (?)",(product_category))

#Lookup with WHERE
c.execute("SELECT rowid, * FROM products WHERE item_name LIKE '%" + entry + "%'")


button = Tk.Button(master=frame, text='press', command= lambda: action(someNumber))