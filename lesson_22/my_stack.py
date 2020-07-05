from typing import List, Any, NoReturn

class My_Stack:
    def __init__(self):
        self.cool_stack: List[Any] = []

    def empty_cool_stack(self) -> bool:
        if len(self.cool_stack) == 0:
            return True
        return False

    def add_cool_stack(self, add_item: Any) -> NoReturn:
        self.cool_stack.append(add_item)

    def take_cool_stack(self) -> Any:
        if len(self.cool_stack) == 0:
            return
        return self.cool_stack.pop()

    def __str__(self):
        return f'{list(self.cool_stack)}'
rrr = [i for i in range(10)]
super_stack = My_Stack()
new_super_stack = My_Stack()
print(rrr)
print ( super_stack, 'lll;' )
x = 0
while x == 0:
    if super_stack.empty_cool_stack == True:
        x = 1
        for takes in super_stack.take_cool_stack():
            new_super_stack.add_cool_stack(takes)

        print ( super_stack, 'uuu' )
    elif super_stack.empty_cool_stack() == True:

        for adds in rrr:
            super_stack.add_cool_stack(adds)
        print ( super_stack, 'ppp' )
print(super_stack.empty_cool_stack(), '888')
print(super_stack, '555')
print(new_super_stack, '222')