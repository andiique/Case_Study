from tkinter import*
from tkinter import messagebox
import time
#import mysql.connector


global username
global password
global first_Name
global surname
global email_Address

def Toys_Catalouge():

    global product_Id
    global product_Name
    global author

    product_Id = int
    product_Name= StringVar()
    author = StringVar()


    screen5=Toplevel(screen)
    screen5.minsize(width="400", height="400")
    screen5.maxsize(width="400", height="400")
    screen5.title("Toys Catalouge")
    screen5.geometry("400x400")
    Label(screen5,text="Welcome to the staff catalogue page", font=("Calibri",20)).pack()
    Label(screen5,text="Product_ID ?").pack()
    Entry(screen5,textvariable=product_Id).pack()
    Label(screen5,text="").pack()
    Label(screen5,text="What is the Product Name ?").pack()
    Entry(screen5,textvariable=product_Name).pack()
    Label(screen5,text="").pack()
    Label(screen5,text="What is the Author's Name ?").pack()
    Entry(screen5,textvariable=author).pack()
    Label(screen5,text="").pack()
    Label(screen5,text="").pack()
    Button(screen5,text="Fetch the details", command=Update_Details).pack()
    Label(screen5,text="").pack()
    Label(screen5,text="").pack()
    Button(screen5,text="Back", command=Back_Toys_Cat).pack()

def Back_Toys_Cat():
     response = messagebox.askyesno('Important Message', "Are u sure you want to go back ? ?")
     if response == True:
         messagebox.showinfo("Important Message", "navigating to the previous page")
         time.sleep(1)
         product_catergories()
     elif response == False:
         # print("unfortunatley it is not possible to continue.")
         messagebox.showinfo("Important Message", "No actions has been taken.")




        # if response == True:
        #     time.sleep(1)
        #     messagebox.showinfo("Important Message", "Fecthing the requested results")
        #     time.sleep(1)
        #     Toys_Catalouge()
        # elif response == False:
        #     # print("unfortunatley it is not possible to continue.")
        #     messagebox.showinfo("Important Message", "No actions has been taken.")


def Update_Details():
    response = messagebox.askyesno('Important Message', "Do you want to see the results ?")
    if response == True:
        messagebox.showinfo("Important Message", "Displaying the Results")
        time.sleep(1)
    elif response == False:
        # print("unfortunatley it is not possible to continue.")
        messagebox.showinfo("Important Message", "No actions has been taken.")



def Products_Page_For_Customer():

    productName=StringVar()
    serialN = int
    authorsName = StringVar()
    bookGenre = StringVar()

    screen4 = Toplevel(screen)
    screen4.title("Customer Product Page")
    screen4.minsize(width="600", height="300")
    screen4.maxsize(width="600", height="300")

    title=Label(screen4,text="Customer's Toys Catalouge",font=("calibri",25))#.pack()
    title.grid(row=2, column=3)

    L1=Label(screen4,text="Product Name")
    L1.grid(row=3, column=2)
    E1=Entry(screen4,textvariable=productName)
    E1.grid(row=4, column=2)

    emptyL1 = Label(screen4)
    emptyL1.grid(row=5, column=2)

    L4=Label(screen4,text="Genre of Book")
    L4.grid(row=6, column=2)
    E4=Entry(screen4,textvariable=bookGenre)
    E4.grid(row=7, column=2)

    emptyL2 = Label(screen4)
    emptyL2.grid(row=8, column=2)

    L2=Label(screen4,text="Product Serial Number")
    L2.grid(row=9, column=2)
    E2=Entry(screen4,textvariable=serialN)
    E2.grid(row=10,column=2)

    emptyL3= Label(screen4)
    emptyL3.grid(row=11,column=2)

    L3=Label(screen4,text="Author's Name")
    L3.grid(row=12, column=2)
    E3=Entry(screen4,textvariable=authorsName)
    E3.grid(row=13, column=2)

    button1=Button(screen4,text="Main Menu", width=10)
    button1.grid(row=15, column=3)
    button2=Button(screen4,text="Exit", width=10)
    button2.grid(row=15 , column= 5)
    # Button(screen4,text="Back to Main Menu").pack()
    # Label(screen4, text="").pack()
    # Button(screen4,text="Exit").pack()

def customer_employee():
    screen3=Toplevel(screen)
    screen3.title("Options")
    screen3.geometry("300x250")
    Label(screen3,text="If you are a customer, then click 'Customer'.").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="If you work for the company, then click 'Work'.").pack()
    Label(screen3, text="").pack()
    Button(screen3,text="Customer", command=customer).pack()
    Label(screen3, text="").pack()
    Button(screen3,text="Work", command=work).pack()


def customer():
    response = messagebox.askyesno('Important Message', "Did you click on the right button? ?")
    if response == True:
        messagebox.showinfo("Important Message", "You will navigated to the Product Catergories")
        time.sleep(1)
        Products_Page_For_Customer()
    elif response == False:
        # print("unfortunatley it is not possible to continue.")
        messagebox.showinfo("Important Message", "No actions has been taken.")



def work():
    response = messagebox.askyesno('Important Message', "Did you click on the right button ?")
    if response == True:
        messagebox.showinfo("Important Message", "You will now go on the Product Details Page")
        time.sleep(1)
        product_catergories()
    else:
        print("You will stay on the current page.")




def product_catergories():

    screen2 = Toplevel(screen)
    screen2.title("Product Catergories")
    #screen2.geometry("500x400")
    screen2.geometry("500x400+500+300")
    Label(screen2,text="").pack()
    Label(screen2,text='Product Description', bg="grey", font=("Calibri", 24)).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Add a new Category",command=Toys_Catalouge, width=20, height=3,).pack() #command=).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Edit a existing catergory", width=20, height=3, ).pack()  # command=).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Delete a category", width=20, height=3, ).pack()  # command=).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Return to Main Menu",command=Return_2, width=20, height=3, ).pack()  # command=).pack()

def Return_2():
    response = messagebox.askyesno('Important Message', "Are u sure you want to go back ?")
    if response == True:
        messagebox.showinfo("Important Message", "You will navigated to the current page")
        time.sleep(1)
        product_catergories()
    elif response == False:
        # print("unfortunatley it is not possible to continue.")
        messagebox.showinfo("Important Message", "You will be navigated to the Main Menu")
        time.sleep(1)
        customer_employee()




def Register():
    from tkinter import messagebox

    global username
    global password
    global first_Name
    global surname
    global email_Address


    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x500+500+20")

    username=StringVar()
    password=StringVar()
    first_Name=StringVar()
    surname=StringVar()
    email_Address=StringVar()

    Label(screen1, text="").pack()
    Label(screen1, bg="lightblue" , font=(16),text="Please enter you username: *").pack()
    Label(screen1, bg="lightblue", font=(16), text="Anything marked with the '*' is mandatory ").pack()
    Label(screen1, text="").pack()
    Label(screen1,text="Username * ").pack()
    Entry(screen1,textvariable=username).pack()
    Label(screen1,text="Password * ").pack()
    Entry(screen1,textvariable=password).pack()
    Label(screen1,text="").pack()
    Label(screen1, text="Enter your first name '*' :").pack()
    Entry(screen1, textvariable=first_Name).pack()
    Label(screen1,text="").pack()
    Label(screen1, text="Enter your surname '*' :").pack()
    Entry(screen1, textvariable=surname).pack()
    Label(screen1,text="").pack()
    Label(screen1, text="Enter in your email address '*' :").pack()
    Entry(screen1, textvariable=email_Address).pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Return to Main Menu", command=Return).pack()
    Label(screen1, text="").pack()
    Button(screen1,text="Register", width=10, height=1, command=register_user).pack()


def register_user():
    result = messagebox.askyesno("Important Message", "Have you already registered with us ? ")
    if result == False:
        register_user()

    if result == True:
        customer_employee()

    #username = StringVar()
    # username_info= username.get()
    # password_info= password.get()
    # first_Name_info=first_Name.get()
    # surname_info=surname.get()
    # email_Address_info=email_Address.get()
    # file=open("File.txt", "a")
    # file.write(username_info + ",")
    # file.write(password_info + ",")
    # file.write(first_Name_info + ",")
    # file.write(surname_info + ",")
    # file.write(email_Address_info + "\n") #Find the /character
    # file.close()
    # #file=open("File.txt","r")
    # username.set("")
    # password.set("")
    # first_Name.set("")
    # surname.set("")
    # email_Address.set("")
    # username_info= username.get()
    # password_info= password.get()
    # first_Name_info=first_Name.get()
    # surname_info=surname.get()
    # email_Address_info=email_Address.get()

    # username_info.append(mysql)
    # password_info.append(mysql)
    # first_Name_info.append(mysql)
    # surname_info.append(mysql)
    # email_Address_info.append(mysql)
    username = ""
    password = ""
    first_Name = ""
    surname = ""
    email_Address = ""

    username.append(mysql)
    password.append(mysql)
    surname.append(mysql)
    first_Name.append(mysql)
    surname.append(mysql)
    email_Address.append(mysql)




    #Label(text = "Registration Success")

def Return():
    response = messagebox.askyesno('Important Message', "Are u sure you want to go back ?")
    if response == True:
        messagebox.showinfo("Important Message", "You will navigated to the Main Menu")
        time.sleep(2)
        #Main_Screen()
    else:
        messagebox.showinfo("Important Information","You will be staying on the page")
    # elif response == False:
    #     # print("unfortunatley it is not possible to continue.")
    #     messagebox.showinfo("Important Message", "You will be navigated to the Main Menu")
    #     time.sleep(1)
    #     customer_employee()


def Login():
    from tkinter import messagebox
    response = messagebox.askyesno('Important Message', "Have u registered ?")
    if response == True:
        messagebox.showinfo("Important Message","You can continue")
        time.sleep(1)
        customer_employee()
    elif response == False:
        #print("unfortunately it is not possible to continue.")
        messagebox.showinfo("Important Message", "You can't continue")
        time.sleep(1)
        register_user()
    # option=input("Have you registered ?")
    # if option == "Yes" or "yes" or "y" or "Y":
    #     print("You can go ahead " + username)
    # elif option == "No" or "N" or "n":
    #     print("You need to register first " + username )

def Main_Screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.maxsize(width="300",height="250")
    screen.minsize(width="300",height="250")
    screen.title("Main_Menu")
    Label(text="Welcome to the Main Menu",  bg="grey", width="300", height="2" , font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="login", width="30", command=Login, height="2").pack()
    Label(text="").pack()
    Button(text="Register", width="30",command=Register, height="2").pack()

    screen.mainloop()

Main_Screen()