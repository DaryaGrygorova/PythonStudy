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
    quantity_of_wheels = None
    locals = locals()


myAutomobile = Automobile()
print('quantity_of_wheels' in myAutomobile.locals)
