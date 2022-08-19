class Dog():
    stray="Animals"
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name

mydog=Dog("Huskie","Tommy")
otherdog=Dog("Stray Dog"," Don")

print(mydog.breed,"   ",mydog.name)

print(otherdog.breed,"  ",otherdog.name)

print(mydog.stray)




class Circle():
    pi=3.14
    def __init__(self,radius):
        self.radius=radius;

    def area(self):
        return self.radius*self.radius*Circle.pi;

mycircle=Circle(5)
print(mycircle.area())