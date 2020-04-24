import random
print('Це генератор випадкових цілих чесел з функцією виводу максимального числа.')
please = 'Будь-ласка'
sorry = 'Вибачте'
limit_dn = 'Будь-ласка введіть нижню межу ціле число: '
limit_up = 'Будь-ласка введіть верхню межу ціле число: '
count = 'Будь-ласка введіть кількість випадкових цілих чисел: '
result_list = 'Згенерована послідовність випадкових чисел така: '
max_digit = 'Максимальне число з послідовності чисел таке: '
lower_limit = input(limit_dn)
upper_limit = input(limit_up)
count_limit = input(count)
lower_limit = lower_limit.strip()
upper_limit = upper_limit.strip()
while not lower_limit.isdigit() or not upper_limit.isdigit() or not count_limit.isdigit():
    print(f'{please} {lower_limit} або {upper_limit} або {count_limit} не є цілим числом.')
    lower_limit = input(limit_dn)
    upper_limit = input(limit_up)
    count_limit = input(count)
    lower_limit = lower_limit.strip()
    upper_limit = upper_limit.strip()
    count_limit = count_limit.strip()
else:
    lower_limit = int(lower_limit.strip())
    upper_limit = int(upper_limit.strip())
    count_limit = int(count_limit.strip())
    i = 0
    list_digit = []
    while i < count_limit:
        limit_digit = random.randrange(lower_limit, upper_limit + 1)
        list_digit1 = list_digit.append(limit_digit)
        i += 1
    print(result_list, list_digit)
    print(max_digit, max(list_digit))

