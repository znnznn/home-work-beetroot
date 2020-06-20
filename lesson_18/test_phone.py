import unittest
#from lesson_17 import typy_in_func


def choice_find(x, y):
    """"checking operation valid"""
    print(x, y)
    choice_oper = None
    for t in y:
        if t not in x:
            return choice_oper
        else:
            choice_oper = t
            return choice_oper


class MyTestPhoneBook(unittest.TestCase):

    def test_choice_find(self):
        """"function test checking operation valid with dict"""

        result_choice_find = choice_find('yyy', {'mylist': 'ok'})
        self.assertEqual(result_choice_find, None)

    def test_choice_find_not_none(self):
        """"function test checking operation valid with dict """

        result_choice_find = choice_find('mylist', {'mylist': 'ok'})
        self.assertEqual(result_choice_find, 'mylist')

    def test_choice_find_empty_data(self):
        """"function test checking operation valid with empty list """

        result_choice_find = choice_find('mylist', [])
        self.assertEqual(result_choice_find, None)

    def test_choice_find_list(self):
        """"function test checking operation valid with list """

        result_choice_find = choice_find('mylist', ['mylist'])
        self.assertEqual(result_choice_find, 'mylist')


if __name__ == '__main__':
    unittest.main()
