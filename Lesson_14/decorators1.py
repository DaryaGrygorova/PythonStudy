import time


def deco(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(round((end - start), 5))
        return res
    return wrapper


@deco
def fun_func():
    print("Print from start of fun_func")
    time.sleep(3)
    print("Print from end of fun_func")


fun_func()
