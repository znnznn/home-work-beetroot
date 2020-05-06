a = {'1': 11, '2': 22, 3: (), 4: (), 5: ()}


def oops():
    raise IndexError


def oops_action():
    b = (input('Введіть бажаний індекс: '))
    try:
        print(a[b], 'це ваше значення.')
        oops()
    except IndexError:
        print(f'{b} це не існуючий індекс. Зловили помилку IndexError.')
    except KeyError:
        print(f' {b} це не існуючий ключ. ловили помилку KeyError.')
    finally:
        print('Спробуйте ще.')


print(oops_action())
