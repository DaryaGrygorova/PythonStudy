"""Task 1 - Primes

We have the following input list of numbers, some of them are prime.
You need to create a utility function that takes as input a number
and returns a bool, whether it is prime or not.

Use ThreadPoolExecutor and ProcessPoolExecutor to create different
concurrent implementations for filtering NUMBERS.

Compare the results and performance of each of them.
"""
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime+
]


def is_prime(num):
    """Returns a bool, whether num is prime or not
    (based on the trial division method).
    """
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False

    for i in range(3, round(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def print_execution_time_decorator(func):
    """Prints the execution time of a function"""
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time {func.__name__} --> {round((end - start), 3)}")
        return res

    return wrapper


@print_execution_time_decorator
def is_prime_multiprocessing():
    """Runs the is_prime function for all num from NUMBERS,
    using multiprocessing"""
    with ProcessPoolExecutor() as executor1:
        executor1.map(is_prime, NUMBERS)


@print_execution_time_decorator
def is_prime_multithreading():
    """Runs the is_prime function for all num from NUMBERS,
    using multithreading"""
    with ThreadPoolExecutor() as executor2:
        executor2.map(is_prime, NUMBERS)


if __name__ == "__main__":
    is_prime_multiprocessing()
    is_prime_multithreading()
    # assert is_prime(2) is True
    # assert is_prime(1099726899285419) is False
    # assert is_prime(1570341764013157) is True
    # assert is_prime(1637027521802551) is True
    # assert is_prime(1880450821379411) is True
    # assert is_prime(1893530391196711) is True
    # assert is_prime(2447109360961063) is True
    # assert is_prime(3) is True
    # assert is_prime(2772290760589219) is True
    # assert is_prime(3033700317376073) is True
    # assert is_prime(4350190374376723) is False
    # assert is_prime(4350190491008389) is True
    # assert is_prime(4350190491008390) is False
    # assert is_prime(4350222956688319) is False
    # assert is_prime(2447120421950803) is False
    # assert is_prime(5) is True
