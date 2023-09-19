class Car():
    def print_color(self):  # метод класу, виконання якого залежить від екземпляру
        print(self.color)
        self.say_hello()    # метод доступний до виклику до об'явлення

    @staticmethod   # статичний метод класу, не залежить від екземпляру
    def say_hello():
        print('hello')


vw = Car()
Car.color = "black"
vw.color = "green"

vw.print_color()
# Car.print_color() # помилка, self в середині метода звертається до екземплаяра класу, а не до самого класу
Car.print_color(vw)
