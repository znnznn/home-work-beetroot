import sys
import socket

from typing import Union, NoReturn
from functools import partial

from PyQt5.QtWidgets import (QApplication,
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
        self.server_socket.bind(('127.0.0.1', 65000))

        buttonLayout = QGridLayout()
        btn = QPushButton('receiving messages')
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        buttonLayout.addWidget(btn)
        mainLayout.addLayout(buttonLayout)
        self.widget.setLayout(mainLayout)
        self.setCentralWidget(self.widget)
        btn.clicked.connect(self.start_server)

    def start_server(self) -> NoReturn:
        """ receives messages from the client """
        try:
            while True:
                server_send = (self.server_socket.recv(1024)).decode('utf-8')
                self.editArea.setText(server_send)
                break
        except Exception as e:
            self.second_label.setText(f'Error : {e}')


def main_window() -> None:
    """" calculator start function """
    app = QApplication(sys.argv)
    window = MyServer()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
