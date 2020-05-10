import random
from calc_mod.func_calc_mod import auto_mod     #  виклик функції автомода AUTOMOD
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
symbol_valid = list('+-1234567890.')
operation_valid = {
    '+': 'додавання',
    '-': 'віднімання',
    '*': 'множення',
    '/': 'ділення',
    '//': 'ділення націло',
    '%': 'остача від цілочисленого ділення',
    '**': 'підведення числа у степінь',
    '^^': 'найти корінь цілого числа',
    '?': 'генератор випадкових цілих чисел',
    '!': 'факторіал',
    '0': 'вийти з програми',
    'auto': 'автоматичний розрахунок на основі виразу (приклад: -1--1)',
}
operationToprint = [': '.join(prety) for prety in operation_valid.items()]
print(name_user_up, *operationToprint, sep='\n')


# функція повернення рандомного числа
def random_choice():
    lower_limit1 = input(name_user_up + ' введіть нижню межу: ')
    upper_limit1 = input(name_user_up + ' введіть верхню межу: ')
    lower_limit1 = lower_limit1.strip()
    upper_limit1 = upper_limit1.strip()
    while not lower_limit1.isdigit() or not upper_limit1.isdigit() or upper_limit1 < lower_limit1:
        print(f'{name_user_up} {lower_limit1} або {upper_limit1} не є числом.')
        lower_limit1 = input(name_user_up + ' введіть нижню межу: ')
        upper_limit1 = input(name_user_up + ' введіть верхню межу: ')
        lower_limit1 = lower_limit1.strip()
        upper_limit1 = upper_limit1.strip()
    else:
        lower_limit1 = int(lower_limit1.strip())
        upper_limit1 = int(upper_limit1.strip())
        limit_digit1 = random.randrange(lower_limit1, upper_limit1)
        return limit_digit1


# функція перевірки операції на валідність
def choice_valide(operation):
    for t in operation:
        if t not in operation_valid:
            return False
        else:
            return t


# функция перевірка на валідність числа кількість знаків після коми
def round():
    round_digit = input(name_user_up + ' введіть бажану кількість знаків після коми: ')
    while not round_digit.isdigit():
        print(round_digit + ' не є цілим числом')
        round_digit = input(name_user_up + ' введіть бажану кількість знаків після коми: ')
        round_digit = round_digit
    else:
        return round_digit


while True:
    choice_operation = input(name_user_up + ' ваш вибір операції: ')
    choice_operation = choice_operation.strip()
    choice_operation_if_not_valid = choice_operation
    choice_operation = {''.join(choice_operation)}
    choice_operation = (choice_valide(choice_operation))
    print(choice_operation)
    if choice_operation == '?':
        print(random_choice())
        continue
    elif choice_operation == '0':
        print(f'Дякуємо {name_user_up} . До наступних обчислень.')
        break
    if choice_operation == '!':
        z_factorial = input(name_user_up + ' введіть число: ')
        if z_factorial.isdigit():
            z_factorial = float(z_factorial)
            i = 1
            factorial = 1
            while i <= z_factorial:
                factorial *= i
                i = i + 1
            print(result_print, factorial)
        else:
            print(f'{name_user_up} {z_factorial} не є числом.')
    elif choice_operation == '^^':
        digit_root = input(name_user_up + ' введіть число: ')
        root = input(name_user_up + ' введіть степінь кореня: ')
        if digit_root.isdigit() and root.isdigit():
            result_root = float(digit_root) ** (1 / float(root))
            print(result_print, result_root)
        else:
            print(f'{name_user_up} {digit_root} або {root} не є числом.')
    elif choice_operation is False:
        print(f'{name_user_up} {choice_operation_if_not_valid} не підтримується.')
    elif choice_operation == 'auto':
        a = name_user_up
        auto = auto_mod(name_user_up)
    else:
        n = round()
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
        for i in digit:
            if i not in symbol_valid:                  # перевірка на валідність введених символів
                digit = False
        if digit_plus_or_minus <= 0 and digit is not False and xy_point == 0:
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
                    print(f'O o o o p s {name_user_up} ділення на ноль')
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
