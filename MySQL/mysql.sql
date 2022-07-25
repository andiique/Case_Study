import mysql.connector

mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="MySQL2020",
     #database="logindb"
)



CREATE TABLE main_login_details 
(
    user_id   VARCHAR(255)  NOT NULL,
    username  VARCHAR (255) NOT NULL,
    firstname VARCHAR(255)  NOT NULL,
    surname   VARCHAR(255)  NOT NULL,  
    email     VARCHAR(255)  NOT NULL,
);