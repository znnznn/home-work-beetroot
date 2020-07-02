import sys

import math

from functools import partial
from typing import Union, NoReturn

from PyQt5.Qt import Qt

from PyQt5.QtWidgets import (QApplication,
                             QSizePolicy,
                             QWidget,
                             QVBoxLayout,
                             QGridLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel)


class MyCalculatorInWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        """ Creates a calculator window"""
        super().__init__(*args, **kwargs)
        self.setWindowTitle('C A L C U L A T O R')
        self.widget = QWidget(self.setGeometry(600, 300, 500, 500))
        #  widget = QWidget(self.setFixedSize(550, 550))
        self.first_label = QLabel('<h1><b><i>Стандартний калькулятор</i></b></h1>')
        self.editArea = QLineEdit('')
        self.editArea.setReadOnly(True)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.first_label)
        mainLayout.addWidget(self.editArea)
        self.second_label = QLabel('')
        mainLayout.addWidget(self.second_label)

        buttonLayout = QGridLayout()
        self.result = ['']
        buttons = [
            {
                'name': '1',
                'row': 3,
                'col': 0
            },
            {
                'name': '2',
                'row': 3,
                'col': 1
            },
            {
                'name': '3',
                'row': 3,
                'col': 2
            },
            {
                'name': '+',
                'row': 3,
                'col': 3
            },
            {
                'name': '4',
                'row': 2,
                'col': 0
            },
            {
                'name': '5',
                'row': 2,
                'col': 1
            },
            {
                'name': '6',
                'row': 2,
                'col': 2
            },
            {
                'name': '-',
                'row': 2,
                'col': 3
            },
            {
                'name': '7',
                'row': 1,
                'col': 0
            },
            {
                'name': '8',
                'row': 1,
                'col': 1
            },
            {
                'name': '9',
                'row': 1,
                'col': 2
            },
            {
                'name': '*',
                'row': 1,
                'col': 3
            },
            {
                'name': '0',
                'row': 4,
                'col': 1
            },
            {
                'name': '.',
                'row': 4,
                'col': 2
            },
            {
                'name': '=',
                'row': 4,
                'col': 3,
                'colSpan': 2
            },
            {
                'name': '00',
                'row': 4,
                'col': 0,
            },
            {
                'name': 'C',
                'row': 0,
                'col': 0,
            },
            {
                'name': '%',
                'row': 0,
                'col': 1,
            },
            {
                'name': '←',
                'row': 0,
                'col': 2,
            },
            {
                'name': '÷',
                'row': 0,
                'col': 3
            },
            {
                'name': 'X²',
                'row': 0,
                'col': 4
            },
            {
                'name': '√',
                'row': 1,
                'col': 4
            },
            {
                'name': 'X !',
                'row': 2,
                'col': 4
            },
            {
                'name': '+/-',
                'row': 3,
                'col': 4
            }
        ]
        self.buttons = {}
        for buttonConfig in buttons:
            name = buttonConfig.get('name', '')
            btn = QPushButton(name)
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            self.buttons[name] = btn
            buttonLayout.addWidget(btn,
                                   buttonConfig['row'],
                                   buttonConfig['col'],
                                   1,
                                   buttonConfig.get('colSpan', 1))
        mainLayout.addLayout(buttonLayout)
        self.widget.setLayout(mainLayout)
        self.setCentralWidget(self.widget)

        for buttonName in self.buttons:
            btn = self.buttons[buttonName]
            if buttonName == 'C':
                btn.clicked.connect(self.end)
            elif buttonName == '+':
                btn.clicked.connect(partial(self.addSecondLable, buttonName))
            elif buttonName == '-':
                btn.clicked.connect(partial(self.addSecondLable, buttonName))
            elif buttonName == '.':
                btn.clicked.connect(partial(self.point_only_once, buttonName))
            elif buttonName == '%':
                btn.clicked.connect(partial(self.result_percent))
            elif buttonName == '*':
                btn.clicked.connect(partial(self.addSecondLable, buttonName))
            elif buttonName == '÷':
                btn.clicked.connect(partial(self.addSecondLable, '/'))
            elif buttonName == '←':
                btn.clicked.connect(partial(self.editAreaText_pop))
            elif buttonName == '+/-':
                btn.clicked.connect(partial(self.positive_negative_number))
            elif buttonName == 'X²':
                btn.clicked.connect(partial(self.result_pow))
            elif buttonName == 'X !':
                btn.clicked.connect(partial(self.result_factorial))
            elif buttonName == '√':
                btn.clicked.connect(partial(self.result_root))
            elif buttonName == '=':
                btn.clicked.connect(partial(self.result_expression, buttonName))
            else:
                btn.clicked.connect(partial(self.change_text, buttonName))

    def editAreaText_pop(self) -> str:
        """Get display's text del last item."""
        return self.editArea.setText(str(self.editArea.text()[:-1]))

    def point_only_once(self, text) -> str:
        """ Сhecks whether a point has been pressed once """
        calc_line = str(self.editArea.text())
        if len(calc_line) > 0 and calc_line[-1] != text:
            return self.editArea.setText(self.editArea.text() + text)
        elif len(calc_line) == 0:
            return self.editArea.setText('0' + text)
        elif len(calc_line) > 0:
            return self.editArea.setText(calc_line[:-1] + text)

    def result_pow(self) -> str:
        """ returns the square of a number """
        try:
            calc_line = str(self.editArea.text())
            if calc_line.count('e') > 0:
                raise ValueError
            if len(calc_line) == 0:
                self.second_label.setText('<h2><b><i>0</i></b></h2>')
                return self.editArea.setText('0')
            else:
                calc_line = str(self.editArea.text())
                text = f'Квадрат числа {calc_line} = '
            if float(calc_line):
                result = float(calc_line) ** 2
            else:
                result = int(calc_line) ** 2
            self.result.append(f'{text}{result}')
            self.second_label.setText(str(f'<h2><b><i>{self.result[-1]}</i></b></h2>'))
            return self.editArea.setText(str(result))
        except :
            self.second_label.setText(str(f'<h2><b><i>=Неможливо обрахувати результат{calc_line}</i></b></h2>'))
            return self.editArea.setText('0')

    def result_root(self) -> str:
        """ Returns the square root of a number"""
        try:
            calc_line = str(self.editArea.text())
            if len(calc_line) == 0:
                self.second_label.setText('<h2><b><i>0</i></b></h2>')
                return self.editArea.setText('0')
            else:
                calc_line = str(self.editArea.text())
                text = f'Квадратний корінь числа {calc_line} = '
            if calc_line.count('e') != 0:
                raise ValueError
            result = float(calc_line) ** 0.5
            self.result.append(f'{text}{result}')
            self.second_label.setText(str(f'<h2><b><i>{self.result[-1]}</i></b></h2>'))
            return self.editArea.setText(str(result))
        except Exception:
            self.second_label.setText(str(f'<h2><b><i>=Неможливо обрахувати результат{calc_line}</i></b></h2>'))
            return self.editArea.setText('0')

    def result_factorial(self) -> str:
        """ Returns the factorial of a number"""
        calc_line = str(self.editArea.text())
        try:
            if len(calc_line) == 0:
                self.second_label.setText('<h2><b><i>0</i></b></h2>')
                return self.editArea.setText('0')
            elif len(calc_line) > 3 or calc_line.count('e') > 0:
                raise ValueError
            digit = math.trunc(float(calc_line))
            text = f'Факторіал числа {digit} = '
            result = math.factorial(digit)
            self.result.append(f'{text}{result}')
            self.second_label.setText(str(f'<h2><b><i>{self.result[-1]}</i></b></h2>'))
            return self.editArea.setText(str(result))
        except ValueError:
            self.second_label.setText(str(f'<h2><b><i>=Завелике число для обрахунку {calc_line}</i></b></h2>'))
            return self.editArea.setText('0')

    def result_expression(self, text: str) -> str:
        """Returns the result of the calculation"""
        try:
            self.addSecondLable(text)
            calc_lable = str(self.second_label.text().
                             strip('=').rstrip('-').rstrip('+').rstrip('/').rstrip('*'))
            if calc_lable.count('e') != 0 or len(calc_lable) > 1000 or calc_lable.count('_') != 0:
                raise ValueError
            result = eval(f'{calc_lable}', {})
            self.second_label.clear()
            text = f'Результат виразу {calc_lable} = '
            self.second_label.setText(str(f'<h2><b><i>{text}{result}</i></b></h2>'))
            return self.editArea.setText(str(result))
        except ZeroDivisionError:
            self.second_label.setText(str(f'<h2><b><i>Увага ділення на 0 = 0</i></b></h2>'))
            return self.editArea.setText('0')
        except Exception as e:
            print(e)
            self.second_label.setText(str(f'<h2><b><i>=Неможливо обрахувати результат{calc_lable}</i></b></h2>'))
            return self.editArea.setText('0')

    def result_percent(self) -> str:
        """ Gives the result of processing the percentage button """
        try:
            if str(self.result[-1]) == '':
                calc_lable = '0+'
                calc_line = '0'
            else:
                calc_lable = str(self.result[-1])
                calc_line = str(self.editArea.text())
                self.result.append('=')
            if calc_lable.count('e') > 0:
                raise ValueError
            if calc_lable.count('=') > 0 or len(calc_lable) == 0 or len(calc_line) == 0:
                result = float(calc_line)
                text = f'Неймовірного числа не достатньо = '
                self.second_label.setText(f'<h2><b><i>{text}{result}</i></b></h2>')
                return self.editArea.setText(str(result))
            mark = calc_lable[-1]
            percent_expression = float(calc_lable[:-1]) / 100 * float(calc_line)
            if mark == '+':
                result = float(calc_lable[:-1]) + percent_expression
                self.second_label.clear()
                self.editArea.clear()
                text = f'{calc_lable[:-1]} + {calc_line} % = '
                self.second_label.setText(f'<h2><b><i>{text}{result}</i></b></h2>')
                return self.editArea.setText(str(result))
            elif mark == '-':
                result = float(calc_lable[:-1]) - percent_expression
                self.second_label.clear()
                self.editArea.clear()
                text = f'{calc_lable[:-1]} - {calc_line} % = '
                self.second_label.setText(f'<h2><b><i>{text}{result}</i></b></h2>')
                return self.editArea.setText(str(result))
            elif mark == '/':
                result = float(calc_lable[:-1]) * (100/float(calc_line))
                self.second_label.clear()
                self.editArea.clear()
                text = f'{calc_lable[:-1]} / {calc_line} % = '
                self.second_label.setText(f'<h2><b><i>{text}{result}</i></b></h2>')
                return self.editArea.setText(str(result))
            elif mark == '*':
                result = float(calc_lable[:-1]) / (100/float(calc_line))
                self.second_label.clear()
                self.editArea.clear()
                text = f'{calc_lable[:-1]} * {calc_line} % = '
                self.second_label.setText(f'<h2><b><i>{text}{result}</i></b></h2>')
                return self.editArea.setText(str(result))
        except Exception:
            self.second_label.setText(str(f'<h2><b><i> =Неможливо обрахувати результат{calc_lable}</i></b></h2>'))
            return self.editArea.setText('0')

    def addSecondLable(self, text: str) -> Union[str, None]:
        """ Adds a number and a sign to second_lable """
        if str(self.editArea.text()) == '' == self.second_label.text():
            calc_line = '0'
            calc_lable = ''
            print('1')
        elif not str(self.editArea.text()).isdigit() and len(str(self.editArea.text())) == 0:
            calc_line = ''
            calc_lable = str(self.result[-1][:-1])
        else:
            calc_line = str(self.editArea.text())
            calc_lable = str(self.result[-1])
        if calc_line[-1] == '.':
            calc_line = calc_line + '0'
            self.result.append(f'{calc_lable}{calc_line}{text}')
            self.second_label.setText(str(self.result[-1]))
            return self.editArea.clear()
        elif len(calc_line) > 0 and len(calc_lable) == 0 or calc_lable.count('=') > 0:
            self.result.append(f'{calc_line}{text}')
            self.second_label.setText(str(self.result[-1]))
            return self.editArea.clear()
        else:
            self.result.append(f'{calc_lable}{calc_line}{text}')
            self.second_label.setText(str(self.result[-1]))
            return self.editArea.clear()

    def change_text(self, text: str) -> str:
        """ Adds a button name to the string."""
        return self.editArea.setText(self.editArea.text() + text)

    def positive_negative_number(self) -> str:
        """Changes the sign of the number to positive or negative """
        calc_line = str(self.editArea.text())
        if len(calc_line) == 0:
            return self.editArea.setText(f'-')
        if calc_line[0] == '-':
            return self.editArea.setText(f'{calc_line[1:]}')
        elif calc_line[0] == '+':
            return self.editArea.setText(f'-{calc_line[1 :]}')
        return self.editArea.setText(f'-{calc_line[0:]}')

    def end(self) -> NoReturn:
        """ Cleans result QLabel and QLineEdit and QWidget """
        self.editArea.clear()
        self.second_label.clear()
        self.result = ['']
        self.widget = self.setGeometry(600, 300, 500, 500)


def main_window() -> None:
    """" calculator start function """
    app = QApplication(sys.argv)
    window = MyCalculatorInWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
