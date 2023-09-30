"""Generators as func, method send"""

def infinity_generator():
    sent = None
    index = 0
    while True:
        index += 1
        print(index, '-', sent)
        sent = yield index


iterator_1 = iter(infinity_generator())
print(next(iterator_1))
print(next(iterator_1))

print(iterator_1.send("test"))
# call new iteration and save arg 'test' as some variable that is local in this iteration

print(next(iterator_1))
