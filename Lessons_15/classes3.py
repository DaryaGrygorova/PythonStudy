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
    def __init__(self, name):
        self.name = name

    quantity_of_wheels = 4


class Automobile(Truck, Suv):
    def __init__(self, name,  production_year):
        super().__init__(self, name)            # виклик конструктора батьківського класу super()
        Suv.__init__(self, name)                # аналог super(), для конкретного батьківського класу
        self.production_year = production_year

    def test_method(self, first_param):
        print(first_param)
    quantity_of_wheels = None
    locals = locals()


my_automobile = Automobile("Volvo", 2010)
my_other_automobile = Automobile("BMW", 1987)

