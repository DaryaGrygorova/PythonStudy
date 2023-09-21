class Car():
    has_wheels = True
    quantity_of_wheels = 4

    def print_color(self):
        print(self.color)
        self.say_hello()

    @staticmethod
    def say_hello():
        print('hello')


class Truck(Car):               # наслідування від класу Car
    quantity_of_wheels = 8


class Suv(Car):
    quantity_of_wheels = 4


class Automobile(Truck, Suv):
    def __init__(self, name):
        self.name = name


    def test_method(self, first_param):
        print(first_param)
    quantity_of_wheels = None
    locals = locals()


my_automobile = Automobile("Volvo")
my_other_automobile = Automobile("BMW")
print('quantity_of_wheels' in my_automobile.locals)
