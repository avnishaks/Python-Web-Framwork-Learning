
# Problem -1

s="django"

print(s[0])

print(s[-1])

print(s[:4])

print(s[1:4])

print(s[::-1])


# Problem-2

list=[1,2,3,[4,5,'hello']]

print(list[3][2])

list[3][2]='goodbye'

print(list)


# Problem -3

dict1={'simple key':'hello calling'}

dict2={'key':{'simple key':'hello calling'}}

dict3={'key':[{'nested key':['this is deep',['hello calling']]}]}


print('Value of Dict 1' ,dict1['simple key'])


print('Value of Dict 2' , dict2['key']['simple key'])


print("Value of Dict 2", dict3['key'][0]['nested key'][1])



# Problem -4

mylist=[1,1,1,2,2,2,2,3,3,3,3,4,4,5,5]

print(set(mylist))


# Problem -5

amount=1000000000000000

name ="Avnish"

statements="Hello ! My name is :{x} , I want to earn :{y}".format(x=name,y=amount)

print(statements)