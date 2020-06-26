import sys
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
        self.setGeometry(600, 300, 500, 500)
        widget = QWidget()
        first_label = QLabel('<h1><b><i>Стандартний калькулятор</i></b></h1>')
        self.editArea = QLineEdit('')
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(first_label)
        mainLayout.addWidget(self.editArea)

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
                'name': '+/-',
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
                'name': '00',
                'row': 3,
                'col': 4
            }
        ]
        self.buttons = {}
        for buttonConfig in buttons:
            name = buttonConfig.get('name', '')
            btn = QPushButton(name)
            self.buttons[name] = btn
            buttonLayout.addWidget(btn,
                                   buttonConfig['row'],
                                   buttonConfig['col'],
                                   1,
                                   buttonConfig.get('colSpan', 1))
        mainLayout.addLayout(buttonLayout)
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        for buttonName in self.buttons :
            btn = self.buttons[buttonName]
            if buttonName == '=':
                btn.clicked.connect(self.end)
            else :
                btn.clicked.connect(partial(self.change_text, buttonName))
                first_label = buttonName

    def change_text(self, text):
        self.editArea.setText(self.editArea.text() + text)

    def end(self):
        
        self.editArea.setText('')


def main_window():
    app = QApplication(sys.argv)
    window = MyCalculatorInWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
