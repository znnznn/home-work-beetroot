import unittest
#  from lesson_17.typy_in_func import choice_find
from lesson_17.typy_in_func import choice_find

'''def choice_find(x, y):    
    """"checking operation valid"""
    print(x, y)
    choice_oper = None
    for t in y:
        if t == x:
            choice_oper = t
        return choice_oper
'''


class MyTestPhoneBook(unittest.TestCase):

    def test_choice_find(self):
        """"function test checking operation valid with dict"""

        result_choice_find = choice_find('yyy', {'list': 'ok'})
        self.assertEqual(result_choice_find, None)

    def test_choice_find_not_none(self):
        """"function test checking operation valid with dict """

        result_choice_find = choice_find('list', {'list': 'ok'})
        self.assertEqual(result_choice_find, 'list')

    def test_choice_find_empty_data(self):
        """"function test checking operation valid with empty list """

        result_choice_find = choice_find('list', [])
        self.assertEqual(result_choice_find, None)

    def test_choice_find_list(self):
        """"function test checking operation valid with list """

        result_choice_find = choice_find('list', ['list', 1])
        self.assertEqual(result_choice_find, 'list')


if __name__ == '__main__':
    unittest.main()
