"""Class decorators"""

def class_decorator(cls):
    """Change __str__ method"""
    class Wrapper(cls):
        """Class wrapper"""
        def __str__(self):
            return "Hello world!"

    return Wrapper

def class_decorator2(cls):
    def new_str():
        return "Hello world!"
    cls.__str__ = new_str
    return cls

@class_decorator
# @class_decorator2
class ProductStore:
    """Prototype of store, with methods for operate with all products in the store"""

    _semiprivate = 1 #напівприватний атрибут. може бути викликаний поза классом
    __privat = 2    #приватний атрибут. Не може бути викликаний поза классом
    test = "In Class"

    def __init__(self, test):
        self.test = test

    def get_semiprivate(self):
        print(self._semiprivate)

    def set_test(self, test):
        self.test = test

    @classmethod # замість екземпляру передає у метод сам клас
    def set_semiprivate(cls):
        cls._semiprivate = 3


    @staticmethod # у метод не передається ні екземпляр, ні сам клас
    def print_arg(*args):
        print(args)


# print(ProductStore().__privat) #Error
new_obj = ProductStore( "In object")
print(new_obj.test) # "In object"
print(ProductStore.test) # "In Class"
