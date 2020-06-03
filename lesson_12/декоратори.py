def myDecorator(choice_func):
    def printResultBoolevo(*args, **kwargs):
        print(f'{choice_func.__name__} функція почалась виконувати')
        my_func = choice_func(*args, **kwargs)
        if my_func is None:
            return f'Така команда {args[1]} не підтримується спробуйте ще.'
        print(f'Команда {args[1]} може бути виконана')
        return my_func
    return printResultBoolevo


@myDecorator
def choice_find(x_list, y_comand):
    choice_oper = None
    for t in x_list:
        if t not in y_comand:
            return choice_oper
        else:
            choice_oper = t
            return choice_oper


operation_list = {
    'list': 'Переглянути список контактів',
    'find': 'пошук контакту',
    'add': 'додавання контакту',
    'del': 'видалити контакт',
    'edit': 'змінити контакт',
    'exit': 'вихід'
}
print(choice_find(['1', 2, 3, 4], '1'))
print(choice_find(operation_list, 'list'))