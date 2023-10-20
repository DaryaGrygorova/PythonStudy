# fibonacci sequence: 0, 1, 1, 2, 3, 5...

def fibonacci(index):
    a, b = 0, 1
    for _ in range(index):
        a, b = b, a + b
    return a

def fibonacci2(index):
    if index <= 1:
        return index
    while index >= 2:
        return fibonacci2(index - 1) + fibonacci2(index - 2)


# print(fibonacci(5))

assert fibonacci(3) == 2
assert fibonacci(5) == 5
assert fibonacci(7) == 13

assert fibonacci2(1) == 1
assert fibonacci2(3) == 2
assert fibonacci2(5) == 5
assert fibonacci2(7) == 13
