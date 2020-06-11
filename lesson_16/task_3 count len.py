import sys


def count_lines(name):
    try:
        openFile = open(name)
        my_count_lines = len(openFile.read().splitlines())
        return my_count_lines
    except FileNotFoundError as e:
        print(e)


def count_chars(name):
    try:
        openFile = open(name)
        my_count_lines = openFile.read().splitlines()
        my_count = len(''.join(my_count_lines))
        return my_count
    except FileNotFoundError as e:
        print(e)


def test(name):
    return count_lines(name), count_chars(name)


try:
    if len(sys.argv) < 2:
        filename = 'input.txt'
    else:
        filename = sys.argv[1]
    print(f'Ви починаєте працювати з {filename} базою даних.')
except FileNotFoundError:
    filename = 'input.txt'
except Exception as e:
    print(f'Ви створили {e} критичну помилку. Перезапустіть програму.')
    exit()


print(count_lines(filename))
print(count_chars(filename))
print(test(filename))
