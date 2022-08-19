"""
! Every thing in Python is Object , We can also create our own custom object !
"""


# List
listed=[]
print("List Object ",type(listed))


# Tuple
tupled=()
print("Tuple Object ", type(tupled))

# Integer
print("Integer Object ", type(10))

# Float
print("Float Object ", type(1.0))


# String
print("String Object ", type("abcde"))


# dict

dict={}
print("Dictonary Object ", type(dict))


# Custome Class ( / Object )

class Demo():
    pass

demo=Demo()
print("Custome Object of Demo Class ", type(demo))