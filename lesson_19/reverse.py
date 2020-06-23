
def my_reverse(word_string: str) -> str:
    """" Function returns reversed input string """
    try:
        if type(word_string) != str:
            raise TypeError
        if len(word_string) == 0:
            return word_string
        return f'{word_string[-1]}{my_reverse(word_string[:-1])}'
    except Exception as e:
        return f'{e}type error'


print(my_reverse('Hello'))
print(my_reverse('H'))
print(my_reverse(['H']))