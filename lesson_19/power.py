from typing import Union


def power(digit: Union[int, float], digit_pow: Union[int, float]) -> Union[int, float, str]:
    """" returns a number to a given power """
    try:
        if digit_pow < 0:
            raise ValueError
        if digit_pow == 0:
            return 1
        return digit * power(digit, digit_pow-1)
    except Exception as e:
        return f'{e}This function works only with exp > 0.'


def power_check_result(digit: Union[int, float],
                       digit_pow: Union[int, float],
                       expected_result: Union[int, float]) -> bool:
    """ checking whether the number is false / true """
    result = digit * power(digit, digit_pow-1)
    if result == expected_result:
        return True
    return False



a, b = 2, 4
print(power(a,b))

a, b, c = 2, 4, 16
print(power_check_result(a,b,c))
