"""
Scope in the Python is quite confusing for the Beginners
We have made some quite easy , methods to get resolved this issues.

Here the Scope follow the Rules of LEGB

-> Local :- When we declare the particular varaible , inside the function then it going to look first into
it.

-> Enclosing Function Deals :- In this , firstly what the variable name is declared , when we call the
function then first , it going to look into the variable name present in the functions then it
going to look , in the outer or global scope if nothing is going to be find inside that vary declared
functions.

-> Global :- Its declare in the global specs , as outside the function.

-> Built-in :- All the function , that present in python package to reduce the complexity of writing code ,
and help in computational task to do in ease manner.

"""


# Local

x="Avnish Kumar"

def my_val():
    x=10
    return x


# local value x return
print(my_val())

#Global value of x return
print(x)


# Enclosing Function Deals



lifes ="Love in Life"
place="native"


# Not Calling the Nested Function

def life():
    place="non-native"
    def love():
        print(lifes, " Brings happiness for ",place)


life()


# Calling the Nested Function

def life():
    place="non-native"
    def love():
        print(lifes, " Brings happiness for ",place)
    love()


life()

# Calling the Global variable inside the nested Function "place"

def life():
    #place="non-native"
    def love():
        print(lifes, " Brings happiness for ",place)
    love()


life()


# Built-in Function in the Python
# Similar way lots of mathematical, logrithmical , and logical in-built function is present
# which we can user it for our healthy computational task.

str="abcddhjkheekhekrw"
print(str.lower())
print(str.capitalize())
print(str.upper())
print(len(str))

