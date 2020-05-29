import json
import sys


class PhoneBook:
    def __init__(self, json_file):
        self.json_file = json_file

    def file_list_print(self):  # виводить данні телефонної книги
        number_of_records = len(self.json_file)
        for i in self.json_file:
            print(i, sep='\n')
        return print(f'В телефонній книці знаходиться {number_of_records} контактів')

    def keys_data(self):
        item_keys_data = self.json_file[0]
        return item_keys_data.keys()

    def jason_file_overwrite(self):
        with open('phone_book.json', 'w') as new_data:
            json.dump ( self.json_file, new_data, indent=4)

    def find(self, find_data):  # повертає шуканий елемент або None
        for find_values in self.json_file:
            if find_data in find_values.values():
                print('YES')
                return find_values

    def find_print(self, criterion):
        find_value = input("> ").strip().capitalize()
        work_my_phone_book = self.json_file
        row = []
        row_index = []
        for index, value in enumerate(work_my_phone_book):
            if find_value == value[criterion]:
                row.append(value)
                row_index.append(index)
            else:
                continue
            if len(row) == 0:
                return print(f'Данні по {criterion} {find_value} відсутні.')
        return print(f"Данні по {criterion} {find_value}: знайдено {len ( row )}'\n' {row}', '\n"), row_index

    def delete(self, criterion):
        print("Введіть номер телефону для видалення: ")
        phone_number = input('> ').strip()
        while not phone_number.isdigit():
            print(f'{phone_number} містить не лише цифри')
            print("Введіть знову номер телефону")
            phone_number = input("> ").strip()
        phone_number_valide = self.find(phone_number)
        if phone_number_valide is not None:
            for number in self.json_file:
                if number[criterion] == phone_number:
                    print(f"Ви дійсно бажаєте видалити контект (yes/no)?: {number}")
                    oper_del = input('> ').strip().lower()
                    if oper_del == 'yes':
                        try:
                            self.json_file.remove(number)
                            print(f"Ви видалили контакт {number}")
                        except Exception as e:
                            print('Сталась критична помилка. Вибачте.', e)
                else:
                    continue
        else:
            print(f'Номер телефону {phone_number} не знайдено.')
            return print(f'Спробуйте іншу операцію. Наприклад: find')

    def edit(self, index_edit, criterion):
        print(f'Введіть нові данні для {criterion}.')
        new_data = input('> ').strip().capitalize()
        try:
            if criterion == 'phone':
                while not criterion.isdigit():
                    print(f'Ви ввели не лише чилса для {criterion}.')
            self.json_file[index_edit[0]][criterion] = new_data
            print(self.json_file)
            return 'Контакт відредаговано'
        except Exception as e:
            print('помилка зміни данних в (edit)', e)

    def add_data(self):
        try:
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
            self.json_file.append(new_contact)
            return print('Контакт збережено')
        except Exception as e:
            print('Сталась помилка в додаванні данних', e)


try:
    if len(sys.argv) < 2:
        print('Введіть базу данних з якою Ви бажаєте працювати')
        sys_argv1 = input('> ')
        filename = sys_argv1
    else:
        filename = sys.argv[1]
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
json_file = open(filename, 'r')   # підсвічується filename
try:
    my_phone_book = json.load(json_file)
    empty_list = True
except Exception:
    empty_list = False
    my_phone_book = []
json_file.close()
phone_book_data = PhoneBook(my_phone_book)


def choice_find(x, y):
    choice_oper = None
    for t in x:
        if t not in y:
            return choice_oper
        else:
            choice_oper = t
            return choice_oper


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
    'del': 'видалити контакт',
    'edit': 'змінити контакт',
    'exit': 'вихід'
}

operation_list_too_print = [': '.join(pretty) for pretty in operation_list.items()]
print(f'В телефонній книзі {filename} доступні наступні команди.')
print(*operation_list_too_print, sep='\n')

try:
    while True:
        print("Введiть команду: ")
        command_input = input('> ').strip().lower()
        command = {''.join(command_input)}
        command = choice_find(command, operation_list)
        if command == 'exit':
            break
        elif command == 'add':
            phone_book_data.add_data()
            empty_list = True
        elif empty_list is True:
            if command == 'list':
                phone_book_data.file_list_print()
            elif command == 'edit':
                print(*find_listToprint, sep='\n')
                print('Оберіть критерій пошуку')
                command_find_input = input('>').strip()
                command_find = {''.join(command_find_input)}
                command_find = choice_find(command_find, find_list)
                if command_find is not None:
                    command_find = command_find_input
                    print('Введіть пошукове значення')
                    edit_find, index_edit = phone_book_data.find_print(command_find)
                    if len(index_edit) != 0:
                        if len(index_edit) > 1:
                            print('Ви вибрали для зміни більше ніж один контакт. Спробуйте ще раз')
                            continue
                        else:
                            phone_book_data.edit(index_edit, command_find)
                    else:
                        print('Даного контакту не існує. Спробуйте ще раз.')
                        continue
                else:
                    print("Даний критерій пошуку не підтримується")
            elif command == 'del':
                criterion = 'phone'
                phone_book_data.delete(criterion)
            elif command == 'find':
                print(*find_listToprint, sep='\n')
                print("Оберіть критерій пошуку: ")
                command_find = input('>').strip()
                command_find = {''.join(command_find)}
                command_find = choice_find(command_find, find_list)
                if command_find is not None:
                    criterion = command_find
                    print(f"Введіть {criterion} яке ви шукаєте: ")
                    phone_book_data.find_print(criterion)
                else:
                    print("Даний критерій пошуку не підтримується")
        elif empty_list is False and command is not None:
            print('База даних порожня тому пошук, видалення, редагування неможливий. Спробуйте іншу команду.')
        else:
            print(f"{command_input} ця команда не підтримується.")
except Exception as e:
    print('Вибачте сталась критична помилка. Вам доведеться перезапустити програму.', e)
finally:
    print('Дані збережено у файл.')
    phone_book_data.jason_file_overwrite()
