import sys
import requests

from functools import partial

from PyQt5.QtWidgets import (QApplication,
                             QSizePolicy,
                             QWidget,
                             QHBoxLayout,
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
        self.setWindowTitle('MyWeather')
        self.widget = QWidget(self.setGeometry(600, 600, 100, 100))
        #self.widget = QWidget(self.setFixedSize(550, 250))
        self.first_label = QLabel('<h1><b><i>Виберіть місто</i></b></h1>')
        self.editArea = QLineEdit('')
        box = QHBoxLayout()
        self.editArea.setReadOnly(False)
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.first_label)
        mainLayout.addWidget(self.editArea)
        self.second_label = QLabel('')
        mainLayout.addWidget(self.second_label)
        self.url = 'http://api.openweathermap.org/data/2.5/weather'
        self.key = '5387623c612af64f83da5b790beef122'


        buttonLayout = QGridLayout()
        buttons = [
            {
                'name': 'Дізнатись погоду',
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
            if buttonName == 'Дізнатись погоду':
                btn.clicked.connect(partial(self.my_weather))

    def my_weather(self):
        """" sends a message to the server  """
        try:
            if self.editArea.text():
                city = self.editArea.text()

                weather = requests.get(self.url, params={'q': city, "units": "metric", 'appid': str(self.key)})
                weather.raise_for_status()
                weather_city = weather.json()
                self.second_label.clear()
                self.second_label.setText(f"<h4><b><i>{str(weather_city['main']).strip('{').strip('}')}</i></b></h4>")
            else:
                raise ValueError
        except ValueError:
            self.second_label.setText('Оберіть інше місто для прогнозу погоди')
        except Exception as e:
            if str(e).count('4') > 1:
                self.second_label.setText(f'Місто {city.capitalize()} не знайдено')
            else:
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



