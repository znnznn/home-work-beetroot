name_user = input('Введіть своє ім\'я: ')
name_user_strip = name_user.strip()
while not name_user_strip.isalpha():
    name_user = input('Введіть своє ім\'я: ')
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
! факторіал
0 вийти з програми""")
while True:
    choice_operation = input(name_user_up + ' ваш вибір операції: ')
    round_digit = input(name_user_up + ' введіть бажану кількість знаків після коми: ')
    while round_digit.islower() or round_digit.islower():
        round_digit = input(name_user_up + ' введіть бажану кількість знаків після коми: ')
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
    elif choice_operation in ('+', '-', '*', '/', '//', '%', '**', '0'):
        if choice_operation == '0':
            print(f'Дякуємо {name_user_up} . До наступних обчислень.')
            break
        x = input(first_digit)
        y = input(second_digit)
        digit = x + y
        if not digit.islower() or not digit.islower():
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
