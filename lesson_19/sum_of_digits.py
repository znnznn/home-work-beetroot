from typing import Union


def sum_of_digits(digit_string: str) -> Union[int, str]:
    """" returns the sum of the digits of the number """
    try:
        if not digit_string.isdigit():
            raise ValueError
        if len(digit_string) <= 1:
            return int(digit_string)
        return sum_of_digits(digit_string[-1]) + sum_of_digits(digit_string[:-1])
    except Exception as e:
        return f'{e} type error'


print(sum_of_digits('26'))
print(sum_of_digits('5555'))
print(sum_of_digits('1111'))
print(sum_of_digits('2525'))
print(sum_of_digits(2525))
print(sum_of_digits('test'))