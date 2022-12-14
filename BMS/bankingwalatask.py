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
record_process.execute("create table if not exists SignUp(username varchar(255),password varchar(255))")

# Creating of Account - Details Table for the Account Holder !
record_process.execute("create table if not exists account_detail(name varchar(255),account_no varchar(255),address varchar(255),contact_no varchar(255),total_balance varchar(255))")

#display PreetyTable
def displayPreetyTable():
    data = record_process.fetchall()
    t = PrettyTable(['name', 'account_no', 'address', 'contact_no', 'total_balance'])
    for name, account_no, address, contact_no, total_balance in data:
        t.add_row([name, account_no, address, contact_no, total_balance])
    print(t)


# Update Contact Number
def Update_Contact_Number(account_no):
    contact_no_update = input("Enter the Updated Contact Number of A/C Holder : ")
    print("๐๏ธ Before Updating the Contact Number  ๐๏ธ")
    record_process.execute("select * from account_detail where account_no=" + str(account_no))
    displayPreetyTable()
    record_process.execute("update account_detail set contact_no=" +contact_no_update+' where account_no = '+str(account_no)+';')
    my_database.commit()
    record_process.execute("select * from account_detail where account_no=" + str(account_no))
    print("๐๏ธAfter  Updating the Contact Number  ๐๏ธ")
    displayPreetyTable()


# Open Account Function
def openAccount():
    name=input("Enter the Full Name of A/C Holder : ")
    account_no=input("Enter the A/C Number : ")
    address=input("Enter the Permanent Address of the A/C Holder : ")
    contact_no=input("Enter the Contact Number of A/C Holder : ")
    total_balance=input("Enter the Opening Amount For Account ! Please Enter Above 5000 : ")

    while(int(total_balance)<5000):
        print("\t\t โ?๏ธYou have Entered Amount Less than 5000 ! Please enter > 5000โ?๏ธ\t\t")
        total_balance=input("๐ Amount must be greater than 5000 ๐ : ")

    # Account Details Table Data insertions
    account_holder_query="insert into account_detail(name, account_no, address, contact_no, total_balance) values(%s,%s,%s,%s,%s)"
    account_holder_data = (name, account_no, address, contact_no, total_balance)
    record_process.execute(account_holder_query, account_holder_data)
    my_database.commit()
    displayInformation()
    print("๐ DATA ENTERED ! ACCOUNT OPENED ๐")


# Deposite Amount Function
def depositeAmount():
    name = input("Enter the Full Name of A/C Holder : ")
    account_no = input("Enter the A/C Number : ")
    deposite_amount=input("Enter the total Amount you want to Deposite : ")
    print("๐ฐ Before Addition of Amount in the Account updated Table Details ๐ฐ")
    displayInformation()
    record_process.execute("update account_detail set total_balance=total_balance+"+str(deposite_amount)+' where account_no = '+str(account_no)+';')
    my_database.commit()
    print("๐ต Success ๐ถ ๐ท  Amount Deposited ๐ฐ\n")
    print("๐ฐ After Addition of Amount in the Account updated Table Details ๐ฐ")
    displayInformation()




# Withdrwan Amount Function
def withdrawAmount():
    name = input("Enter the Full Name of A/C Holder : ")
    account_no = input("Enter the A/C Number : ")
    withdrawn_amount = input("Enter the total Amount you want to WithDrawn : ")
    print("๐ฐ Before WithDrawn of Amount in the Account updated Table Details ๐ฐ")
    displayInformation()
    record_process.execute("update account_detail set total_balance=total_balance-" + str(withdrawn_amount) + ' where account_no = ' + str(account_no) + ';')
    my_database.commit()
    print("๐ต Success ๐ถ ๐ท  Amount WithDrawn ๐ฐ\n")
    print("๐ฐ After  WithDrawn of Amount in the Account updated Table Details ๐ฐ")
    displayInformation()

# Balance Enquiry Function
def balanceEnquiry():
    account_no = input("Enter the A/C Number : ")
    record_process.execute("select total_balance from account_detail where account_no="+str(account_no))
    data=record_process.fetchall()
    t=PrettyTable(['total_balance'])
    for total_balance in data:
        t.add_row([total_balance])
    print(t)


# Customer Details Function
def customerDetails():
    account_no = input("Enter the A/C Number : ")
    record_process.execute("select * from account_detail where account_no=" + str(account_no))
    data = record_process.fetchall()
    t = PrettyTable(['name', 'account_no', 'address', 'contact_no', 'total_balance'])
    for name, account_no, address, contact_no, total_balance in data:
        t.add_row([name, account_no, address, contact_no, total_balance])
    print(t)

# Information Update Function
def informationUpdate():
    account_no = input("Enter the A/C Number : ")
    while True:
        print("\t1: ๐ UPDATE CONTACT NUMBER\t\n")
        print("\t2: ๐ UPDATE ADDRESS, NAME , TB , ACCOUNT NUMBER \t\n")
        options=int(input("\t\tEnter your choice โก๏ธ< 1 / 2 >  โฌ๏ธfor Updation!\t\t\n"))
        if options==1:
            Update_Contact_Number(account_no)
        else:
            print("Address , Name , Total Balance and Account Number is in Restricted Mode ! It can't be Updated")
            break




# Dispaly Information Function
def displayInformation():
    record_process.execute("select * from account_detail")
    data = record_process.fetchall()
    t = PrettyTable(['name', 'account_no', 'address', 'contact_no', 'total_balance'])
    for name, account_no, address, contact_no, total_balance in data:
        t.add_row([name, account_no, address, contact_no, total_balance])
    print(t)

# Closing of Account
def closeAccount():
    print("\t\t ๐ Account Details Table : Before Closing of Account ๐ \t\t")
    displayInformation()
    name = input("Enter the Full Name of A/C Holder : ")
    account_no = input("Enter the A/C Number : ")
    record_process.execute("delete from account_detail where account_no="+str(account_no))
    my_database.commit()
    print("\t\t ๐ Account Details Table : After Closing of Account ๐ \t\t")
    displayInformation()





# For the New User Sign Up Function
def SignUp():
    print("WELCOME TO ! ๐ด SIGN-UP PAGE  ๐ด")
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
        print("\t\tโ?๏ธ!!๐ฅHELLO HELLO ! PLEASE WAIT ๐ฅ!! ๐DATA MATCHED ! LOOK-LIKE YOU HAVE ALREDY SIGN-UP , PLEASE LOG-IN DIRECTLY ๐ โ?๏ธ\t\t\n")
        LogIn()
        return

    # If its a new Account then you should redirect to new Account - creation method !

    sql = "insert into SignUp (username, password) values (%s, %s)"
    val=(user_name,pass_word)
    record_process.execute(sql,val)
    my_database.commit()
    print("Sign Up ! Completed ๐๐๏ธ๐ \n")
    print("Please ! Now Log in to your Account with Username and Password")
    LogIn()


# For the Existing User Log in Function
def LogIn():
    print("WELCOME TO ! ๐ด LOGIN PAGE :- ENTER YOUR DETAILS ๐ด")
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
        print("!!๐ฅOOPS๐ฅ!! ๐WRONG PASSWORD๐")
    # If the User have entered the code by mistaken , then it provide user the option to Retry the Option
        flag=1
        while True:
            flag=int(input("๐ Press 1 ๐ for Again Try To Login: "))
            if flag==1:
                LogIn()
            else:
                exit()
    else:
        print("๐งโ๐ !! HURRAY !! LOG-IN INTO ACCOUNT ๐งโ๐")
        print("\t ๐๏ธ SERVICES OFFERED BY BANK ๐๏ธ \n")
        while True:
            print("\t1: ๐ OPEN ACCOUNT\t\n")
            print("\t2: ๐ DEPOSIT AMOUNT\t\n")
            print("\t3: ๐ WITHDRAW AMOUNT\t\n")
            print("\t4: ๐ BALANCE ENQUIRY\t\n")
            print("\t5: ๐ CUSTOMER DETAILS\t\n")
            print("\t6: ๐ INFORMATION UPDATE\t\n")
            print("\t7: ๐ DISPLAY INFORMATION\t\n")
            print("\t8: ๐ CLOSE ACCOUNT\t\n")
            print("\n\n\t\t !!WARNING!!๐๏ธ Please Enter the Numerical Number From โก๏ธ1-8   โฌ๏ธ as Per Choice.๐๏ธ!\t\t\n")
            print("\t\tโ?๏ธ!PRESS!  โ?๏ธANY NUMBER โก๏ธ< 0 or 9 >   โฌ๏ธTO EXIT FROM  ๐ง Banking Service ๐ง\t\t\n ")
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
                print("! ๐  Thank You  ๐ , For Using Our ๐ง Banking Service ๐ง  !")
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

