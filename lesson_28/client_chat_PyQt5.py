import asyncio
import sys
import threading

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
        self.loop = None

        buttonLayout = QGridLayout()
        btn = QPushButton('send')
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        buttonLayout.addWidget(btn)
        mainLayout.addLayout(buttonLayout)
        self.widget.setLayout(mainLayout)
        self.setCentralWidget(self.widget)
        btn.clicked.connect(partial(self.my_client))

    def my_client(self):
        """" sends a message to the server  """
        try:
            send_client = self.editArea.text()
            self.editArea.clear()
            asyncio.run(self.main(send_client))
        except Exception as e:
            self.second_label.setText(f'Error: {e}')

    async def main(self, text):
        self.loop = asyncio.get_running_loop()

        on_con_lost = self.loop.create_future()
        message = text

        transport, protocol = await self.loop.create_connection(
            lambda: ClientChat(message, on_con_lost),
            '127.0.0.1', 8888)
        try:
            await on_con_lost
        finally:
            transport.close()


class ClientChat(asyncio.Protocol, MyClient):
    def __init__(self, message, on_con_lost, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):

        transport.write(self.message.encode())
        print(f'Data sent: {self.message}')

    def data_received(self, data):

        text = data.decode()

        self.second_label.setText(text)
        print(f'Data received: {text}')

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)


def main_window() -> None:
    """" client start function """
    app = QApplication(sys.argv)
    window_client = MyClient()
    window_client.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()




