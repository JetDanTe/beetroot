"""Task 1

Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make their own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplemented("Must be implemented by a sub class")


class Cat(Animal):
    def talk(self):
        return "Meow"


class Dog(Animal):
    def talk(self):
        return "Woof"


animals = [Cat("Garfield"), Dog("Hans"), Cat("Maja")]

for animal in animals:
    if input(f"What does the {animal} say?\n") == animal.talk():
        print("Correct")
    else:
        print(f"The {animal} say {animal.talk}")



