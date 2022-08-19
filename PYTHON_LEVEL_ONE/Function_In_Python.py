def my_fun():
    print("Hello Avnish Kumar")


def my_fu(params):
    print("Most Ideal things people , get from the Parents is the Moral Value")



def addition(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry ! Oops you have Entered Wrong Data Type ! Please Provide Integers"


print(addition(10,17));

my_fun()

my_fu(10)

print(addition("10","20"))



# Filter and Lambda Expressions


dataList=[1,2,3,4,5,6,7,88,9,85,78,61]

print(dataList)


print(list(filter(lambda x:x%2==0,dataList)))


# Split Functionality

string="Hello ! @Dear How its #going #around #this @week"

print(string.split("#"))

print(string.split("@"))

print(string.split("@")[0])

print(string.split("@")[1])

print(string.split("#")[0])

print(string.split("#")[1])
