def deco(func):
    additional_str = 'I am additional string'
    def wrapper(*args, **kwargs):
        return func(additional_str, *args, **kwargs)

    return wrapper


def deco2(func):
    additional_str = 'I am additional string from deco2'
    def wrapper(*args, **kwargs):
        return func(additional_str, *args, **kwargs)

    return wrapper


@deco
def fun_func(*args, fun='fun'):
    print("Print from fun_func: ", end='\n')
    for el in [*args]:
        print(f"{fun}_{el}")
    print('\n')


@deco
@deco2
def fun_func2(*args, fun='fun'):
    print("Print from fun_func2: ", end='\n')
    for element in [*args]:
        print(f"{fun}_{element}")
    print('\n')


fun_func("first argument", "second argument")
fun_func2("first argument", "second argument", fun='Super Fun')
