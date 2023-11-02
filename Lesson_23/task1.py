"""
Task 1 - Big O
We assume that all lists passed to functions are the same length N
Match big O complexities with the code snippets below

Answers:
1 - n       - question1
2 - 1       - question2
3 - n^2     - question3
4 - n       - question4
5 - n^2     - question5
6 - log n   - question6
"""

from typing import List, Tuple


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    """O(1+n(a+1))
    'a' is some constant, a counter of operations necessary
    to check whether el_first_list is in the second_list
    -> O(n)"""
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


def question2(n: int) -> int:
    """O(10*(1)) -> O(1)"""
    for _ in range(10):
        n **= 3
    return n


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    """O(n+n*(1+n((1+3)+(1+1)) -> O(n^2)"""
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(*second_list)
    return temp


def question4(input_list: List[int]) -> int:
    """O(1+n(1+1)) -> O(n)"""
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]:
    """O(1+n*(n*(1))) -> O(n^2)"""
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


def question6(n: int) -> int:
    """Count of operation (x) for n from 0 to 16:
    n = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
    x = 1, 2, 2, 3, 3, 3, 3, 4, 4,  4,  4,  4,  4,  4,  4,  4
    x(n*2) = x(n)+1
    -> O(log n)"""
    count = 0
    while n > 1:
        n /= 2
        count += 1
    print("count:", count)
    return n
