import time


def decorator(some_attr):
    def inner_deco(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(some_attr, *args, **kwargs)
            end = time.time()
            print(round((end - start), 5))
            return res
        return wrapper
    return inner_deco


@decorator('some_attr')
# equals fun_func = decorator('some_attr')(fun_func) => inner_deco(fun_func)
def fun_func(*args):
    print("Print from start of fun_func")
    print([*args])
    time.sleep(3)
    print("Print from end of fun_func")


fun_func()
