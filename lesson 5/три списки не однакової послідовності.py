import random
print('''Це генератор двох списків випадкових цілих чесел, і третього
списку з чисел які є в першій послідовності але немає в другій''')
please = 'Будь ласка'
sorry = 'Вибачте'
limit_dn = f'{please} введіть нижню межу ціле число: '
limit_up = f'{please} введіть верхню межу ціле число: '
count = f'{please} введіть кількість випадкових цілих чисел: '
result_list = 'Згенерована послідовність випадкових чисел така: '
result_list_without_duplicates = 'Числа які є лише в першій полсідовності'
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
    list_digit1 = []
    while i < count_limit:
        limit_digit1 = random.randint(lower_limit, upper_limit)
        limit_digit2 = random.randint(lower_limit, upper_limit)
        list_digit.append(limit_digit1)
        list_digit1.append(limit_digit2)
        i += 1
    print(result_list, list_digit)
    print(result_list, list_digit1)
i = 0
list_new1 = []
list_new2 = []

for list_new in list_digit:
    if list_new not in list_new2:
        list_new2.append(list_new)
print(result_list_without_duplicates, list_new2, ' iterator for')

while i < len(list_digit):
    if list_digit[i] not in (list_digit1 and list_new1) and i < len(list_digit):
        list_new1.append(list_digit[i])
    i += 1
print(result_list_without_duplicates, list_new1, ' через while')
