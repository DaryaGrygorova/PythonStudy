"""Iters"""

test_list = [1, 2, 3]

for item in test_list:
    print(item)

#This for-loop is identical next code

iterator_1 = iter(test_list)
iterator_2 = iter(test_list)
print(next(iterator_1))     #1
print(next(iterator_1))     #2
print(next(iterator_1))     #3

print('we reached the end')
print(next(iterator_1))     #Error
print(next(iterator_2))     #1 another iter has own position