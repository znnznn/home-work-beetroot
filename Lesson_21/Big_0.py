from typing import Union, List, Tuple, Optional

# We assume that all lists passed to functions are same length N

# answers
# 1 - n
# 2 - 1
# 3 - n^2
# 4 - n
# 5 - n^2
# 6 - log n


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    """" Returns a list of items that are in two lists """
    res: List[int] = []
    my_count = 0
    for el_first_list in first_list:
        my_count += 1
        if el_first_list in second_list:
            my_count += 1
            res.append(el_first_list)
    print(my_count)
    return res


def question2(n: int) -> int:
    """" Returns a number in power 59049"""
    my_count = 0
    for i in range(10):
        my_count += 1
        n **= 3
    print(my_count)
    return n


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    """" returns a list of non-identical items """
    temp: List[int] = first_list[:]
    my_count = 0
    for el_second_list in second_list:
        my_count += 1
        flag = False
        for check in temp:
            my_count += 1
            if el_second_list == check:
                my_count += 1
                flag = True
                break
        if not flag:
            my_count += 1
            temp.append(el_second_list)
    print(my_count)
    return temp


def question4(input_list: List[int]) -> int:
    """" returns the maximum number of the list """
    res: int = 0
    my_count = 0
    for el in input_list:
        my_count += 1
        if el > res:
            my_count += 1
            res = el
    print(my_count)
    return res


def question5(n: int) -> List[Tuple[int, int]]:
    """ returns a tuple of n for each number n times """
    res: List[Tuple[int, int]] = []
    my_count = 0
    for i in range(n):
        my_count += 1
        for j in range(n):
            my_count += 1
            res.append((i, j))
    print(my_count)
    return res


def question6(n: int) -> int:
    """ returns a number less than one from n / 2 """
    my_count = 0
    while n > 1:
        my_count += 1
        n /= 2
    print(my_count)
    return n


one_list = list(range(0, 10))
two_list = [1, 25, 45, 3, 6, 2, 10]
print(question1(one_list, two_list))
#  print(question2(2))
print(question3(one_list, two_list))
print(question4(two_list))
print(question5(5))
print(question6(20))
