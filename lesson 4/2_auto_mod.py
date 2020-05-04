import math


# перевірка на валідність введених символів
def check_valid_digit(str_digit):
    symbol_valid = '*+-1234567890./^^'
    symbol_valid_place = str_digit.find('/') * str_digit.find('*') * str_digit.find('^')
    for item in str_digit:
        if item not in symbol_valid or symbol_valid_place == 0:
            return False
        return True


def auto_mod(name_user_up):
    while True:
        print(f'{name_user_up} Для завершення обчислень натисніть 0 :')
        valid_mult = '*/^'
        valid_plus = '-+'
        valid_all = ['*', '+', '-', '/', '^^']
        string_expression = input(f'{name_user_up} Введіть вираз :')
        y_string = string_expression.replace(' ', '')
        a = y_string.replace(',', '.')
        w1 = a.strip('+')
        w2 = w1.strip('^^')
        w = w2.rstrip('-')
        print(w)
        n = False
        count = 0
        u = 0
        string_valid = check_valid_digit(w)
        if w == '0':
            print(f'{name_user_up} Ви вийшли з автомода.')
            break
        elif string_valid is False:
            print(f'{name_user_up} Ви ввели вираз який не підтримується :')
            continue
        else:
            for i in w:
                if i in valid_mult and u == 0:   # {'*', '**', '/', '//', '^^'} щоб не було плюса
                        n = w.rpartition(i)
                        u += 1
                        print(n)
                if i in valid_plus and u == 0 and 0 != w.find('-'):   # {'+', '-'} окремо бо плюс крутіший
                        n = w.partition(i)
                        u += 1
                if i in valid_plus and u == 0:
                        n = w.rpartition(i)
                if i in valid_all:
                    count = w.count(i)
                    print(count)
            if n is not False:              # треба щоб відкидало якщо немає другого числа
                one_digit = n[0]
                two_digit = n[-1]
                operation = n[1]
                print(one_digit, two_digit, operation)
                # l = eval(w) випадково прочитав таку функцію крутяцьку
                if count <= 3 and ('-' == one_digit[-1] or one_digit[-1] == '+'):
                    one_digit_new = one_digit[:-1]
                    two_digit_new = one_digit[-1] + two_digit
                    operation_new = operation
                elif count < 3 and operation[-1] == '^':
                    one_digit_new = one_digit.strip('^')
                    two_digit_new = two_digit.strip('^')
                    operation_new = operation * 2
                elif count < 3 and ('*' == two_digit[0] or two_digit[0] == '/'):
                    one_digit_new1 = one_digit.strip('/')
                    one_digit_new = one_digit.strip('*')
                    two_digit_new = two_digit.strip(two_digit[0])
                    operation_new = operation * 2
                elif count < 3 and ('*' == one_digit[-1] or one_digit[-1] == '/'):
                    one_digit_new = one_digit.strip(one_digit[-1])
                    two_digit_new1 = two_digit.strip('/')
                    two_digit_new = two_digit.strip('*')
                    operation_new = operation * 2
                elif count < 3:
                    one_digit_new = one_digit
                    two_digit_new = two_digit
                    operation_new = operation
                else:
                    print(f'{name_user_up} Ви ввели незрозумілий вираз :')
                    continue
                x, y, choice_operation = float(one_digit_new), float(two_digit_new), operation_new
                print(x, y, choice_operation)
                from .2_функция import calculator
                print(calculator(x, y, choice_operation, name_user_up))
            else:
                print(f'{name_user_up} Ви ввели надто мало даних :')
