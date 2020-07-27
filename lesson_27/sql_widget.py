import sys
from functools import partial
import psycopg2

from typing import NoReturn

from PyQt5.QtWidgets import (QApplication,
                             QTextEdit,
                             QTabWidget,
                             QWidget,
                             QVBoxLayout,
                             QGridLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel,)


""" I create tables on the basis of which I will work """

connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres', password='postgres')
cursor = connection.cursor()
try:

    cursor.execute("""CREATE TABLE parties (
                          ID serial,
                          name VARCHAR(20) PRIMARY KEY NOT NULL                                            
                          );""")
    cursor.execute("""CREATE TABLE districts(
                          ID serial,
                          name VARCHAR(20) PRIMARY KEY NOT NULL                                                 
                          );""")
    cursor.execute("""CREATE TABLE candidates(
                          ID serial,
                          name VARCHAR(20) PRIMARY KEY NOT NULL,
                          parties_name VARCHAR(20), FOREIGN KEY (parties_name) REFERENCES parties(name),
                          districts_name VARCHAR(20), FOREIGN KEY (districts_name) REFERENCES districts(name)                   
                          );""")
    cursor.execute("""CREATE TABLE electorates(
                              ID serial PRIMARY KEY,
                              name VARCHAR(20) NOT NULL,
                              parties_name VARCHAR(20), FOREIGN KEY (parties_name) REFERENCES parties(name),
                              districts_name VARCHAR(20), FOREIGN KEY (districts_name) REFERENCES districts(name),
                              candidates_name VARCHAR(20), FOREIGN KEY (candidates_name) REFERENCES candidates(name)                   
                              );""")
    cursor.execute("INSERT INTO parties(name) VALUES('Безпартійний');")
    cursor.execute("INSERT INTO parties(name) VALUES('Не голосував');")

    cursor.close()
    connection.commit()
except Exception as e:
    print(e)
    if 'relation' in str(e):
        print('вже створена')
    connection.rollback()


class MyAgentFootball(QMainWindow):
    def __init__(self, *args, **kwargs):
        """ Creates a weather window """
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Database Voice 2020')
        self.widget = QWidget(self.setGeometry(600, 600, 400, 300))
        self.first_label = QLabel('<h1><b><i>Cool Voice</i></b></h1>')
        self.loyaut = QVBoxLayout()
        self.tabs = QTabWidget()

        self.tab_parties = QWidget()
        self.tab_electorates = QWidget()
        self.tab_districts = QWidget()
        self.tab_candidates = QWidget()

        self.tabs.addTab(self.tab_parties, 'Партії')
        self.tabs.addTab(self.tab_electorates, 'Виборці')
        self.tabs.addTab(self.tab_districts, 'Округи')
        self.tabs.addTab(self.tab_candidates, 'Кандидати')

        self.buttons = ["Записати", "Видалити", "Знайти данні"]

        self.parties = QGridLayout()
        self.parties.setSpacing(8)
        name = QLabel('Name')
        self.parties_line = QLineEdit('')
        self.parties_text = QTextEdit()
        self.parties.addWidget(name, 1, 0)
        self.parties.addWidget(self.parties_line, 1, 1)
        self.tab_parties.setLayout(self.parties)
        self.pushButton_parties = QPushButton("Записати")
        self.pushButton_parties1 = QPushButton("Видалити")
        self.pushButton_parties2 = QPushButton("Знайти данні")
        self.parties.addWidget(self.pushButton_parties, 2, 1)
        self.parties.addWidget(self.pushButton_parties1, 3, 1)
        self.parties.addWidget(self.pushButton_parties2, 4, 1)
        self.parties.addWidget(self.parties_text, 5, 1, 8, 1)
        self.pushButton_parties.clicked.connect(partial(self.records, 'parties'))
        self.pushButton_parties1.clicked.connect(partial(self.deletes, 'parties'))
        self.pushButton_parties2.clicked.connect(partial(self.data_search, 'parties'))

        self.setCentralWidget(self.tabs)
        self.setCentralWidget(self.tabs)
        self.electorates = QGridLayout()
        self.electorates.setSpacing(8)
        name = QLabel('Name')
        self.electorates_line = QLineEdit('')
        self.electorates_text = QTextEdit()
        self.electorates.addWidget(name, 1, 0)
        self.electorates.addWidget(self.electorates_line, 1, 1)
        self.tab_electorates.setLayout(self.electorates)
        self.pushButton_electorates = QPushButton("Записати")
        self.pushButton_electorates1 = QPushButton("Видалити")
        self.pushButton_electorates2 = QPushButton("Знайти данні")
        self.electorates.addWidget(self.pushButton_electorates, 2, 1)
        self.electorates.addWidget(self.pushButton_electorates1, 3, 1)
        self.electorates.addWidget(self.pushButton_electorates2, 4, 1)
        self.electorates.addWidget(self.electorates_text, 5, 1, 8, 1)
        self.pushButton_electorates.clicked.connect(partial(self.records, 'electorates'))
        self.pushButton_electorates1.clicked.connect(partial(self.deletes, 'electorates'))
        self.pushButton_electorates2.clicked.connect(partial(self.data_search, 'electorates'))

        self.districts = QGridLayout()
        self.districts.setSpacing(8)
        name = QLabel('Name')
        self.districts_line = QLineEdit('')
        self.districts_text = QTextEdit()
        self.districts.addWidget(name, 1, 0)
        self.districts.addWidget(self.districts_line, 1, 1)
        self.tab_districts.setLayout(self.districts)
        self.pushButton_districts = QPushButton("Записати")
        self.pushButton_districts1 = QPushButton("Видалити")
        self.pushButton_districts2 = QPushButton("Знайти данні")
        self.districts.addWidget(self.pushButton_districts, 2, 1)
        self.districts.addWidget(self.pushButton_districts1, 3, 1)
        self.districts.addWidget(self.pushButton_districts2, 4, 1)
        self.districts.addWidget(self.districts_text, 5, 1, 8, 1)
        self.pushButton_districts.clicked.connect(partial(self.records, 'districts'))
        self.pushButton_districts1.clicked.connect(partial(self.deletes, 'districts'))
        self.pushButton_districts2.clicked.connect(partial(self.data_search, 'districts'))

        self.candidates = QGridLayout()
        self.candidates.setSpacing(8)
        name = QLabel('Name')
        self.candidates_line = QLineEdit('')
        self.candidates_text = QTextEdit()
        self.candidates.addWidget(name, 1, 0)
        self.candidates.addWidget(self.candidates_line, 1, 1)
        self.tab_candidates.setLayout(self.candidates)
        self.pushButton_candidates = QPushButton("Записати")
        self.pushButton_candidates1 = QPushButton("Видалити")
        self.pushButton_candidates2 = QPushButton("Знайти данні")
        self.candidates.addWidget(self.pushButton_candidates, 2, 1)
        self.candidates.addWidget(self.pushButton_candidates1, 3, 1)
        self.candidates.addWidget(self.pushButton_candidates2, 4, 1)
        self.candidates.addWidget(self.candidates_text, 5, 1, 8, 1)
        self.pushButton_candidates.clicked.connect(partial(self.records, 'candidates'))
        self.pushButton_candidates1.clicked.connect(partial(self.deletes, 'candidates'))
        self.pushButton_candidates2.clicked.connect(partial(self.data_search, 'candidates'))

        self.loyaut.addWidget(self.tabs)
        self.widget.setLayout(self.loyaut)
        self.setCentralWidget(self.tabs)

        self.cursor = True
        self.connection = True

    def set_error(self, name_tab: str, error: str) -> NoReturn:
        if name_tab == 'parties':
            self.parties_text.setText(error)
        elif name_tab == 'electorates':
            self.electorates_text.setText(error)
        elif name_tab == 'districts':
            self.districts_text.setText(error)
        elif name_tab == 'candidates':
            self.candidates_text.setText(error)

    def my_connection(self, name_tab: str) -> NoReturn:
        try:
            self.connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                               user='postgres', password='postgres')
            self.cursor = self.connection.cursor()
        except Exception as error:
            self.set_error(name_tab, str(error))

    def reads_line(self, name_tab: str) -> str:
        """ reads input data """
        values_data = False
        try:
            if name_tab == 'parties':
                values_data = self.parties_line.text()
            elif name_tab == 'electorates':
                values_data = self.electorates_line.text()
            elif name_tab == 'districts':
                values_data = self.districts_line.text()
            elif name_tab == 'candidates':
                values_data = self.candidates_line.text()
            return values_data
        except Exception as error:
            self.set_error(name_tab, str(error))

    def records(self, name_tab: str) -> NoReturn:
        """ writes the entered data to the database """
        self.my_connection(name_tab)
        values_data = self.reads_line(name_tab)
        if values_data:
            if name_tab == 'parties' or name_tab == 'districts':
                try:
                    self.cursor.execute(f"INSERT INTO {name_tab}(name) VALUES('{values_data}');")
                    self.cursor.close()
                    self.connection.commit()
                    self.set_error(name_tab, f'name\n{values_data} додано в базу даних')
                    return
                except Exception as error:
                    self.set_error(name_tab, str(error))
                    self.connection.rollback()
                finally:
                    self.cursor.close()
            else:
                values_foreign_parties = self.reads_line('parties')
                values_foreign_districts = self.reads_line('districts')
                if not values_foreign_districts:
                    self.set_error(name_tab, 'Введіть округ')
                    return
                if name_tab == 'candidates':
                    if not values_foreign_parties:
                        self.parties_line.setText('Безпартійний')
                elif name_tab == 'electorates':
                    if not values_foreign_parties:
                        self.parties_line.setText('Не голосував')
                values_foreign_parties = self.reads_line('parties')
                values_foreign_districts = self.reads_line('districts')
                try:
                    self.cursor.execute(f"INSERT INTO {name_tab}(name, parties_name, districts_name)"
                                        f"values('{values_data}', '{values_foreign_parties}', '{values_foreign_districts}');"
                                        )
                    self.cursor.close()
                    self.connection.commit()
                    self.set_error(name_tab, f'(name, parties_name, districts_name)\n'
                                             f'{values_data}, {values_foreign_parties}, {values_foreign_districts}'
                                             f' додано в базу даних')
                    return
                except Exception as error:
                    self.set_error(name_tab, str(error))
                    self.connection.rollback()
                finally:
                    self.cursor.close()
        else:
            self.set_error(name_tab, 'Ви не ввели данні')
            return

    def deletes(self, name_tab: str) -> NoReturn:
        """ deletes the entered data in the database """
        self.my_connection(name_tab)
        values_data = self.reads_line(name_tab)
        if values_data:
            try:
                self.cursor.execute(f"DELETE FROM {name_tab} WHERE(name='{values_data}');")
                self.cursor.close()
                self.connection.commit()
                self.set_error(name_tab, f'{values_data} з бази данних видалено')
            except Exception as error:
                self.set_error(name_tab, str(error))
                self.connection.rollback()
            finally:
                self.cursor.close()
        else:
            self.set_error(name_tab, 'Ви не ввели данні')
            return

    def data_search(self, name_tab: str) -> NoReturn:
        """ searches for entered data in the database """
        self.my_connection(name_tab)
        values_data = self.reads_line(name_tab)
        if values_data:
            if name_tab == 'parties' or name_tab == 'districts':
                try:
                    self.cursor.execute(f"SELECT * from {name_tab} where name='{values_data}'")
                    self.set_error(name_tab, f'{self.cursor.fetchall()}')

                    self.cursor.close()
                    self.connection.commit()
                except Exception as error:
                    self.set_error(name_tab, str(error))
                    self.connection.rollback()
                finally:
                    self.cursor.close()
            else:
                try:
                    self.cursor.execute(f"SELECT * "
                                        f"FROM '{name_tab}' "
                                        f"INNER JOIN parties ON ({name_tab}.parties_name = parties.name) "
                                        f"WHERE {name_tab}.name={values_data}")
                    self.set_error(name_tab, f'{self.cursor.fetchall()}')
                    self.cursor.close()
                    self.connection.commit()
                except Exception as error:
                    self.set_error(name_tab, str(error))
                    self.connection.rollback()
                finally:
                    self.cursor.close()
        else:
            self.set_error(name_tab, 'Ви не ввели данні')
            return


def main_window() -> None:
    """" weather request start function """
    app = QApplication(sys.argv)
    window_client = MyAgentFootball()
    window_client.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
