"""

Exception Handling is Done in Python Using Mainly Three Keywords:-

1. Try
2. Except
3. Finally

We can dedicate the logic , if in case some error comes up ! In Case , of writting the code.

"""

# Complete Package of code without throwing an error

try:
    print("Hello Avnish Kumar , Founder of Tech and Travel")
    print("Multiplication of 5*3 gives output ", 15)
    f=open('sample.txt','w')
    f.write("Sardar Vallav Bhai Patel , brings integrity and unity of country. ")
except:
    print("Hello! Oops Something went wrong here ||")

finally:
    print("The real truth of life lies between birth and death. ")
    f = open('sample.txt', 'r')
    print("After reading the File statement is :  " , f.read())



print("!!!  After Handling the ERRORS using exceot and also working with finally keyword   !!!")

# Complete Package of Code with error containing in it.


try:
    print("Hello Avnish Kumar , Founder of Tech and Travel")
    print("Multiplication of 5*3 gives output ", 15)
    f=open('sample.txt','r')
    f.write("Sardar Vallav Bhai Patel , brings integrity and unity of country. ")
except:
    print("ERRORS :::  Hello! Oops Something went wrong here ||")

finally:
    print("The real truth of life lies between birth and death. ")
    f = open('sample.txt', 'r')
    print("After reading the File statement is :  " , f.read())


