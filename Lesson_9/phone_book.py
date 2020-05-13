import json

import sys

try:
    if len(sys.argv) < 2:
        print('Введіть базу данних з якою Ви бажаєте працювати')
        sys_argv1 = input('> ')
        filename = sys_argv1
    else:
        filename = sys.argv[1]
    json_file = open(filename)
    print(f'Ви починаєте працювати з {filename} базою даних.')
except FileNotFoundError:
    print(f'{sys_argv1} базу даних не знайдено.')
    filename = 'phone_book.json'
    print(f'Створити порожню базу данних {filename}? Якщо так натисніть 1.')
    empty_file_user = input('> ')
    if empty_file_user == '1':
        json_file = open(filename, 'w')
    else:
        print('До побачення.')
        exit()
except Exception:
    print('До побачення.')


try:
    my_phone_book = json.load(json_file)
    empty_list = True
except Exception:
    empty_list = False
    my_phone_book = []
json_file.close()


#my_phone_book = open('phone_book.json', 'w+')


'''with open('phone_book.json', 'w') as phone_book:
    json.dump(contacts, phone_book, indent=4)'''




def list(my_phone_book):
        for i in json.load(my_phone_book):
            print(i, sep='\n')


def choice_find(x, y):
    for t in x:
        if t not in y:
            return None
        else:
            return t


def find(my_phone_book, criterion):
    find_value = input("> ")
    work_my_phone_book = my_phone_book.copy()
    row = []
    item = 0
    for value in work_my_phone_book:
        if find_value == value[criterion]:
            row.append(value)
            item += 1
        else:
            continue
        if item == 0:
            return print(f'Данні по {criterion} {find_value} відсутні.')
    return print(f"Данні по {criterion} {find_value}: знайдено {len(row)}'\n' {row}', '\n'"), row




def delete(my_phone_book):
    print("Введіть контакт: ")
    name = input('> ').strip().capitalize()
    for value in json.load(my_phone_book):
        if value == name:
            print(f"Ви дійсно бажаєте видалити контект (yes/no)?: {name}")
            name_del = input('> ').strip()
            if name_del == 'yes':
                my_phone_book.remove(value)
                print(f"Ви видалили контакт {name}")


def add():
    print("Введіть ім\'я контакту")
    name = input("> ").strip()
    print("Введіть призвіще контакту")
    last_name = input("> ").strip()
    print("Введіть номер телефону")
    phone = input("> ").strip()
    while not phone.isdigit():
        print(f'{phone} містить не лише цифри')
        print("Введіть знову номер телефону")
        phone = input("> ").strip()
    print("Введіть місто проживання")
    city_live = input("> ").strip()
    valid_simbol = name + last_name + city_live
    while not valid_simbol.isalpha() or not phone.isdigit():
        if not valid_simbol.isalpha() and phone.isdigit():
            print(f'{name} або {last_name} або {city_live} містять не лише букви. Введіть лише букви')
            print("Введіть ім\'я контакту")
            name = input("> ").strip()
            print("Введіть призвіще контакту")
            last_name = input("> ").strip()
            print("Введіть місто проживання")
            city_live = input("> ").strip()
    new_contact = {
        'name': name,
        'last name': last_name,
        'phone': phone,
        'city': city_live
    }
    phone_book = open(filename, 'r+')
    try:
        all_contacts = json.load(phone_book)
        all_contacts.append(new_contact)
    except json.decoder.JSONDecodeError:
        all_contacts = []
        all_contacts.append(new_contact)
        my_phone_book.append(new_contact)
    phone_book.seek(0)
    json.dump(all_contacts, phone_book, indent=4)
    print('Контакт збережено')
    phone_book.close()


find_list = {
    'name': 'пошук за ім\'ям',
    'last name': 'пошук за призвіщем',
    'city': 'пошук по місту проживання',
    'phone': 'пошук по по номеру телефону'
}
find_listToprint = [': '.join(prety) for prety in find_list.items()]
print("Вітаємо Вас в телефонній книзі.")
operation_list = {
    'list': 'Переглянути список контактів',
    'find': 'пошук контакту',
    'add': 'додавання контакту',
    'edit': 'змінити контакт',
    'exit': 'вихід'
}
operation_listToprint = [': '.join(prety) for prety in operation_list.items()]
print(f'В телефонній книзі доступні наступні команди.')
print(*operation_listToprint, sep='\n')
try:
    while True:
        print("Введiть команду: ")
        command1 = input('> ').strip().lower()
        command = {''.join(command1)}
        command = choice_find(command, operation_list)
        if command == 'exit':
            break
        elif command == 'add':
            add()
            empty_list = True
        elif empty_list is True:
            if command == 'list':
                list ( my_phone_book )
            elif command == 'del':
                delete(my_phone_book)
            elif command == 'find':
                print(*find_listToprint, sep='\n')
                print("\nОберіть критерій пошуку: ")
                command_find = input('>').strip()
                command_find = {''.join(command_find)}
                command_find = choice_find(command_find, find_list)
                if command_find == 'name':
                    criterion = 'name'
                    print("Введіть iм\'я: ")
                    print(find(my_phone_book, criterion))
                elif command_find == 'last name':
                    criterion = 'last name'
                    print("Введіть призвіще: ")
                    find(my_phone_book, criterion)
                elif command_find == 'city':
                    print("Введіть місто проживання: ")
                    criterion = 'city'
                    find(my_phone_book, criterion)
                elif command_find == 'phone':
                    criterion = 'phone'
                    print("Введіть номер телеіону: ")
                    find(my_phone_book, criterion)
                elif command == 'edit':
                    print('Вибачте ця команда на стадії налаштування. Спробуйте іншу команду.')
                    pass    #edit(my_phone_book)
                else:
                    print("Даний критерій пошуку не підтримується")
        elif empty_list is False and command is not None:
            print('База даних порожня тому пошук, видалення, редагування неможливий. Спробуйте іншу команду.')

        else:
            print(f"{command1} ця команда не підтримується.")
except Exception:
    print('Вибачте критична помилка Вам доведеться перезапустити програму.')
finally:
    print('Дані збережено у файл.')
    json_file.close()
