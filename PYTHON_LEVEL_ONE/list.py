mylist=['abcdef',1,2,4,"I am Avnish Kumar",78,'aks']

print(mylist)

print('Length of the Above List iteams ',len(mylist))


print("Before Assigment we have list ", mylist)

mylist[0]="Tanvi"

print("After Assigment we have list , value at assigned index get replaced ",mylist)


mylist.append(89)

print(mylist)

print(mylist[4][:5])

otherlist=['a','b','c','d','e','f']

mylist.extend(otherlist)

print('Extended List of mylist and otherList is : ', mylist)


matrix=[[1,2,3],[4,5,6],[7,8,9]]

iteam=[row[1] for row in matrix]

value1=[row[-1] for row in matrix]

print(value1)

print(iteam)

