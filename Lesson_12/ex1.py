def deco(c):
    raise ValueError
    return c


try:
    @deco
    def func():
        print(1)
        return 1
except ValueError:
    print("Error in decorator")


try:
    func()
except NameError:
    print("Error! 'func' is not defined")
except:
    print("Some another error")
