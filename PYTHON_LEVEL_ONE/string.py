#Points  to be covered in the string part of the Python

"""
Here we have some Points to be Noted we are going to Cover in this Sections:-

1. String
2. Basics
3. Indexing
4. Slicing
5. Basic Method
6. Print Formating

"""

print(1+2)
#Basics
"""
"I am Avnish Kumar"
'I am Avnish'
"""

print("I am Avnish Kumar")
print("My love of life is Setia")

# string
mystring="Avnish Tanvi"


#Indexing
print(mystring[0])
print(mystring[:])

#Slicing
print(mystring[1:])
print(mystring[::])
print('Here is the statement ',mystring[1::2])
print(mystring[1:2])


#Basic Methods
st="avnishkumarsingh"
y=st.upper()
print(y)
z=st.lower()
print(z)
m=st.capitalize()
print(m)


#Print Formationg

value= "Value of First item: {x} Value of Second item: {y}".format(x="Dog",y="Cat");

print(value)
