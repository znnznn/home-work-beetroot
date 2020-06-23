from typing import Union


def my_palindrom(word_string: str) -> Union[bool, str]:
    """" check the string on the palindrome """
    try:
        if type(word_string) != str:
            raise TypeError
        if len(word_string) <= 1:
            return True
        elif word_string[0] == word_string[-1]:
            return my_palindrom(word_string[1:-1])
        return False
    except TypeError as e:
        return f'{e}type error'


print(my_palindrom('mom'), 'mom')
print(my_palindrom('sassas'), 'sassas')
print(my_palindrom('o'), 'o')
print(my_palindrom('2002'), '2002')
print(my_palindrom('Natochka'), 'Natochka')
print(my_palindrom('2020'), '2020')
print(my_palindrom(2002), 2002)
print(my_palindrom([1512]), [[1512]])