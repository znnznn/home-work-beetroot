import random
name_user = input('Введіть своє ім\'я: ')
name_user_strip = name_user.strip()
while not name_user_strip.isalpha():
    print(name_user_strip + ' містить не лише букви')
    name_user = input('Введіть своє ім\'я: ')
    name_user_strip = name_user.strip()
else:
    name_user_strip = name_user_strip.capitalize()
name_user_up = name_user_strip
first_digit = name_user_up + ' введіть перше число: '
second_digit = name_user_up + ' введіть друге число: '
result_print = name_user_up + ' ваш результат:'
print(name_user_up + """ будь-ласка оберіть операцію, натиснувши відповідний символ: 
+ додавання 
- віднімання
* множення
/ ділення
// ділення націло
% остача від цілочисленого ділення 
** підведення числа у степінь
^^ знайти корінь цілого числа
? генератор випадкових цілих чисел
! факторіал
0 вийти з програми""")
while True:
    choice_operation = input(name_user_up + ' ваш вибір операції: ')
    choice_operation = choice_operation.strip()
    if choice_operation == '?':
        lower_limit = input(name_user_up + ' введіть нижню межу: ')
        upper_limit = input(name_user_up + ' введіть верхню межу: ')
        lower_limit = lower_limit.strip()
        upper_limit = upper_limit.strip()
        while not (lower_limit.isdigit() or upper_limit.isdigit()):
            print(f'{name_user_up} {lower_limit} або {upper_limit} не є числом.')
            lower_limit = input(name_user_up + ' введіть нижню межу: ')
            upper_limit = input(name_user_up + ' введіть верхню межу: ')
            lower_limit = lower_limit.strip()
            upper_limit = upper_limit.strip()
        else:
            lower_limit = int(lower_limit.strip())
            upper_limit = int(upper_limit.strip())
            limit_digit = random.randrange(lower_limit, upper_limit)
            print (limit_digit)
    elif choice_operation == '0':
        print(f'Дякуємо {name_user_up} . До наступних обчислень.')
        break
    round_digit = input(name_user_up + ' введіть бажану кількість знаків після коми: ')
    while not round_digit.isdigit():
        print(round_digit + ' не є цілим числом')
        round_digit = input(name_user_up + ' введіть бажану кількість знаків після коми: ')
        round_digit = round_digit
    else:
        n = round_digit
    if choice_operation == '!':
        z = input(name_user_up + ' введіть число: ')
        if z.isdigit():
            z = float(z)
            i = 1
            factorial = 1
            while i <= z:
                factorial *= i
                i = i + 1
            print(result_print, factorial)
        else:
            print(f'{name_user_up} {z} не є числом.')
    elif choice_operation == '^^':
        digit_root = input(name_user_up + ' введіть число: ')
        root = input(name_user_up + ' введіть степінь кореня: ')
        if digit_root.isdigit() and root.isdigit():
            result_root = float(digit_root) ** (1 / float(root))
            print(result_print, result_root)
        else:
            print(f'{name_user_up} {digit_root} або {root} не є числом.')
    elif choice_operation in ('+', '-', '*', '/', '//', '%', '**'):
        x = input(first_digit)
        y = input(second_digit)
        x = x.strip()
        y = y.strip()
        x_find_plus = x.rfind('+')
        x_find_minus = x.rfind('-')
        y_find_plus = y.rfind('+')
        y_find_minus = y.rfind('-')
        xy_point = (x.find('.') - x.rfind('.')) + (y.find('.') - y.rfind('.'))
        digit_plus_or_minus = max([x_find_plus, x_find_minus, y_find_plus, y_find_minus])
        digit = x + y
        x_symbol = x.find('/')
        x_symbol1 = x.find('*')
        x_symbol2 = x.find(',')
        y_symbol = y.find('/')
        y_symbol1 = y.find('*')
        y_symbol2 = y.find(',')
        digit_find_symbol = max([x_symbol, x_symbol1, x_symbol2, y_symbol, y_symbol1, y_symbol2])
        if digit_plus_or_minus <= 0 >= digit_find_symbol and not (digit.islower() or digit.isupper()) and xy_point == 0:
            if choice_operation == '+':
                print(f'{result_print} {x} + {y} = {(float(x) + float(y)):.{n}f}')
            elif choice_operation == '-':
                print(f'{result_print} {x} - {y} = {(float(x) - float(y)):.{n}f}')
            elif choice_operation == '/':
                if y == '0':
                    print(f'{name_user_up} ділення на ноль')
                else:
                    print(f'{result_print} {x} / {y} = {(float(x) / float(y)):.{n}f}')
            elif choice_operation == '//':
                if y == '0':
                    print(f'{name_user_up} ділення на ноль')
                else:
                    print(f'{result_print} {x} // {y} = {float(x) // float(y)}')
            elif choice_operation == '%':
                print(f'{result_print} {x} % {y} = {float(x) % float(y)}')
            elif choice_operation == '*':
                print(f'{result_print} {x} * {y} = {(float(x) * float(y)):.{n}f}')
            elif choice_operation == '**':
                print(f'{result_print} {x} ** {y} = {(float(x) ** float(y)):.{n}f}')
        else:
            print(f'{name_user_up} {x} або {y} не є числом.')
    else:
        print(f'{name_user_up} {choice_operation} не підтримується.')
