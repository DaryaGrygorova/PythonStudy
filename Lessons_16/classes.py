"""Decorator @property"""
class Employee:
    """Create object employee"""
    def __init__(self, first, second):  # initialization
        self.first = first
        self.second = second
        # self.email = f'{self.first[0].lower()}{self.second.lower()}@email.com'

    @property
    # вбудований декоратор що при кожному виклику self.email перераховує
    # та повертає актуальне значення
    # ВАЖЛИВО!!! синтаксис звернення як для атрибуту (без дужок)
    def email(self):
        """Return email"""
        return f'{self.first[0].lower()}{self.second.lower()}@email.com'

    @property           #not working if .getter method exist
    def full_name(self):
        """Return full name of employee"""
        print("i am in @property")
        return f"{self.first} {self.second}"

    @full_name.setter
    # може бути викликаний лише на атрибутах, заданих через декоратор @property
    def full_name(self, full_name):
        # переприсвоєння full_name відбуваєтья автоматично
        # у тілі функції описуються лише додаткові дії при зміні
        # атрибуту full_name
        print("I am setting full name")
        self.first, self.second = full_name.split()

    @full_name.deleter # working only if .getter method exist
    def full_name(self):
        print("I am deleting full name")

    @full_name.getter
    def full_name(self):
        print("I am get full name")


employee_1 = Employee("Jenny", "Smith")   # instantiation
print(employee_1.email)
print(employee_1.full_name)
print('____________')

employee_1.second = "Ford"
print(employee_1.email)
print(employee_1.full_name) # -> property(full_name(self)) or full_name.getter(full_name(self) if .getter exist
print('____________')

employee_1.full_name = "Peter Ford" # -> full_name.setter(full_name(self, new_value))
print(employee_1.full_name)         # -> property(full_name(self)) or full_name.getter(full_name(self) if .getter exist
print(employee_1.first)
print(employee_1.second)
print('____________')

del employee_1.full_name            # -> full_name.deleter(full_name(self)) if .getter and .deleter exist
print(employee_1.full_name)
print('____________')
