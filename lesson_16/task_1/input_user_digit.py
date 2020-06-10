from lesson_16.task_1.all_digit_pow import pow_all_int as allintpow
print('Введіть число і кожну цифру цього числа буде піднесено в квадрат')
print('Введіть число:')
number_user = input('> ').strip()
while not number_user.isdigit():
    print('Ви ввели не лише ціле число. Спробуйте знову.')
    number_user = input('> ').strip()
number_user = int(number_user)
print(allintpow(number_user))
