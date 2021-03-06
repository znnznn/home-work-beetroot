import sys
import requests

from typing import NoReturn, List, Dict
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
        """ Creates a weather window """
        super().__init__(*args, **kwargs)
        self.setWindowTitle('MyWeather')
        self.widget = QWidget(self.setGeometry(600, 600, 100, 100))
        self.first_label = QLabel('<h1><b><i>Виберіть місто / Found city</i></b></h1>')
        self.editArea = QLineEdit('')
        self.main_lable = QLabel('')
        self.editArea.setReadOnly(False)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.first_label)
        mainLayout.addWidget(self.editArea)
        self.second_label = QLabel('')
        mainLayout.addWidget(self.second_label)
        mainLayout.addWidget(self.main_lable)
        self.url = 'http://api.openweathermap.org/data/2.5/weather'
        self.key = '5387623c612af64f83da5b790beef122'

        buttonLayout = QGridLayout()

        btn = QPushButton('Дізнатись погоду')
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        buttonLayout.addWidget(btn)
        mainLayout.addLayout(buttonLayout)
        self.widget.setLayout(mainLayout)
        self.setCentralWidget(self.widget)
        btn.clicked.connect(self.my_weather)

    def my_weather(self) -> NoReturn:
        """" sends a request for weather in the city on the HTTP server  """
        try:
            if self.editArea.text():
                self.second_label.clear()
                self.widget = self.setGeometry(600, 600, 100, 100)
                city = self.editArea.text()
                weather = requests.get(self.url, params={'q': city, 'units': 'metric', 'appid': self.key})
                weather.raise_for_status()
                weather_city = weather.json()
                self.second_label.setText(f"<h4><b><i>{str(weather_city['main']).strip('{}')}</i></b></h4>")
                self.main_lable.setText(f"<h1><b><i>"
                                        f"{str ( weather_city['main']['temp'] )} ℃</i></b></h1>")
            else:
                raise ValueError
        except ValueError:
            self.second_label.setText('<h4><b><i>Оберіть інше місто для прогнозу погоди</i></b></h4>')
        except Exception as e:
            if weather.status_code == 404:
                self.second_label.setText(f'<h4><b><i>Місто {city} не знайдено</i></b></h4>')
            else:
                self.second_label.setText(f'Error: {e}')


def main_window() -> None:
    """" weather request start function """
    app = QApplication(sys.argv)
    window_client = MyClient()
    window_client.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
