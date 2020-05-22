class ControllerTV:

    def __init__(self, list_tv, number):
        self.name = list_tv
        self.number = number

    def __str__(self):
        return f'{self.number} - {self.name}'

    def first_tv(self):
        self.number = 1
        return self.current_tv()

    def last_tv(self):
        self.number = len(self.name)
        return self.current_tv()

    def current_tv(self):
        return self.number, self.name[self.number - 1]

    def previous_tv(self):
        while True:
            self.number = (self.number - 1) % (len(self.name) + 1)
            if self.number == 0:
                self.number = len(self.name)
            return self.current_tv()

    def get_tv(self, index_tv):
        if 0 < index_tv <= len(self.name):
            self.number = index_tv
            return self.current_tv()
        else:
            index_tv = f'{index_tv} нe дійсний канал'
            return index_tv

    def next_tv(self):
        while True:
            self.number = (self.number + 1) % len(self.name)
            if self.number == 0:
                self.number = len(self.name)
            return self.current_tv()


# функція перевірки операції на валідність
def choice_valide(operation):
    oper_user = None
    for t in operation:
        if t in operation_valid:
            oper_user = t
            break
    return oper_user


channels = ["BBC", "Discovery", "TV1000", "MTV", "Sci-Fi", "GALAXY TV", "CNN"]
channels_obj = ControllerTV(channels, number=1)

operation_valid = {
    '1': 'Ввімкнеться перший канал у списку',
    '-': 'Ввімкнеться попередній канал у списку',
    '+': 'Ввімкнеться наступний канал у списку',
    '?': 'Ввімкнеться канал у списку який ви оберете.',
    '!': 'Показує поточний телеканал',
    '0': 'Ввімкнеться останній канал у списку',
    '*': 'Вихід'
}
operationToprint = [' : '.join(pretty) for pretty in operation_valid.items()]
print(*operationToprint, sep='\n')

try:
    while True:
        print('Оберіть операцію для управління каналами: ')
        tv_oper = (input('> ')).strip()
        tv_oper = {''.join(tv_oper)}
        tv_oper = (choice_valide(tv_oper))
        if tv_oper == '*':
            print('До побачення')
            break
        if tv_oper == '!':
            print(channels_obj.current_tv())
        elif tv_oper == '1':
            print(channels_obj.first_tv())
        elif tv_oper == '0':
            print(channels_obj.last_tv())
        elif tv_oper == '-':
            print(channels_obj.previous_tv())
        elif tv_oper == '+':
            print(channels_obj.next_tv())
        elif tv_oper == '?':
            print('Натисніть номер каналу для перегляду: ')
            tv = (input('> ')).strip()
            while not tv.isdigit():
                if not tv.isdigit():
                    print('Номер каналу місчтить не лише цифри: ')
                    tv = input('> ').strip()
                else:
                    print('Даного TV каналу не існує: ')
                    tv = input('> ').strip()
            index_tv = int(tv)
            print(channels_obj.get_tv(index_tv))
        else:
            print('Дана операція не підтримується.')
except Exception as h:
    print('Halepa', h)
