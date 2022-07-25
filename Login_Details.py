import mysql.connector

mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="MySQL2020",
     database="logindb"
)


mycursor = mydb.cursor()

#mycursor.execute(("CREATE TABLE mainToysCatalouge (Toys_id INT AUTO_INCREMENT PRIMARY KEY,Product_Name VARCHAR (30),Product_Description VARCHAR (255),Product_Serial_Number VARCHAR(30),Product_Price INT)"))

#mycursor.execute("CREATE TABLE ToysCatalouge (Toys_id INT AUTO_INCREMENT PRIMARY KEY,Product_Name VARCHAR (12),ProductSort_code VARCHAR(8))")
# for db in mycursor:
#      print(db)

#mycursor.execute("SHOW TABLES")


