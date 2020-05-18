class ControllerTV:

    def __init__(self, name='no name', number=0):
        self.name = name
        self.number = number

    def __str__(self):
        return f'{self.number} - {self.name}'

    def __next__(self):
        self += 1
        return f'{self.number} - {self.name}'

    def __iter__(self):
        pass                    # як правильно створити ітератор

    def find_f(self):
        i = 1
        for i in channels_obj:  # як ітерувати не зі списку об'єктів, а напряму з класу ітерувати всі об'єкти
            if i.number == self:
                return i
        return i

    def __contains__(self, item):
        pass


# функція перевірки операції на валідність
def choice_valide(operation):
    oper_user = None
    for t in operation:
        if t in operation_valid:
            oper_user = t
            break
    return oper_user


channels = ["BBC", "Discovery", "TV1000", "MTV", "Sci-Fi", "GALAXY TV", "CNN"]
channels_obj = []
for number, name in enumerate(channels, 1):
    channels_obj.append(ControllerTV(name, number))
print(*channels_obj, sep='\n')


    #print(channels_obj.__next__(d))
    #print(dir(channels_obj))
    #print(channels_obj.__getitem__(6))
a = ([i for i in enumerate(channels, 1)])
    #print(channels_obj.__class__.__len__(channels_obj))

    #print(channels_obj.__class__.__next__(d))

operation_valid = {
    '1': 'Ввімкнеться перший канал у списку',
    '-': 'Ввімкнеться попередній канал у списку',
    '+': 'Ввімкнеться наступний канал у списку',
    '?': 'Ввімкнеться канал у списку який ви оберете.',
    '0': 'Ввімкнеться останній канал у списку',
    '*': 'Вихід'
}
operationToprint = [' : '.join(pretty) for pretty in operation_valid.items()]
print(*operationToprint, sep='\n')
    #print(channels_obj.__class__.__getitem__(ControllerTV))
print(ControllerTV.find_f(self=1))
try:
    index_tv = 0
    len_obj = channels_obj.__class__.__len__(channels_obj)
    while True:
        print('Оберіть операцію для управління каналами: ')
        tv_oper = (input('> ')).strip()
        tv_oper = {''.join(tv_oper)}
        tv_oper = (choice_valide(tv_oper))
        tv = channels_obj[index_tv]
        if tv_oper == '*':
            print('До побачення')
            break
        if tv_oper == '1':
            print(ControllerTV.find_f(index_tv))
        elif tv_oper == '0':
            index_tv = len_obj
            print(ControllerTV.find_f(index_tv))
        elif tv_oper == '-':
            if index_tv == 1:
                index_tv = len_obj
                print(ControllerTV.find_f(index_tv))
            else:
                index_tv -= 1
                print(ControllerTV.find_f(index_tv))
        elif tv_oper == '+':
            if index_tv < len_obj:
                index_tv += 1
                print(ControllerTV.find_f(index_tv))
            else:
                index_tv = 1
                print(ControllerTV.find_f(index_tv))
        elif tv_oper == '?':
            print('Натисніть номер каналу для перегляду: ')
            tv = (input('> ')).strip()
            while not tv.isdigit() or int(tv) > len_obj:
                if not tv.isdigit():
                    print('Номер каналу місчтить не лише цифри: ')
                    tv = input('> ').strip()
                else:
                    print('Даного TV каналу не існує: ')
                    tv = input('> ').strip()
            index_tv = int(tv)
            print(ControllerTV.find_f(index_tv))
        else:
            print('Дана операція не підтримується.')
except Exception as h:
    print('Halepa', h)
