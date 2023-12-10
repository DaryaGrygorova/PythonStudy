"""Task 1
A bubble sort can be modified to "bubble" in both directions.
The first pass moves "up" the list and the second pass moves "down".
This alternating pattern continues until no more passes are necessary.
Implement this variation and describe under what circumstances it might
be appropriate.
"""


def bubble_both_directions_sort(array):
    """
    The first pass moves "up" the list and the second pass moves "down".
    """
    left_index = 0
    right_index = len(array) - 1

    while left_index < right_index:
        # move the biggest element to the right
        for i in range(left_index, right_index):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right_index -= 1

        # move the smallest element to the left
        for i in range(right_index, left_index, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left_index += 1
    return array


assert bubble_both_directions_sort([7, 42, 8, 5, 6, 19, 55, 1, -1]) == [
    -1,
    1,
    5,
    6,
    7,
    8,
    19,
    42,
    55,
]
assert bubble_both_directions_sort([82, -66, 64, 91, -51, 13, 42, -29, 20, -29]) == [
    -66,
    -51,
    -29,
    -29,
    13,
    20,
    42,
    64,
    82,
    91,
]
assert bubble_both_directions_sort([-81, 68, 50, -95, -56, -29, -56, 91, -7, -46]) == [
    -95,
    -81,
    -56,
    -56,
    -46,
    -29,
    -7,
    50,
    68,
    91,
]
