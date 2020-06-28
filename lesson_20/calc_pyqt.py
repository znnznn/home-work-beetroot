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
                btn.clicked.connect(partial(self.point_not_once, buttonName))
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


    def editAreaText_pop(self):
        """Get display's text del last item."""
        return self.editArea.setText(str(self.editArea.text()[:-1]))

    def editAreaText(self):
        """Get display's text."""
        return self.editArea.text()

    def second_lable_Text(self, text):
        """Get display's text."""
        return self.second_label.setText(self.editArea.text() + text)

    def point_not_once(self, text):
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
        text = f'Квадрат числа {calc_line} = '
        result = calc_line
        if int(calc_line):
            result = int(calc_line) ** 2
        elif float(calc_line):
            result = float(calc_line) ** 2
        self.second_label.setText(f'{text}{result}')
        return self.editArea.clear()

    def result_root(self):
        calc_line = str(self.editArea.text())
        text = f'Квадратний корінь числа {calc_line} = '
        result = float(calc_line) ** 0.5
        self.second_label.setText(f'{text}{result}')
        return self.editArea.clear()

    def result_factorial(self):
        calc_line = str(self.editArea.text())
        digit = math.trunc(float(calc_line))
        text = f'Факторіал числа {digit} = '
        result = math.factorial(digit)
        self.second_label.setText(f'{text}{result}')
        return self.editArea.clear()

    def result_expression(self, text):
        self.addSecondLable(text)
        calc_lable = str(self.second_label.text())
        result = eval(calc_lable[:-1])
        self.second_label.clear()
        text = f'Результат виразу {calc_lable} '
        self.second_label.setText(f'{text}{result}')
        return self.editArea.setText(str(result))

    def addSecondLable(self, text):
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
            return self.editArea.setText(f'+{calc_line[1:]}')
        elif calc_line[0] == '+':
            return self.editArea.setText(f'-{calc_line[1 :]}')
        return self.editArea.setText(f'-{calc_line[0:]}')

    def end(self):
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
