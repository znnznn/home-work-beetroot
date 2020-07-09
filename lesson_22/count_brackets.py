from typing import List, Any, NoReturn


class CountBrackets:
    def __init__(self):
        self.brackets = []

    def empty_cool_stack(self) -> bool:
        if len(list(self.brackets)) == 0:
            return True
        return False

    def add_cool_stack(self, add_item: Any) -> NoReturn:
        self.brackets.append(add_item)

    def take_cool_stack(self) -> Any:
        if len(self.brackets) != 0:
            return self.brackets.pop()

    def show_cool_stack(self):
        if len(self.brackets) != 0:
            return self.brackets[-1]

    def __str__(self):
        return f'{list(self.brackets)}'


def count_brackets(item: str) -> bool:
    brackets = "〈〉()[]{}"
    open_brackets = brackets[::2]
    close_brackets = brackets[1::2]
    stack_brackets = CountBrackets()
    for i in item:
        if i in open_brackets:
            stack_brackets.add_cool_stack(i)
        elif i in close_brackets:
            if i == '〉' and '〈' == stack_brackets.show_cool_stack():
                stack_brackets.take_cool_stack()
            elif i == ')' and '(' == stack_brackets.show_cool_stack():
                stack_brackets.take_cool_stack()
            elif i == ']' and '[' == stack_brackets.show_cool_stack():
                stack_brackets.take_cool_stack()
            elif i == '}' and '{' == stack_brackets.show_cool_stack():
                stack_brackets.take_cool_stack()
            else:
                return False
    return True

fake = '5+6(5+6)+{}'

print(count_brackets(fake))
