"""

In the Regular Expression , We generally do going to import the python library , which we going to use
to do computational work , to make logical writing of the code , in smooth manner.

1. search
2. split
3. findall


Some Formating To Elimate some symbol to get expreession in form of the List , and removing the special
character.



"""

# Using Importing the Regular Expression

import  re


pattern=['term1','term2']

text='I am looking for the term1 ! nothing other than that !'

for it in pattern:
    print("I am searching :  "+it)
    if re.search(it,text):
        print("MATCH FOUNDED")
    else:
        print("MATCH NOT FOUND")


# For the Finding the index of the match element we just use it also.

match=re.search('term1',text)

print(type(match))

print("Index at which match start or begins : ",match.start())


# Split the string using Regular Expression

split_it='@'

email_id="avnish@aks@gmail.com"

print("Here is the String comes up after Spliting : -  ", re.split(split_it,email_id))


# Getting all the number of match find element from the String

text_given="Avnish is the Founder of T and T company , T and T makes good profit in year 2024."

find="T and T"

print("List of all the match element present in text are as follow : ", re.findall(find,text_given))


# Finding the Pattern of choice present in the phrase

def multi_re(pattern,phrase):
    for pat in pattern:
        print("Searching for the {} ".format(pat))

        print("Here is the List of matching Pattern in Phrase" , re.findall(pat,phrase))

        print('\n')


test_phrase="abcd.......abbb...abc.....aaaabbb....cc...acd"

test_pattern=['a+']
print("One or More number of a in the row Continious")
multi_re(test_pattern,test_phrase)

test_pattern1=['ab*']
print("One a or ab (with single a and more number of b)")
multi_re(test_pattern1,test_phrase)


test_pattern2=['ab?']
print("Single a or just ab nothing else combination")
multi_re(test_pattern2,test_phrase)


# To remove some of the character , and split the string into list by doing that.


test_phrase1="45 This is the String!Oops , but not more Functionality Supported 786 .How! Can you Resolve it?"
test_pattern3=['[^!?.]+']
print("Options of Removing some of the Puncuations Symbol from the String!")
multi_re(test_pattern3,test_phrase1)


#To get the digit only from expression
test_pattern4=[r'\d+']
print("Above Pattern for the Regular Expression Going to Return the Digits only")
multi_re(test_pattern4,test_phrase1)

#To get alpha numric one
test_pattern5=[r'\w+']
print("All the Alpha numeric one string and digit using above regular expression Pattern")
multi_re(test_pattern5,test_phrase1)

# Each individual one
test_pattern6=[r'\w']
print("All the Alpha numeric one string and digit each individual using above regular expression Pattern")
multi_re(test_pattern6,test_phrase1)

# Each Spacing Individula
test_pattern7=[r'\s']
print("All spacing using above regular expression Pattern")
multi_re(test_pattern7,test_phrase1)

