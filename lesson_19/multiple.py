from typing import Union


def my_mult(a: int, n: int) -> Union[int, str]:
    """" This function works only with positive integers """
    try:
        if a < 0 or n < 0:
            raise ValueError
        if n == 0:
            return 0
        return a + my_mult(a, n-1)
    except TypeError as e:
        return f'{e} type error'
    except Exception as e:
        return f'{e}This function works only with positive integers'


print(my_mult(2, 16))
print(my_mult(2, 0))
print(my_mult(2, -4))
print(my_mult(['2'], 16))
