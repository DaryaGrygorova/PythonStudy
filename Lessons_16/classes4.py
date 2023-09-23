"""Decorator @property, .getter, .setter, .deletter"""
class Employee:
    """Create object employee"""
    def __init__(self, first, second):  # initialization
        self.first = first
        self.second = second

    @property           #not working if .getter method exist
    def full_name(self):
        """Return full name of employee"""
        print("i am in @property")
        return f"{self.first} {self.second}"

    @full_name.setter
    def full_name(self, full_name):
        print("I am setting full name")
        self.first, self.second = full_name.split()

    @full_name.deleter
    def full_name(self):
        print("I am deleting full name")

    @full_name.getter
    def full_name(self):
        print(f"I am get full name")

    def my_class_method(self):
        print(f"I am works with {self}")

    @staticmethod
    def my_static_method():
        print("I am works")


employee_1 = Employee("Jenny", "Smith")   # instantiation
employee_1.my_static_method()
employee_1.my_class_method()
print(employee_1.full_name)
print('____________')
