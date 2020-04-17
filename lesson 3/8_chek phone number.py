phone_number = input()
if phone_number.isdigit() and len(phone_number) == 10:
    print('Ваш номер відповідає формату')
else:
    print('Введіть номер телефону наприклад 0671234567')
