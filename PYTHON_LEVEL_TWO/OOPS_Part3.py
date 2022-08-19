"""
In this OOPS Part 3 of the section , we are going to over mainly two topics

1. Inheritance
2. Special Method

"""
# 1. Inheritance Concept is Cleared ! Now
class Animal():
    def __init__(self):
        print("ANIMAL CLASS CREATED")

    def eat(self):
        print("Animal is Eating")

    def hunt(self):
        print("Animal is Hunting")

    def rest(self):
        print("Animal is having a rest")

class Tiger(Animal):
    def __init__(self):
        print("Tiger Class is created")

class Cat(Tiger):
    def __init__(self):
        print("Cat Class is Created")


myCat=Cat();
myCat.rest()
myCat.hunt()
myCat.eat()


# 2. Special Method that we are going to be use in Python


class Book():
    def __init__(self,Author,Title,Year):
        self.Author=Author
        self.Title=Title
        self.Year=Year

    def __str__(self):
        return "Author Name is :{} , Title of the Book : {} , Year of Published : {}".format(self.Author,self.Title,self.Year)

    def __len__(self):
        return self.Year

    def __del__(self):
        print("Book Object is Destroyed")


myBook=Book("Avnish","Oppurtunity",2028)
print(myBook)

print(len(myBook))

del myBook