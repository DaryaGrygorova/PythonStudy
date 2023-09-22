"""Task 2 - Doggy age
Create a class Dog with class attribute 'age_factor' equals to 7.
Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human
equivalent."""


class Dog:
    """Create dog object with attributes age, age_factor and method
    `human_age` which returns the dog’s age in human equivalent"""

    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        """Returns the dog’s age in human equivalent"""
        return self.age * self.age_factor


sharik = Dog(5)
sharik.human_age()
