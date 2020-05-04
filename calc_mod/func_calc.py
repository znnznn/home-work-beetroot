def calculator(x, y, choice_operation, name_user_up):
    result_print = name_user_up + ' ваш результат:'
    from .calculator_plus_mod import round
    n = round()
    if choice_operation == '^^':
        digit_root = x
        root = y
        if digit_root.isdigit() and root.isdigit():
            result = float(digit_root) ** (1 / float(root))
            print(f'{name_user_up}, {result}')
        else:
            print(f'{name_user_up} {digit_root} або {root} не є числом.')
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
