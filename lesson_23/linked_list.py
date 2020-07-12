from typing import List, Any, NoReturn


class MapLinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next_item = None


class MyLinkedList:
    def __init__(self):
        self.linked_list = {}

    def empty_cool_stack(self) -> bool:
        """ checks if the list is empty """
        if self.linked_list:
            return True
        return False

    def length_linked_list(self) -> int:
        """ calculates the length of the linked_list """
        count = 0
        if self.empty_cool_stack() is True:
            for key in self.linked_list.keys():
                count += 1
        return count

    def add_cool_stack_end(self, add_item: Any) -> NoReturn:
        """ adds an element to the end of the linked_list """
        add_dict: dict = dict()
        start_key = 0
        if self.linked_list:
            for key, data in self.linked_list.items():
                if data['next'] is None:
                    new_key = key + 1
                    data['next'] = new_key
                    news_data = MapLinkedList(add_item)
                    news_data.next_item = None
                    add_dict['value'] = news_data.data
                    add_dict['next'] = news_data.next_item
                    self.linked_list[new_key] = add_dict
                    return
        new_data = MapLinkedList(add_item)
        add_dict['value'] = new_data.data
        add_dict['next'] = new_data.next_item
        self.linked_list[start_key] = add_dict

    def add_cool_stack_after(self, after_item: Any, add_item: Any) -> NoReturn:
        """ adds an item after the specified item of the linked_list """
        add_dict: dict = dict()
        if self.linked_list:
            for key, data in self.linked_list.items():
                if data['value'] == after_item:
                    new_key = self.length_linked_list() + 1
                    old_key = data['next']
                    data['next'] = new_key
                    news_data_before = MapLinkedList(add_item)
                    news_data_before.next_item = old_key
                    add_dict['value'] = news_data_before.data
                    add_dict['next'] = news_data_before.next_item
                    self.linked_list[new_key] = add_dict
                    return
            return self.add_cool_stack_end(add_item)
        new_key = 0
        new_data = MapLinkedList(add_item)
        add_dict['value'] = new_data.data
        add_dict['next'] = new_data.next_item
        self.linked_list[new_key] = add_dict

    def take_cool_stack(self, take_item: Any) -> Any:
        """" deletes the specified item and returns it """
        if self.length_linked_list() > 1:
            for key, data in self.linked_list.items():
                if data['value'] == take_item:
                    know_key = data['next']
                    prev_key = key
                    show = data
                    del self.linked_list[key]
                    for key_prev, data_prev in self.linked_list.items():
                        if data_prev['next'] == prev_key:
                            data_prev['next'] = know_key
                    return show
            return False
        else:
            self.linked_list.clear()

    def __str__(self):
        return f'{dict(self.linked_list)}'


my = MyLinkedList()
my.add_cool_stack_end('April')
my.add_cool_stack_end('May')
my.add_cool_stack_end('June')
my.add_cool_stack_end('Juli')
print(my, 1)
my.add_cool_stack_after('April', 'March')
print(my, 2)
print(my.empty_cool_stack(), 3)
print(my.take_cool_stack('March'), 4)
print(my.linked_list, 5)
