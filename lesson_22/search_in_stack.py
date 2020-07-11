from typing import List, Any, NoReturn


class My_Stack:
    def __init__(self):
        self.cool_stack: List[Any] = []

    def empty_cool_stack(self) -> bool:
        """ checks if the list is empty """
        if len(list(self.cool_stack)) == 0:
            return True
        return False

    def add_cool_stack(self, add_item: Any) -> NoReturn:
        """ adds an item to the list """
        self.cool_stack.append(add_item)

    def take_cool_stack(self) -> Any:
        """ deletes the last item in the list """
        if len(self.cool_stack) != 0:
            return self.cool_stack.pop()

    def get_from_stack(self, item_search: Any) -> Any:
        """ removes the specified item from the stack """
        try:
            new_stack = []
            i = None
            while self.empty_cool_stack() is False:
                ns = self.take_cool_stack()
                if ns != item_search:
                    new_stack.append(ns)
                elif ns == item_search:
                    i = ns
            if i is None:
                raise ValueError
            while new_stack:
                self.add_cool_stack(new_stack.pop())
            return i
        except ValueError:
            return False

    def __str__(self):
        return f'{list(self.cool_stack)}'


rrr = [i for i in range(10)]
super_stack = My_Stack()
new_super_stack = My_Stack()

print ( super_stack, '0')
x = 0

if super_stack.empty_cool_stack is False:
    for takes in super_stack.take_cool_stack():
        new_super_stack.add_cool_stack(takes)
if super_stack.empty_cool_stack() is True:
    for adds in rrr:
        super_stack.add_cool_stack(adds)
print(super_stack, '1')
print(super_stack.empty_cool_stack(), '2')
while super_stack.empty_cool_stack() is False:
    new_super_stack.add_cool_stack(super_stack.take_cool_stack())


print (new_super_stack, '3')
print(super_stack.empty_cool_stack(), '4')
print(super_stack, '5')
print(new_super_stack, '6')
print(super_stack.empty_cool_stack(), 'Empty')
print(new_super_stack.get_from_stack(5), '7')
print(new_super_stack, '8')





