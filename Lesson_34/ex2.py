"""Multiprocessing"""
import multiprocessing
import time
from multiprocessing import Process, freeze_support

start = time.time()
PROCESSES = []
intermediate_res = multiprocessing.Array(int, 256)


def fibonacci(f_index, intermediate=False):
    if index in intermediate_res:
        print('worked!')
        return intermediate_res.get(index)
    if f_index <= 1:
        return f_index
    while f_index >= 2:
        result = fibonacci(f_index - 1) + fibonacci(f_index - 2)
        if index == 25 and intermediate:
            intermediate_res.set(index, result)
        return result


for index in range(3):
    PROCESSES.append(Process(target=fibonacci, name=f'process_{str(index).zfill(1)}'))


if __name__ == '__main__':
    freeze_support()
    fibonacci_intermediate = Process(target=fibonacci, args=(25, True))
    fibonacci_final = Process(target=fibonacci, args=(30, ))

    for fib in (fibonacci_intermediate, fibonacci_final):
        fib.start()
    for fib in (fibonacci_intermediate, fibonacci_final):
        fib.join()

    print(time.time() - start)
