"""Дано масив із нуликів і одиничок.
Одинички - заповнені комірки, нулики - незаповнені.
Ви можете брати об'єкт із заповненої комірки і перекладати у незаповнену.
Задача: створити функцію, котра порахує мінімальну кількість перекладань,
потрібну для того щоб всі заповнені комірки стали у неперервний ряд"""


def replace_counter(el_list):
    """Calculate the minimum number of permutations of elements"""
    block_len = el_list.count(1)
    zero_counts = []
    i = 0
    while i <= len(el_list) - block_len:
        zero_counts.append((el_list[i: i + block_len]).count(0))
        i += 1
    return min(zero_counts)


assert replace_counter([1, 0, 0, 0, 1, 1, 0, 1]) == 1
assert replace_counter([1, 0, 0, 0, 1, 1, 0, 0, 0, 1]) == 2
assert replace_counter([1, 0, 0, 0, 1, 1, 0, 0, 0, 1]) == 2
assert replace_counter([1, 1, 1, 1, 1, 1, 0, 1]) == 1
assert replace_counter([0, 0, 0, 0, 1, 0, 1]) == 1
assert replace_counter([1, 1, 1, 1, 1, 1, 1]) == 0
assert replace_counter([1, 1, 1, 0, 1, 1, 1]) == 1
assert replace_counter([1, 1, 1, 1, 1, 1, 0]) == 0
assert replace_counter([1, 1, 1, 0, 0, 1, 1, 0]) == 2
assert replace_counter([0, 1, 1, 1, 1, 1, 1]) == 0

assert replace_counter([0, 0, 1, 1, 1, 0, 0]) == 0
assert replace_counter([1, 1, 1, 1, 1, 1, 0, 1]) == 1
assert replace_counter([1, 0, 1, 0, 1, 1, 0, 1]) == 2
assert replace_counter([1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0]) == 3
assert replace_counter([1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]) == 2