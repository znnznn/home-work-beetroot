import sys
import socket

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


class MyClient(QMainWindow):
    def __init__(self, *args, **kwargs):
        """ Creates a server window """
        super().__init__(*args, **kwargs)
        self.setWindowTitle('MyClient')
        self.widget = QWidget(self.setGeometry(60, 30, 50, 50))
        #  widget = QWidget(self.setFixedSize(550, 550))
        self.first_label = QLabel('<h1><b><i>Мікро клієнт</i></b></h1>')
        self.editArea = QLineEdit('')
        self.editArea.setReadOnly(False)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.first_label)
        mainLayout.addWidget(self.editArea)
        self.second_label = QLabel('')
        mainLayout.addWidget(self.second_label)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.connect(('127.0.0.1', 65000))

        buttonLayout = QGridLayout()
        buttons = [
            {
                'name': 'send',
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
            if buttonName == 'send':
                btn.clicked.connect(partial(self.my_client))

    def my_client(self):
        """" sends a message to the server  """
        try:
            send_client = self.editArea.text()
            self.client_socket.sendall(bytes(send_client, encoding='utf-8'))
            self.second_label.setText(self.editArea.text())
            self.editArea.clear()
        except Exception as e:
            self.second_label.setText(f'Error: {e}')


def main_window() -> None:
    """" client start function """
    app = QApplication(sys.argv)
    window_client = MyClient()
    window_client.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()



