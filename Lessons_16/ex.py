"""Дано масив із нуликів і одиничок.
Одинички - заповнені комірки, нулики - незаповнені.
Ви можете брати об'єкт із заповненої комірки і перекладати у незаповнену.
Задача: створити функцію, котра порахує мінімальну кількість перекладань,
потрібну для того щоб всі заповнені комірки стали у неперервний ряд"""


def replace_counter(el_list):
    """Calculate the minimum number of permutations of elements"""
    counter = 0
    i = 0
    k = len(el_list) - 1
    last_ind = len(el_list) - 1
    # print(list)
    if not el_list.count(0) == 0:
        while i < len(el_list) - 1:
            if el_list[i] == 0:
                for j in range(k, 0, -1):
                    if not el_list[j] == 0:
                        counter += 1
                        last_ind = j - 1
                        # print(f'replace element {j} on position {i}')
                        break

            k = last_ind
            i += 1

    return counter


# print(f'Result: {replace_counter([1, 0, 0, 0, 1, 1, 0, 1])} replaces\n')
# print(f'Result: {replace_counter([1, 1, 1, 1, 1, 1, 0, 1])} replaces\n')
# print(f'Result: {replace_counter([0, 0, 0, 0, 1, 0, 1])} replaces\n')
# print(f'Result: {replace_counter([1, 1, 1, 1, 1, 1, 1])} replaces\n')
# print(f'Result: {replace_counter([1, 1, 1, 0, 1, 1, 1])} replaces\n')


assert replace_counter([1, 0, 0, 0, 1, 1, 0, 1]) == 3
assert replace_counter([1, 1, 1, 1, 1, 1, 0, 1]) == 1
assert replace_counter([0, 0, 0, 0, 1, 0, 1]) == 2
assert replace_counter([1, 1, 1, 1, 1, 1, 1]) == 0
assert replace_counter([1, 1, 1, 0, 1, 1, 1]) == 1
assert replace_counter([1, 1, 1, 1, 1, 1, 0]) == 0
assert replace_counter([1, 1, 1, 0, 0, 1, 1, 0]) == 2
assert replace_counter([0, 1, 1, 1, 1, 1, 1]) == 1
assert replace_counter([1, 1, 1, 1, 1, 1, 0, 1]) == 1
