try:
    a = input('Введіть ціле число: ')
    b = input('Введіть ціле число: ')
    a = int(a)
    b = int(b)
    print(a ** 2 / b)
except ValueError as e:
    print(f'{e} не є цілим числом')
except ZeroDivisionError:
    print(f'O o o o p s ділення на ноль')
finally:
    print('Маєте бажання. Спробуйте ще.')
