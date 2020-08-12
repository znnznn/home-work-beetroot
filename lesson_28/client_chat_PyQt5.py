import asyncio
import sys


from functools import partial
from quamash import QEventLoop
from PyQt5.QtWidgets import (QApplication,
                             QSizePolicy,
                             QTextEdit,
                             QWidget,
                             QVBoxLayout,
                             QGridLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel)


class MyClient(QMainWindow):
    def __init__(self, loop, *args, **kwargs):
        """ Creates a server window """
        super().__init__(*args, **kwargs)
        self.setWindowTitle('MyClient')
        self.widget = QWidget(self.setGeometry(60, 30, 50, 50))

        self.first_label = QLabel('<h2><b><i>Мікро чат</i></b></h2>')
        self.editArea = QLineEdit('')
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.first_label)

        self.loop = loop
        self.msg = None

        chat_send = QGridLayout()
        chat_send.setSpacing(2)
        chat = QGridLayout()
        chat.setSpacing(25)
        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        btn = QPushButton('send')
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        chat.addWidget(self.chat, 1, 24)
        chat_send.addWidget(btn, 25, 1)
        chat_send.addWidget(self.editArea, 25, 0)
        mainLayout.addLayout(chat)
        mainLayout.addLayout(chat_send)
        self.widget.setLayout(mainLayout)
        self.setCentralWidget(self.widget)
        btn.clicked.connect(partial(self.my_client))

    def my_client(self):
        """" sends a message to the server  """
        try:
            self.msg = self.editArea.text()
            self.editArea.clear()

        except Exception as e:
            self.second_label.setText(f'Error: {e}')


class ClientChat(asyncio.Protocol, MyClient):
    def __init__(self, loop, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop = loop
        self.message = None
        self.transport = None

    def connection_made(self, transport):
        self.message = self.msg
        self.transport = transport
        self.transport.write(self.message.encode())
        print(f'Data sent: {self.message}')

    def data_received(self, data):

        text = data.decode()
        self.chat.setText(text)
        print(f'Data received: {text}')

    def connection_lost(self, exc):
        self.chat.setText('The server closed the connection')


class App(QApplication):
    def __init__(self):
        QApplication.__init__(self, sys.argv)
        self.loop = QEventLoop(self)
        asyncio.set_event_loop(self.loop)

        self.client = ClientChat(self.loop, self.loop)
        self.loop.create_task(self.start())

        self.gui = MyClient(self.loop)
        self.gui.show()
        self.loop.run_forever()

    async def start(self):
        connection = self.loop.create_connection(lambda: self.client, '127.0.0.1', 8888)
        await asyncio.wait_for(connection, 10000)


def main_window() -> None:
    App()


if __name__ == '__main__':
    main_window()




