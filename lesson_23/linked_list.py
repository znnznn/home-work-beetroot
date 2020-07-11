from typing import List, Any, NoReturn


class MapLinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next_item = None


class MyLinkedList:
    def __init__(self, ):
        self.linked_list = {}

    def empty_cool_stack(self) -> bool:
        pass

    def add_cool_stack(self, add_item: Any) -> NoReturn:
        add_dict = dict()
        i = 0
        if self.linked_list:
            for key, data in self.linked_list.items():
                if data['next'] is None:
                    new_key = key + 1
                    data['next'] = new_key
                    new_data1 = MapLinkedList(add_item)
                    new_data1.next_item = None
                    add_dict['value'] = new_data1.data
                    add_dict['next'] = new_data1.next_item
                    self.linked_list[new_key] = add_dict
                    return
        new_data = MapLinkedList(add_item)
        add_dict['value'] = new_data.data
        add_dict['next'] = new_data.next_item
        self.linked_list[i] = add_dict

    def take_cool_stack(self) -> Any:
        pass

    def __str__(self):
        return f'{list(self.linked_list)}'


my = MyLinkedList()
my.add_cool_stack('April')
my.add_cool_stack('May')
my.add_cool_stack('June')
my.add_cool_stack('Juli')
print(my.linked_list)
