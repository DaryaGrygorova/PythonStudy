"""Task 1 - Implement a fibonacci search for element in list"""
import time


def fibonacci_search_simple(value, sorted_list):
    """Returns True if value contains in the list"""
    list_len = len(sorted_list)

    if list_len == 0 or list_len == 1 and value != sorted_list[0]:
        return False

    mid_index = get_prev_fibonacci_num(list_len)

    if value == sorted_list[mid_index]:
        return True

    if value < sorted_list[mid_index] and mid_index > 0:
        return fibonacci_search_simple(value, sorted_list[0:mid_index])

    if value > sorted_list[mid_index]:
        return fibonacci_search_simple(value, sorted_list[mid_index:])

    return False


def get_prev_fibonacci_num(num):
    """Returns number from Fibonacci sequence that is less than num"""
    current_el, next_el = 0, 1
    prev_el = 0

    for _ in range(num):
        if current_el <= num < next_el:
            return prev_el
        prev_el, current_el, next_el = current_el, next_el, current_el + next_el

    return prev_el


def fibonacci_search_optimal(value, sorted_list):
    """Returns True if value contains in the list"""
    list_len = len(sorted_list)

    if not list_len:
        return False

    if list_len == 1:
        return value == sorted_list[0]

    sequence = get_fibonacci_sequence(list_len)
    index_sequence = -2

    def recursive_search(start_index, next_index):
        nonlocal index_sequence
        index_sequence -= 1
        if value == sorted_list[start_index]:
            return True

        if start_index >= 0 and next_index >= 1:

            if value < sorted_list[start_index]:
                return recursive_search(start_index - next_index, sequence[index_sequence - 1])

            if value > sorted_list[start_index]:
                return recursive_search(start_index + next_index, sequence[index_sequence - 1])

        return False

    return recursive_search(sequence[index_sequence], sequence[index_sequence - 1])


def get_fibonacci_sequence(num):
    """Returns Fibonacci sequence ending with a number less than num"""
    if num <= 0:
        return []

    current_el, next_el = 0, 1
    sequence = [0]
    while not current_el <= num <= next_el:
        current_el, next_el = next_el, current_el + next_el
        sequence.append(current_el)

    return sequence


assert get_prev_fibonacci_num(13) == 8
assert get_prev_fibonacci_num(19) == 8
assert get_prev_fibonacci_num(22) == 13

assert get_fibonacci_sequence(13) == [0, 1, 1, 2, 3, 5, 8]
assert get_fibonacci_sequence(19) == [0, 1, 1, 2, 3, 5, 8, 13]
assert get_fibonacci_sequence(22) == [0, 1, 1, 2, 3, 5, 8, 13, 21]

assert fibonacci_search_simple(1, []) is False

assert fibonacci_search_simple(1, [1]) is True
assert fibonacci_search_simple(1, [6]) is False

assert fibonacci_search_simple(5, [1, 6]) is False
assert fibonacci_search_simple(6, [1, 6]) is True

assert fibonacci_search_simple(5, [1, 6, 8, 10, 14, 66]) is False
assert fibonacci_search_simple(5, [1, 6, 8, 10, 14, 66, 85]) is False

assert fibonacci_search_simple(8, [1, 6, 8, 10, 14, 66]) is True
assert fibonacci_search_simple(8, [1, 6, 8, 10, 14, 66, 85]) is True

assert fibonacci_search_simple(1, [1, 6, 8, 10, 14, 66]) is True
assert fibonacci_search_simple(85, [1, 6, 8, 10, 14, 66, 85]) is True

assert fibonacci_search_simple(7, [-19, -15, -8, -6, -4, -2, 0, 5, 7, 9, 11, 15, 18, 21]) is True
assert fibonacci_search_simple(8, [-19, -15, -8, -6, -4, -2, 0, 5, 7, 9, 11, 15, 18, 21]) is False

assert fibonacci_search_optimal(1, []) is False

assert fibonacci_search_optimal(1, [1]) is True
assert fibonacci_search_optimal(1, [6]) is False

assert fibonacci_search_optimal(5, [1, 6]) is False
assert fibonacci_search_optimal(6, [1, 6]) is True

assert fibonacci_search_optimal(5, [1, 6, 8, 10, 14, 66]) is False
assert fibonacci_search_optimal(5, [1, 6, 8, 10, 14, 66, 85]) is False

assert fibonacci_search_optimal(8, [1, 6, 8, 10, 14, 66]) is True
assert fibonacci_search_optimal(8, [1, 6, 8, 10, 14, 66, 85]) is True

assert fibonacci_search_optimal(1, [1, 6, 8, 10, 14, 66]) is True
assert fibonacci_search_optimal(85, [1, 6, 8, 10, 14, 66, 85]) is True

assert fibonacci_search_optimal(7, [-19, -15, -8, -6, -4, -2, 0, 5, 7, 9, 11, 15, 18, 21]) is True
assert fibonacci_search_optimal(8, [-19, -15, -8, -6, -4, -2, 0, 5, 7, 9, 11, 15, 18, 21]) is False

start_1 = time.time()
fibonacci_search_simple(55252, list(range(1000000)))
operation_time_1 = time.time() - start_1

start_2 = time.time()
fibonacci_search_optimal(55252, list(range(1000000)))
operation_time_2 = time.time() - start_2

print(
    'For searching 55252 in range(1_000_000)\n'
    'fibonacci_search_optimal is faster then fibonacci_search_simple by\n',
    (operation_time_1 - operation_time_2),
    's',
    sep=''
)
