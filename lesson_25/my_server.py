import sys
import socket
import math


from functools import partial
from typing import Union, NoReturn

from PyQt5.Qt import Qt

from PyQt5.QtWidgets import (QApplication,
                             QComboBox,
                             QSizePolicy,
                             QWidget,
                             QVBoxLayout,
                             QGridLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel)


class MyServer(QMainWindow):
    def __init__(self, *args, **kwargs):
        """ Creates a server window"""
        super().__init__(*args, **kwargs)
        self.setWindowTitle('MyServer')
        self.widget = QWidget(self.setGeometry(60, 30, 50, 50))
        #  widget = QWidget(self.setFixedSize(550, 550))
        self.first_label = QLabel('<h1><b><i>Мікро сервер</i></b></h1>')
        self.editArea = QLineEdit('')
        self.editArea.setReadOnly(True)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.first_label)
        mainLayout.addWidget(self.editArea)
        self.second_label = QLabel('')
        mainLayout.addWidget(self.second_label)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(('localhost', 65000))
        #self.server_send = self.server_socket.recv(1024)
        buttonLayout = QGridLayout()
        self.button_round = QComboBox()
        mainLayout.addWidget(self.button_round)

        buttons = [
            {
                'name': 'on/off',
                'row': 0,
                'col': 0
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
            if buttonName == 'on/off':
                btn.clicked.connect(partial(self.start_server))

    def start_server(self):
        while True:
            server_send = self.server_socket.recv(1024)
            self.editArea.setText(server_send)
            self.server_socket.close()
            break

def main_window() -> None:
    """" calculator start function """
    app = QApplication(sys.argv)
    window = MyServer()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()

