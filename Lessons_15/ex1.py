some_variable = 200

def some_func():
    a = 10
    some_variable = 5         #створиться локальна змінна з заданим значенням
    global some_variable      #перезаписує глобальну змінну
    some_variable = 5

    return a

some_func()

# Errors
# print(some_func().a)
# print(a)

print(some_func.__code__.co_nlocals)


