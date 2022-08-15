# Tuple is not interchangebale other than that all the operation of list is applied here

t=(1,2,3)
print(t)
print(t[0])
print(t[2])

#Assigment Operation is not performed here ! t[2]=5

# Set

s=set()

s.add(1)
s.add(3)
s.add(4)
s.add(1)
s.add(4)
s.add(9)

print(s)


#Boolean is true or False

way=9
def fun(x):
    if x<10:
        return True
    else:
        return False

print(fun(way))
print(fun(15))
