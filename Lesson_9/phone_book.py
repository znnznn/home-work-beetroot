import json
my_phone_book = open('phone_book.json', 'w+')

contacts = [
    {
        "name": "Mark",
        "last name": "Markin",
        "phone": "123456",
        "city": "Rivne"
    },
    {
        "name": "Julia",
        "last name": "Markin",
        "phone": "564321",
        "city": "Rivne"
    },
    {
        "name": "Bohdan",
        "last name": "Markin",
        "phone": "+1234",
        "city": "Dnipro"
    },
]
with open('phone_book.json', 'w') as phone_book:
    json.dump(contacts, phone_book, indent=4)




def list(my_phone_book):
        for i in json.load(my_phone_book):
            print(i, sep='\n')


def choice_find(x, y):
    for t in x:
        if t not in y:
            return None
        else:
            return t


def find(my_phone_book):
    name = input("> ")
    row = []
    item = 0
    for value in json.load(my_phone_book):
        for i, x in value.items():
            if name == x:
                row.append(value)
                item += 1
            else:
                continue
        if item == 0:
            return print(f'Данні по {i} {name} відсутні.')
    return print(f"Данні по {i} {name} '\n' {[s for s in row]}', '\n'"), row



def delete(my_phone_book):
    print("Введіть контакт: ")
    name = input('> ').strip()
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
    print("Введіть місто проживання")
    city_live = input("> ").strip()
    new_contact = {
        'name': name,
        'Last name': last_name,
        'phone': phone,
        'city': city_live
    }

    with open('phone_book.json', 'a') as phone_book:
        json.dump(new_contact, phone_book)
        contacts.append(new_contact)
    print('Контакт збережено')


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
print(*operation_listToprint, sep='\n')

while True:
    print("Введiть команду: ")
    command1 = input('> ').strip()
    command = {''.join(command1)}
    command = choice_find(command, operation_list)
    if command == 'list':
        list(my_phone_book)
    elif command == 'find':
        print(*find_listToprint, sep='\n')
        print("\nОберіть критерій пошуку: ")
        command_find = input('>').strip()
        command_find = {''.join(command_find)}
        command_find = choice_find(command_find, find_list)
        if command_find == 'name':
            print("Введіть iм'я: ")
            print(find(my_phone_book))
        elif command_find == 'last name':
            print("Введіть призвіще: ")
            find(my_phone_book)
        elif command_find == 'city':
            print("Введіть місто проживання: ")
            find(my_phone_book)
        elif command_find == 'find phone':
            print("Введіть номер телеіону: ")
            find(my_phone_book)
        else:
            print("Даний критерій пошуку не підтримується")
    elif command == 'add':
        add()
    elif command == 'del':
        delete(my_phone_book)
        '''elif command == 'edit':
        edit(my_phone_book)'''
    elif command == 'exit':
        break
    else :
        print(f"{command1} ця команда не підтримується.")
my_phone_book.close()
