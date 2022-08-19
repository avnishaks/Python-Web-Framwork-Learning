# Elif Block
if 1!=1:
    print("First Block")
elif 'hi'=='hi':
    print("Hi ! Block")
else:
    print("EveryThing")


# If statement

if 1==1:
    print("First Block")
elif 'hi'=='hi':
    print("Hi ! Block")
else:
    print("EveryThing")



# Dictonary Block

dict={'A':123,'B':234,'C':143}

print("Getting the keys iteams present in the Dictonary :- ")

for i in dict.keys():
    print(i)


print("Getting the values iteams present in the Dictonary :- ")

for i in dict.values():
    print(i)

print("Getting the key + values together using Dictonary :- ")

for i in dict:
    print("Keys : ", i, "  Values : ", dict[i])



# Tuples packing and un-packing


mytuple=[(1,2),(3,4),(5,6)]

for (t1,t2) in mytuple:
    print("Value of t1 :- " , t1, " Value of t2 :- " ,t2)


# List with range

demoList=list(range(0,100,10))

print(demoList)



# Append in the List

x=[1,2,3,4,5]

out=[]

for it in x:
    out.append(it**2)

print(out)

# Using the List Comphrensions

demoBox=[(e+10) for e in x]
print(demoBox)



