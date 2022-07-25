import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL2020",
    database="toys_catalouge"
)

mycursor = mydb.cursor()

#mycursor.execute(("CREATE TABLE mainToysCatalouge (Toys_id INT AUTO_INCREMENT PRIMARY KEY,Product_Name VARCHAR (30),Product_Description VARCHAR (255),Product_Serial_Number VARCHAR(30),Product_Price INT)"))

#mycursor.execute("CREATE DATABASE Toys_Catalouge")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#      print(db)
#mycursor.execute("CREATE DATABSE ToysCatalougedb")

# #mycursor.execute("CREATE DATABASE toysCatalougedb")
# sqlFormula = "INSERT INTO ToysCatalougeDB(product_Id(AUTO INCEMENT, INTEGER), product_Name, price) VALUES (%s %s)"
# toysCatalougdb = [
#     ("", "Dolls World Little Treasure (White)", "£10.99")
#     ("", "Dolls World Little Treasure (Blue)", "£9.99")
#     ("", "Disney Princess Rapunzel", "£7.99")
#     ("", "Disney Princess Cinderella", "£7.99")
#     ("", "Disney Princess Elsa", "£7.99")
#     ("", "Drown Cuddly Bear", "£9.30")
#     ("", "Large Cuddly Bear (Brown)", "£11.00")
#     ("", "Medium Cuddly Bear (Pink)", "£12.00")
#     ("", "Pink Unicorn", "£9.99")
# ]
# mycursor.executemany(sqlFormula,toysCatalougdb)
# mydb.commit()