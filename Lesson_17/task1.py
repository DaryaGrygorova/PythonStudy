"""Task 1 - Method overloading.
Create a base class named Animal with a method called talk and then
create two subclasses: Dog and Cat, and make their own implementation
of the method talk be different. For instance, Dog’s can be to print
'woof, woof', while Cat’s can be to print 'meow'.

Also, create a simple generic function, which takes as input instance
of a Cat or Dog classes and performs talk method on input parameter.
"""


class Animal:
    """Base class named Animal with a method called talk"""

    def talk(self):
        """Return greeting"""
        return "Hello, I'm animal!"


class Dog(Animal):
    """Create instance of Animal that talking like a dog"""

    greeting = "Woof, woof!"

    def __init__(self, name):
        self.name = name

    def talk(self):
        """Return greeting"""
        return Dog.greeting


class Cat(Animal):
    """Create instance of Animal that talking like a dog"""

    greeting = "Meow!"

    def __init__(self, name):
        self.name = name

    def talk(self):
        """Return greeting"""
        return Cat.greeting


def print_greeting(animal):
    """Print how the animal speaks"""
    print(animal.talk())


my_dog = Dog("Pulya")
my_cat = Cat("Dushka")

print_greeting(my_dog)
print_greeting(my_cat)
