import mysql.connector
from prettytable import PrettyTable;
my = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Avnish@123",
)

process=my.cursor()

process.execute("create database if not exists my")

process.execute("use my")




process.execute("create table if not exists up(username varchar(30),password varchar(30))")

process.execute("create table if not exists down(number int)")

s="insert into down(number) values(%s)"
v=[456]


process.execute(s,v)

my.commit()
process.execute("select *from down")
data = process.fetchall()
t=PrettyTable(['number'])
for number in data:
    t.add_row([number])


print(t)



def fun():
    value=90
    process.execute("update down set number=number+"+str(value))

    process.execute("select *from down")
    data = process.fetchall()
    for x in data:
        print(x)

fun()