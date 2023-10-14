"""
Дано масив із нуликів і одиничок. Одинички - заповнені комірки, нулики - незаповнені.
Ви можете брати об'єкт із заповненої комірки і перекладати у незаповнену.
Задача: створити функцію, котра порахує мінімальну кількість перекладань,
потрібну для того щоб всі заповнені комірки стали у неперервний ряд
"""


def count_min_replacements(iterable: list[int]) -> int:
    """Count minimal replacements"""
    if not iterable:
        return 0

    iterable_length = len(iterable)
    range_len = iterable.count(1)
    min_count = range_len
    for start in range(iterable_length - range_len + 1):
        zero_count = iterable[start:(start + range_len)].count(0)
        min_count = min(min_count, zero_count)
    return min_count
