from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import time
import mysql.connector
import Case_Study.Login_Details as ld
import Case_Study.Toys_Catalouge as toysCatalouge


def newProducts():

    global productName
    global productSerialNumber
    global productPrice

    screen6 = Toplevel(screen)
    screen6.title("Maintain Product/Toys")
    screen6.minsize(width=350, height=300)
    screen6.maxsize(width=350, height=300)

    Label(screen6,text="Enter the Product Details",font=("calibri", 25)).pack()
    Label(text="").pack()
    Label(text="").pack()

    Label(screen6,text="Product Name").pack()
    Entry(screen6,textvariable=productName).pack()
    Label(text="").pack()

    Label(screen6,text="Serial Number").pack()
    Entry(screen6,textvariable=productSerialNumber).pack()
    Label(text="").pack()

    Label(screen6,text="Price").pack()
    Entry(screen6,textvariable=productPrice).pack()
    Label(text="").pack()

    #Button(screen6,text="Add Product",command=newProduct)


def Maintain_products():

    screen5 = Toplevel(screen)
    screen5.title("Maintain Product/Toys")
    screen5.minsize(width=350, height=300)
    screen5.maxsize(width=350, height=300)

    Label(screen5,text="Maintain Products",font=("calibri", 25)).pack()
    Label(screen5,text="").pack()
    Label(screen5, text="").pack()

    Label(screen5,text="Add a Product").pack()
    Button(screen5,text="Add Product").pack()#,command=newProduct).pack()
    Label(screen5,text="").pack()

    Label(screen5,text="Edit a Product").pack()
    Button(screen5,text="Edit Product").pack()
    Label(screen5,text="").pack()

    Label(screen5,text="Delete a Product").pack()
    Button(screen5,text="Delete Product").pack()
    Label(screen5,text="").pack()


def Products_Page():

    screen4 = Toplevel(screen)
    screen4.title("Employees Product Page")
    screen4.minsize(width="600", height="300")
    screen4.maxsize(width="600", height="300")

    title = Label(screen4, text="Customer's Toys Catalouge", font=("calibri", 25))  # .pack()
    title.grid(row=1, column=3)

    L1 = Label(screen4, text="Add a category")
    L1.grid(row=3, column=2)
    B1 = Button(screen4, text="Add a category",width=12,height=1)
    B1.grid(row=4, column=2)

    emptyL1 = Label(screen4)
    emptyL1.grid(row=5, column=2)

    L4 = Label(screen4, text="Edit a catergory")
    L4.grid(row=6, column=2)
    B4 = Button(screen4,text="Edit a catergory",width=12,height=1)
    B4.grid(row=7, column=2)

    emptyL2 = Label(screen4)
    emptyL2.grid(row=8, column=2)

    L2 = Label(screen4, text="Delete a Catergory")
    L2.grid(row=9, column=2)
    B2 = Button(screen4,text="Delete a category",width=12,height=1)
    B2.grid(row=10, column=2)

    emptyL3 = Label(screen4)
    emptyL3.grid(row=11, column=2)

    L3 = Label(screen4, text="Maintain Product/Toys")
    L3.grid(row=12, column=2)
    B3 = Button(screen4,text="Maintain Product",width=12,height=1,command=Maintain_products)
    B3.grid(row=13, column=2)

    button1 = Button(screen4, text="Main Menu", width=10)
    button1.grid(row=15, column=3)

    button2 = Button(screen4, text="Exit", width=10)
    button2.grid(row=15, column=5)
    # frame_1=tk.Frame(screen4,width=40, height=20)
    # frame_1.grid(row=3,column=3)#, rowspan=2, columnspan=2)
    #
    # label_01 = tk.Label(frame_1,text="Table")
    # label_01.grid(row=4,column=4)


def work():

    response = messagebox.askyesno('Important Message', "Are you sure ?")
    if response == True:
        messagebox.showinfo("Important Message", "Action has been taken")
        time.sleep(1)
        Products_Page()
        #Login()

    else:
        print("You will stay on the current page.")


def customer_employee():

    screen3 = Toplevel(screen)
    screen3.minsize(width=300, height=250)
    screen3.maxsize(width=300, height=250)

    Label(screen3, text="If you are a customer, then click 'Customer'.").pack()
    Label(screen3, text="").pack()

    Button(screen3, text="Customer").pack()#, command=customer).pack()
    Label(screen3, text="").pack()

    Label(screen3, text="If you work for the company, then click 'Work'.").pack()
    Label(screen3, text="").pack()

    Button(screen3, text="Work", command=work).pack()

def insert_into_db(tbl_name,vals):

    sql_script="INSERT INTO " + tbl_name + "(username,password,firstName,surName,email_address)" + "VALUES(%s,%s,%s,%s,%s)" #SQl script
    ld.mycursor.execute(sql_script,vals)
    ld.mydb.commit() #This is adding to database


def register_user():

    insert_into_db("mainLogindb",(username.get(),password.get(),first_Name.get(),surname.get(),email_Address.get())) #Creating a tuple containing the values

    username.set("")
    password.set("")
    first_Name.set("")
    surname.set("")
    email_Address.set("")


def Return():
    response = messagebox.askyesno('Important Message', "Are u sure you want to go back ?")
    if response == True:
        messagebox.showinfo("Important Message", "You will navigated to the Main Menu")
        time.sleep(2)
        # Main_Screen()
    else:
        messagebox.showinfo("Important Information", "You will be staying on the page")
    # elif response == False:


def Register():

    global username
    global password
    global first_Name
    global surname
    global email_Address
    global username_id
    global username_entry

    global productName
    global productSerialNumber
    global productPrice

    screen1 = Toplevel(screen)
    screen1.title("Register")

    screen1.maxsize(width=400, height=500)
    screen1.minsize(width=400, height=500)

    # username_id = int
    # username_id = str(username_id)
    username = StringVar()
    password = StringVar()
    first_Name = StringVar()
    surname = StringVar()
    email_Address = StringVar()

    Label(screen1, text="").pack()
    Label(screen1, bg="lightblue", font=(16), text="Please enter you username: *").pack()
    Label(screen1, bg="lightblue", font=(16), text="Anything marked with the '*' is mandatory ").pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Username * ").pack()
    Entry(screen1, textvariable=username).pack()

    Label(screen1, text="Password * ").pack()
    Entry(screen1, textvariable=password).pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Enter your first name '*' :").pack()
    Entry(screen1, textvariable=first_Name).pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Enter your surname '*' :").pack()
    Entry(screen1, textvariable=surname).pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Enter in your email address '*' :").pack()
    Entry(screen1, textvariable=email_Address).pack()
    Label(screen1, text="").pack()

    Button(screen1, text="Return to Main Menu", command=Return).pack()
    Label(screen1, text="").pack()

    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def get_from_db(tbl_name,field,where_field,val):

    sql_script=" SELECT " + field + " FROM " + tbl_name + " WHERE " + where_field + " = '" + val + "'"
    ld.mycursor.execute(sql_script)

    result = ld.mycursor.fetchall()

    for x in result:
        return x[0]


def login_check():

    psword=get_from_db("mainLogindb","password","username",login_username.get())

    #print("Entered password",login_password.get())

    messagebox.showinfo("Important Message","Checking the details")

    if login_password.get() == psword:
        messagebox.showinfo("Important Message","You can continue")
        time.sleep(1)

        customer_employee()


    else: #login_username.get() and login_password.get() != username and password:
        messagebox.showinfo("Important Message","Your details do not match. Please try again")


def Login():

    global login_username
    global login_password

    login_username = StringVar()
    login_password = StringVar()

    screen6 = Toplevel(screen)
    screen6.title("Login")

    screen6.maxsize(width=400, height=300)
    screen6.minsize(width=400, height=210)


    Label(screen6, font=("calibri",20), text="welcome to the Login page").pack()
    Label(screen6, text="").pack()
    Label(screen6,text="Username").pack()
    Entry(screen6,textvariable=login_username).pack()
    Label(screen6,text="").pack()
    Label(screen6,text="Password").pack()
    Entry(screen6,show="*",textvariable=login_password).pack()
    Label(screen6,text="").pack()
    Button(screen6,text="Proceed",command=login_check, width=10, height=1).pack()
    Label(screen6,text="").pack()
    Button(screen6,text="Exit",command=quit, width=10, height=1).pack()


def Main_Screen():

    global screen
    global username
    global password
    global first_Name
    global surname
    global email_Address
    global username_id
    global login_username
    global login_password

    screen = Tk()
    #screen.geometry("300x250")
    screen.maxsize(width="300", height="300")
    screen.minsize(width="300", height="300")
    screen.title("Main_Menu")
    Label(text="Welcome to the Main Menu", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="login", width="30", command=Login, height="2").pack()
    Label(text="").pack()
    Button(text="Register", width="30", command=Register, height="2").pack()
    Label(text="").pack()
    Button(text="Exit",command=quit, width="30", height="2").pack()


    screen.mainloop()


Main_Screen()
