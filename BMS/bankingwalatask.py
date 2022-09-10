import mysql.connector
from prettytable import PrettyTable;
my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Avnish@123",
)

record_process=my_database.cursor();

record_process.execute("create database if not exists my_database")
record_process.execute("use my_database")
record_process.execute("create table if not exists SignUp(username varchar(30),password varchar(30))")



# For the New User Sign Up Function
def SignUp():
    user_name=input("UserName : ")
    pass_word=input("Password : ")
    sql = "insert into SignUp (username, password) values (%s, %s)"
    val=(user_name,pass_word)
    record_process.execute(sql,val)
    my_database.commit()
    print("Sign Up ! SuccessFull \n")
    print("Please ! Now Log in to your Account with Username and Password")
    LogIn()


# For the Existing User Log in Function
def LogIn():
    print("Welcome !! To Log in Page !")
    print("Log In Function Entered")
    record_process.execute("select username from SignUp")
    result=record_process.fetchall()
    for x in result:
        print(x)



# Driver Code

print("\t\t\t|---------->>>> BANKING MANAGEMENT SYSTEM <<<<--------------|\t\t\t")
print("Please Choose Below Two Option !\n")
print("\t1:Sign Up \n \t2:Log in\n")
print("For the New User Please Select (Sign Up) => 1 \nFor the Existing User Please Select (Log in) => 2\n");


options=int(input("Choose the Options : Sign Up / Log in < 1 / 2 > :"))

if options==1:
    SignUp()
elif options==2:
    LogIn()
else:
    print("Please Try < 1 or 2 > ! Oops !! Wrong Attempt")


'''
# Creating an object reference
mycursor = mydb.cursor()

# Creating a DataBase Name called mydatabase!
# At the very first time create a database for single time only
# mycursor.execute("CREATE DATABASE mydatabase")


# Creating a table name called customers
# Create a Table for that given database for the single time only
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# Insert the Multiple Row in the Table - Insertion

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")



# Selecting all the Iteam from the DataBase


Selecting and Displaying all the inserted row and col in the Table



mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()


STIPM=PrettyTable(['name', 'address'])

for name, address in myresult:
    STIPM.add_row([name, address])

print(STIPM)


'''
