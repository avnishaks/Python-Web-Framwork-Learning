import mysql.connector
from prettytable import PrettyTable;
my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Avnish@123",
)

record_process = my_database.cursor()
# my_database creation
record_process.execute("create database if not exists my_database")

# using of my_database ( DataBase)
record_process.execute("use my_database")

# Creating of Sign Up Table if earlier not existed !
record_process.execute("create table if not exists SignUp(username varchar(30),password varchar(30))")

# Creating of Account - Details Table for the Account Holder !
record_process.execute("create table if not exists account_detail(name varchar(30),account_no varchar(30),address varchar(30),contact_no varchar(30),total_balance int)")

# Creating of Amount Table for the Account Holder !
record_process.execute("create table if not exists amount(name varchar(30),account_no varchar(30),total_balance int)")


# Open Account Function
def openAccount():
    name=input("Enter the Full Name of A/C Holder : ")
    account_no=input("Enter the A/C Number : ")
    address=input("Enter the Permanent Address of the A/C Holder : ")
    contact_no=input("Enter the Contact Number of A/C Holder : ")
    total_balance=int(input("Enter the Opening Amount For Account ! Please Enter Above 5000 : "))

    while(total_balance<5000):
        print("\t\t ⚠️You have Entered Amount Less than 5000 ! Please enter > 5000⚠️\t\t")
        total_balance=int(input("🔂 Amount must be greater than 5000 🔂 : "))

    # Account Details Table Data insertions

    account_holder_query="insert into account_detail(name, account_no, address, contact_no, total_balance) values(%s,%s,%s,%s,%s)"
    account_holder_data = (name, account_no, address, contact_no, total_balance)
    record_process.execute(account_holder_query, account_holder_data)

    # Amount Table Data Insertions

    amount_query="insert into amount (name, account_no, total_balance) values(%s,%s,%s)"
    amount_data = (name, account_no, total_balance)
    record_process.execute(amount_query,amount_data)

    my_database.commit()

    record_process.execute("select * from account_detail")
    data =record_process.fetchall()
    t=PrettyTable(['name', 'account_no', 'address', 'contact_no', 'total_balance'])
    for name, account_no, address, contact_no, total_balance in data:
        t.add_row([name, account_no, address, contact_no, total_balance])
    print(t)

    print("🚀 DATA ENTERED ! ACCOUNT OPENED 🚀")


# Deposite Amount Function
def depositeAmount():
    name = input("Enter the Full Name of A/C Holder : ")
    account_no = input("Enter the A/C Number : ")
    deposite_amount=int(input("Enter the total Amount you want to Deposite"))

    record_process.execute("update account_detail set total_balance=total_balance+"+deposite_amount+'where account_no='+account_no+'')
    my_database.commit()
    '''
      record_process.execute("select total_balance from account_detail where account_no="+str(account_no))
    data=record_process.fetchall()
    t=PrettyTable(['total_balance'])
    for total_balance in data:
        t.add_row([total_balance])
    print("Amount Deposited SuccessFully\n")
    print(t)
    '''
    print("Amount Deposited SuccessFully\n")


# Withdrwan Amount Function
def withdrawAmount():
    return
# Balance Enquiry Function
def balanceEnquiry():
    return
# Customer Details Function
def customerDetails():
    return
# Information Update Function
def informationUpdate():
    return
# Dispaly Information Function
def displayInformation():
    return
# Closing of Account
def closeAccount():
    return




# For the New User Sign Up Function
def SignUp():
    print("WELCOME TO ! 🛴 SIGN-UP PAGE  🛴")
    user_name=input("UserName : ")
    pass_word=input("Password : ")

    # To Check if the User Already have opened the Account

    record_process.execute("select username from SignUp")
    get_user = record_process.fetchall()
    temp_user = []
    for i in range(len(get_user)):
        temp_user.append(get_user[i][0])

    record_process.execute("select password from SignUp")
    get_pass = record_process.fetchall()
    temp_pass = []
    for i in range(len(get_pass)):
        temp_pass.append(get_pass[i][0])

    if (user_name in temp_user) or (pass_word in temp_pass):
        print("\t\t⚠️!!💥HELLO HELLO ! PLEASE WAIT 💥!! 🚀DATA MATCHED ! LOOK-LIKE YOU HAVE ALREDY SIGN-UP , PLEASE LOG-IN DIRECTLY 🚀 ⚠️\t\t\n")
        LogIn()
        return

    # If its a new Account then you should redirect to new Account - creation method !

    sql = "insert into SignUp (username, password) values (%s, %s)"
    val=(user_name,pass_word)
    record_process.execute(sql,val)
    my_database.commit()
    print("Sign Up ! Completed 🚀🏝️🚀 \n")
    print("Please ! Now Log in to your Account with Username and Password")
    LogIn()


# For the Existing User Log in Function
def LogIn():
    print("WELCOME TO ! 🛴 LOGIN PAGE :- ENTER YOUR DETAILS 🛴")
    user_name = input("UserName : ")
    pass_word = input("Password : ")
    record_process.execute("select username from SignUp")
    get_user=record_process.fetchall()
    temp_user=[]
    for i in range(len(get_user)):
        temp_user.append(get_user[i][0])

    record_process.execute("select password from SignUp")
    get_pass=record_process.fetchall()
    temp_pass=[]
    for i in range(len(get_pass)):
        temp_pass.append(get_pass[i][0])

    if(user_name not in temp_user) or (pass_word not in temp_pass):
        print("!!💥OOPS💥!! 🚀WRONG PASSWORD🚀")
    # If the User have entered the code by mistaken , then it provide user the option to Retry the Option
        flag=1
        while True:
            f=int(input("🔂 Press 1 🔂 for Again Try To Login: "))
            if f==1:
                LogIn()
            else:
                exit()
    else:
        print("🧑‍🚒 !! HURRAY !! LOG-IN INTO ACCOUNT 🧑‍🚒")
        print("\t 🕉️ SERVICES OFFERED BY BANK 🕉️ \n")
        while True:
            print("\t1: 🚀 OPEN ACCOUNT\t\n")
            print("\t2: 🚀 DEPOSIT AMOUNT\t\n")
            print("\t3: 🚀 WITHDRAW AMOUNT\t\n")
            print("\t4: 🚀 BALANCE ENQUIRY\t\n")
            print("\t5: 🚀 CUSTOMER DETAILS\t\n")
            print("\t6: 🚀 INFORMATION UPDATE\t\n")
            print("\t7: 🚀 DISPLAY INFORMATION\t\n")
            print("\t8: 🚀 CLOSE ACCOUNT\t\n")
            print("\n\n\t\t !!WARNING!!🏝️ Please Enter the Numerical Number From ➡️1-8   ⬅️ as Per Choice.🏝️!\t\t\n")
            print("\t\t⚠️!PRESS!  ⚠️ANY NUMBER ➡️< 0 or 9 >   ⬅️TO EXIT FROM  🏧 Banking Service 🏧\t\t\n ")
            choice=int(input("! Enter the Choice of the Service which you Want !"))
            if choice==1:
                openAccount()
            elif choice==2:
                depositeAmount()
            elif choice==3:
                withdrawAmount()
            elif choice==4:
                balanceEnquiry()
            elif choice==5:
                customerDetails()
            elif choice==6:
                informationUpdate()
            elif choice==7:
                displayInformation()
            elif choice==8:
                closeAccount()
            else:
                print("! 🙏  Thank You  🙏 , For Using Our 🏧 Banking Service 🏧  !")
                break


# Driver Code

print("\t\t\t|---------->>>> BANKING MANAGEMENT SYSTEM <<<<--------------|\t\t\t")
print("Please Choose Below Two Option !\n")
print("\t1:Sign Up \n \t2:Log in\n")
print("For the New User Please Select (Sign Up) => 1 \nFor the Existing User Please Select (Log in) => 2\n")


options=int(input("Choose the Options : Sign Up / Log in < 1 / 2 > :"))

if options==1:
    SignUp()
elif options==2:
    LogIn()
else:
    print("Please Try < 1 or 2 > ! Oops !! Wrong Attempt")

