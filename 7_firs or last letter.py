x = input('Введіть данні: ')
x_len = len(x)
if x_len >= 2:
    x_print = x[0] + x[1] + x[-2] + x[-1]
    print(x_print)
else:
    print()

