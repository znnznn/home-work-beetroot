import sys
import math
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel)


class MyCalculatorInWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('C A L C U L A T O R')
        # self.setGeometry(600, 300, 500, 500)
        widget = QWidget(self.setFixedSize(550, 550))
        self.first_label = QLabel('<h1><b><i>Стандартний калькулятор</i></b></h1>')
        self.editArea = QLineEdit('')
        self.editArea.setReadOnly(True)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.first_label)
        mainLayout.addWidget(self.editArea)
        yyy = ''
        self.second_label = QLabel(yyy)
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
            self.buttons[name] = btn
            self.buttons[name].setFixedSize(85, 85)
            buttonLayout.addWidget(btn,
                                   buttonConfig['row'],
                                   buttonConfig['col'],
                                   1,
                                   buttonConfig.get('colSpan', 1))
        mainLayout.addLayout(buttonLayout)
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

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

    def editAreaText_pop(self):  # not used
        """Get display's text del last item."""
        return self.editArea.setText(str(self.editArea.text()[:-1]))

    def editAreaText(self):  # not used
        """Get display's text."""
        return self.editArea.text()

    def second_lable_Text(self, text):  # not used
        """Get display's text."""
        return self.second_label.setText(self.editArea.text() + text)

    def point_only_once(self, text):
        """checks whether a point has been pressed once  """
        calc_line = str(self.editArea.text())
        if len(calc_line) > 0 and calc_line[-1] != text:
            return self.editArea.setText(self.editArea.text() + text)
        elif len(calc_line) == 0:
            return self.editArea.setText('0' + text)
        elif len(calc_line) > 0:
            return self.editArea.setText(calc_line[:-1] + text)

    def result_pow(self):
        calc_line = str(self.editArea.text())
        if len(calc_line) == 0:
            self.second_label.setText('0')
            return self.editArea.setText('0')
        else:
            calc_line = str(self.editArea.text())
            text = f'Квадрат числа {calc_line} = '
        if float(calc_line):
            result = float(calc_line) ** 2
        else:
            result = int(calc_line) ** 2
        self.result.append(f'{text}{result}')
        self.second_label.setText(str(self.result[-1]))
        return self.editArea.setText(str(result))

    def result_root(self):
        calc_line = str(self.editArea.text())
        if len(calc_line) == 0:
            self.second_label.setText('0')
            return self.editArea.setText('0')
        else:
            calc_line = str(self.editArea.text())
            text = f'Квадратний корінь числа {calc_line} = '
        result = float(calc_line) ** 0.5
        self.result.append(f'{text}{result}')
        self.second_label.setText(str(self.result[-1]))
        return self.editArea.setText(str(result))

    def result_factorial(self):
        calc_line = str(self.editArea.text())
        if len(calc_line) == 0:
            self.second_label.setText('0')
            return self.editArea.setText('0')
        digit = math.trunc(float(calc_line))
        text = f'Факторіал числа {digit} = '
        result = math.factorial(digit)
        self.result.append(f'{text}{result}')
        self.second_label.setText(str(self.result[-1]))
        return self.editArea.setText(str(result))

    def result_expression(self, text):
        self.addSecondLable(text)
        calc_lable = str(self.second_label.text().
                         strip('=').rstrip('-').rstrip('+').rstrip('/').rstrip('*'))
        result = eval(f'{calc_lable} + 0')
        self.second_label.clear()
        text = f'Результат виразу {calc_lable} = '
        self.second_label.setText(f'{text}{result}')
        return self.editArea.setText(str(result))

    def result_percent(self):
        """ Gives the result of processing the percentage button """
        if str(self.result[-1]) == '':
            calc_lable = '1+'
            calc_line = '0'
        else:
            calc_lable = str(self.second_label.text())
            calc_line = str(self.editArea.text())
            self.result.append('=')
        if calc_lable.count('=') > 0 or (len(calc_lable) == 0, len(calc_line) == 0):
            result = float(calc_line)
            text = f'Неймовірного числа не достатньо = '
            self.second_label.setText(f'{text}{result}')
            return self.editArea.setText(str(result))
        mark = calc_lable[-1]
        percent_expression = float(calc_lable[:-1]) / 100 * float(calc_line)
        if mark == '+':
            result = float(calc_lable[:-1]) + percent_expression
            self.second_label.clear()
            self.editArea.clear()
            text = f'{calc_lable[:-1]} + {calc_line} % = '
            self.second_label.setText(f'{text}{result}')
            return self.editArea.setText(str(result))
        elif mark == '-':
            result = float(calc_lable[:-1]) - percent_expression
            self.second_label.clear()
            self.editArea.clear()
            text = f'{calc_lable[:-1]} - {calc_line} % = '
            self.second_label.setText(f'{text}{result}')
            return self.editArea.setText(str(result))
        elif mark == '/':
            result = float(calc_lable[:-1]) * (100/float(calc_line))
            self.second_label.clear()
            self.editArea.clear()
            text = f'{calc_lable[:-1]} / {calc_line} % = '
            self.second_label.setText(f'{text}{result}')
            return self.editArea.setText(str(result))
        elif mark == '*':
            result = float(calc_lable[:-1]) / (100/float(calc_line))
            self.second_label.clear()
            self.editArea.clear()
            text = f'{calc_lable[:-1]} * {calc_line} % = '
            self.second_label.setText(f'{text}{result}')
            return self.editArea.setText(str(result))

    def addSecondLable(self, text):
        """" Adds a number and a sign to second_lable """
        calc_line = str(self.editArea.text())
        calc_lable = str(self.result[-1])
        if len(calc_line) > 0 and len(calc_lable) == 0 or calc_lable.count('=') > 0:
            self.result.append(f'{calc_line}{text}')
            self.second_label.setText(str(self.result[-1]))
            return self.editArea.clear()
        else:
            self.result.append(f'{calc_lable}{calc_line}{text}')
            self.second_label.setText(str(self.result[-1]))
            return self.editArea.clear()

    def addSecondLable1(self, text):  # not used
        """" Adds a number and a sign to second_lable """
        calc_line = str(self.editArea.text())
        calc_lable = str(self.second_label.text())
        if len(calc_line) > 0 and len(calc_lable) == 0:
            self.second_label.setText(calc_line + text)
            return self.editArea.clear()
        else:
            self.second_label.setText(calc_lable + calc_line + text)
            return self.editArea.clear()

    def change_text(self, text):
        """ Adds a button name to the string."""
        return self.editArea.setText(self.editArea.text() + text)

    def positive_negative_number(self):
        """changes the sign of the number to positive or negative"""
        calc_line = str(self.editArea.text())
        if calc_line[0] == '-':
            return self.editArea.setText(f'{calc_line[1:]}')
        elif calc_line[0] == '+':
            return self.editArea.setText(f'-{calc_line[1 :]}')
        return self.editArea.setText(f'-{calc_line[0:]}')

    def end(self):
        """ Cleans result QLabel and QLineEdit """
        self.result = ['']
        self.second_label.clear()
        return self.editArea.clear()


def main_window():
    app = QApplication(sys.argv)
    window = MyCalculatorInWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
