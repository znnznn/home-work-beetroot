import json
import sys



from typing import Dict, Type, Union, Optional, Any, Iterable, Iterator, List


def list(filename: str):
    with open(filename, 'r') as phone_book:
        for i in json.load(phone_book):
            print(i, sep='\n')


def choice_find(x: Any, y: Dict) -> Optional[Dict]:
    """"checking operation valid"""
    print(x, y)
    choice_oper = None
    for t in y:
        if t == x:
            choice_oper = t
        return choice_oper


def find(my_phone_book: list, criterion: str) -> Union[str, list]:
    """"search for an item by criterion"""
    find_value = input("> ").strip().capitalize()
    work_my_phone_book = my_phone_book.copy()
    row = []
    row_index = []
    for index, value in enumerate(work_my_phone_book):
        if find_value == value[criterion]:
            row.append(value)
            row_index.append(index)
        else:
            continue
        if len(row_index) == 0:
            return f'Данні по {criterion} {find_value} відсутні.'
    return f"Данні по {criterion} {find_value}: знайдено {len(row)}'\n' {row}', '\n", row_index


def delete(criterion: str):
    """"delete an item by criterion"""
    print("Введіть номер телефону для видалення: ")
    phone_number = input('> ').strip()
    phone_book = open(filename, 'r')
    all_contacts = json.load ( phone_book )
    phone_book.close()
    item = 0
    while not phone_number.isdigit():
        print(f'{phone_number} містить не лише цифри')
        print("Введіть знову номер телефону")
        phone_number = input("> ").strip()
    for number in all_contacts:
        if number[criterion] == phone_number:
            print(f"Ви дійсно бажаєте видалити контект (yes/no)?: {number}")
            name_del = input('> ').strip()
            if name_del == 'yes':
                item += 1
                phone_book = open(filename, 'w')
                try:
                    all_contacts.remove(number)
                except Exception:
                    print('Сталась критична помилка. Вибачте.')
                phone_book.seek(0)
                json.dump(all_contacts, phone_book, indent=4)
                print(f"Ви видалили контакт {number}")
        else:
            continue
        if item == 0:
            print(f'Номер телефону {phone_number} не знайдено.')
    phone_book.close()
    return f'Спробуйте іншу операцію. Наприклад: find'


def edit(index_edit: int):
    """"edit an item by criterion"""

    phone_book = open(filename, 'r')
    print(index_edit)
    work_my_phone_book = json.load(phone_book)
    phone_book.close()
    phone_book = open(filename, 'w')
    print(work_my_phone_book)
    del work_my_phone_book[index_edit[0]]
    print(work_my_phone_book)
    json.dump(work_my_phone_book, phone_book, indent=4)
    phone_book.close()
    print('Введіть нові данні для даного контакту.')
    add()
    print('Контакт відредаговано')


def add():
    """"add an item"""
    print("Введіть ім\'я контакту")
    name = input("> ").strip().capitalize()
    while not name.isalpha():
        print(f'{name} містить не лише букви. Введіть лише букви.')
        print("Введіть знову ім\'я: ")
        name = input("> ").strip().capitalize()
    print("Введіть призвіще контакту")
    last_name = input("> ").strip().capitalize()
    while not last_name.isalpha():
        print(f'{last_name} містить не лише букви. Введіть лише букви.')
        print("Введіть знову призвіще: ")
        last_name = input("> ").strip().capitalize()
    print("Введіть номер телефону")
    phone = input("> ").strip()
    while not phone.isdigit():
        print(f'{phone} містить не лише цифри')
        print("Введіть знову номер телефону")
        phone = input("> ").strip()
    print("Введіть місто проживання")
    city_live = input("> ").strip().capitalize()
    while not city_live.isalpha():
        print(f'{city_live} містить не лише букви. Введіть лише букви.')
        print("Введіть знову призвіще: ")
        city_live = input("> ").strip().capitalize()
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
    phone_book.close()
    return f'Контакт збережено'


find_list = {
    'name': 'пошук за ім\'ям',
    'last name': 'пошук за призвіщем',
    'city': 'пошук по місту проживання',
    'phone': 'пошук по по номеру телефону'
}

find_listToprint = [': '.join(pretty) for pretty in find_list.items()]
print("Вітаємо Вас в телефонній книзі.")
operation_list = {
    'list': 'Переглянути список контактів',
    'find': 'пошук контакту',
    'add': 'додавання контакту',
    'del': 'видалити контакт',
    'edit': 'змінити контакт',
    'exit': 'вихід'
}

operation_listToprint = [': '.join(pretty) for pretty in operation_list.items()]


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print('Введіть базу данних з якою Ви бажаєте працювати')
            sys_argv1 = input('> ')
            filename = sys_argv1
        else:
            filename = sys.argv[1]
        print(sys.argv)
        json_file = open(filename, 'r')
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
        print('Ви створили критичну помилку. Перезапустіть програму.')
        exit()

    try:
        my_phone_book = json.load(json_file)
        empty_list = True
    except Exception:
        empty_list = False
        my_phone_book = []
    json_file.close()
    print(f'В телефонній книзі {filename} доступні наступні команди.')
    print(*operation_listToprint, sep='\n')

    try:
        while True:
            print("Введiть команду: ")
            command1 = input('> ').strip().lower()
            command = {''.join(command1)}
            print(command)
            command = choice_find(command, operation_list)
            if command == 'exit':
                break
            elif command == 'add':
                add()
                empty_list = True
            elif empty_list is True:
                if command == 'list':
                    list(filename)
                elif command == 'edit':
                    print(*find_listToprint, sep='\n')
                    print('Оберіть критерій пошуку')
                    command_find1 = input('>').strip()
                    command_find = {''.join(command_find1)}
                    command_find = choice_find(command_find, find_list)
                    if command_find is not None:
                        command_find = command_find1
                        print('Введіть пошукове значення')
                        edit_find, index_edit = find(my_phone_book, command_find)
                        if len(index_edit) != 0:
                            if len(index_edit) > 1:
                                print(index_edit, len(index_edit))
                                print('Ви вибрали для зміни більше ніж один контакт. Спробуйте ще раз')
                                continue
                            else:
                                print(index_edit)
                                edit(index_edit)
                        else:
                            print('Даного контакту не існує. Спробуйте ще раз.')
                            continue
                    else:
                        print("Даний критерій пошуку не підтримується")
                elif command == 'del':
                    criterion = 'phone'
                    delete(criterion)
                elif command == 'find':
                    print(*find_listToprint, sep='\n')
                    print("\nОберіть критерій пошуку: ")
                    command_find = input('>').strip()
                    command_find = {''.join(command_find)}
                    command_find = choice_find(command_find, find_list)
                    if command_find == 'name':
                        criterion = 'name'
                        print("Введіть iм\'я: ")
                        find(my_phone_book, criterion)
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
                        print("Введіть номер телефону: ")
                        find(my_phone_book, criterion)
                    else:
                        print("Даний критерій пошуку не підтримується")
            elif empty_list is False and command is not None:
                print('База даних порожня тому пошук, видалення, редагування неможливий. Спробуйте іншу команду.')
            else:
                print(f"{command1} ця команда не підтримується.")
    except Exception:
        print('Вибачте сталась критична помилка. Вам доведеться перезапустити програму.')
    finally:
        print('Дані збережено у файл.')
        json_file.close()


