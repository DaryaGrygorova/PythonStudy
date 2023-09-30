"""Generators as func"""

def new_generator():
    print('first iteration')
    yield 0                     # return 0 for first iteration
    print('second iteration')
    yield 1                     # return 1 for second iteration
    print('third iteration')    # never has been print


iterator_1 = iter(new_generator())
print(next(iterator_1))        # 0
print(next(iterator_1))        # 1
print(next(iterator_1))        # Error "StopIteration"

iterator_2 = iter(new_generator()) # new generator index started from 0
print(next(iterator_2))        # 0
print(next(iterator_2))        # 1
print(next(iterator_2))        # Error "StopIteration"


def infinity_generator():
    index = 0
    while True:
        index += 1
        yield index             # generator starts from 1
