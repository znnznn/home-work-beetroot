def round(name_user_up):
    round_digit = input(name_user_up + ' введіть бажану кількість знаків після коми: ')
    while not round_digit.isdigit():
        print(round_digit + ' не є цілим числом')
        round_digit = input(name_user_up + ' введіть бажану кількість знаків після коми: ')
        round_digit = round_digit
    else:
        return round_digit


def calculator(x, y, choice_operation, name_user_up):
    result_print = name_user_up + ' ваш результат:'
    n = round(name_user_up)
    if choice_operation == '^^':
        digit_root = x
        root = y
        result = float(digit_root) ** (1 / float(root))
        print(f'{name_user_up}, {result}')
    if choice_operation == '+':
        print(f'{result_print} {x} + {y} = {(float ( x ) + float ( y )):.{n}f}')
    elif choice_operation == '-':
        print(f'{result_print} {x} - {y} = {(float ( x ) - float ( y )):.{n}f}')
    elif choice_operation == '/':
        if y == 0:
            print(f'O o o o p s {name_user_up} ділення на ноль')
        else:
            print(f'{result_print} {x} / {y} = {(float ( x ) / float ( y )):.{n}f}')
    elif choice_operation == '//':
        if y == 0:
            print(f'O o o o p s {name_user_up} ділення на ноль')
        else:
            print(f'{result_print} {x} // {y} = {float ( x ) // float ( y )}')
    elif choice_operation == '%':
        print(f'{result_print} {x} % {y} = {float ( x ) % float ( y )}')
    elif choice_operation == '*':
        print(f'{result_print} {x} * {y} = {(float ( x ) * float ( y )):.{n}f}')
    elif choice_operation == '**':
        print(f'{result_print} {x} ** {y} = {(float ( x ) ** float ( y )):.{n}f}')
    return
