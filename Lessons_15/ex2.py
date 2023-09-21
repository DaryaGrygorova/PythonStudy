some_variable = 200

def some_func(a):
    some_init = 1000
    some_int = 100

    def inner_func():
        inner_local_var = 550      # nonlocals область видимості блоку-обгортки
        print(some_init)           # доступна для читання з рядка 4, але не для перезапису

        nonlocal some_int           # перезаписуємо some_int з області видимості some_func
        some_int = 10
        print(some_variable)
    inner_func()
    return a

some_func(100)

