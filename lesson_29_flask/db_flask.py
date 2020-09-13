import psycopg2
import datetime

from psycopg2.extras import RealDictCursor


class DataBase:
    #  work with the database
    def __init__(self, user: dict):
        self.connection = None
        self.cursor = None
        self.user = user
        self.data_base()

    def data_base(self):
        """ connection to the database """
        try:
            self.connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                               user='postgres', password='postgres')
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        except:
            self.cursor.close()

    def take_user(self):
        """ takes data from database by email """
        try:
            self.cursor.execute("SELECT * FROM users WHERE email = %s", (f"{self.user['email']}",))
            user = self.cursor.fetchone()
            if user:
                self.cursor.close()
                self.connection.commit()
                return dict(user)
            self.cursor.close()
            self.connection.commit()
            return False
        except Exception as e:
            self.cursor.close()
            self.connection.commit()
            print(e, 'take_user')
            return False

    def take_user_id(self):
        """ takes data from database by id(integer)  (used for Userlogin.UserMixin)"""
        try:
            self.cursor.execute(f"SELECT * FROM users WHERE id = {self.user};")
            user = self.cursor.fetchone()
            if user:
                self.cursor.close()
                self.connection.commit()
                return dict(user)
            self.cursor.close()
            self.connection.commit()
            return False
        except Exception as e:
            self.cursor.close()
            self.connection.commit()
            print(e, 'take_user_id')
            return False

    def edit_user(self):
        """ changes the data in the database by id """
        try:
            self.data_base()
            self.cursor.execute("""UPDATE users 
                                        SET first_name=%s, last_name=%s,
                                            username=%s, password=%s, 
                                            email=%s, address=%s  WHERE id=%s;""", (f"{self.user['firstName']}",
                                                                                    f"{self.user['lastName']}",
                                                                                    f"{self.user['username']}",
                                                                                    f"{self.user['password']}",
                                                                                    f"{self.user['email']}",
                                                                                    f"{self.user['address']}",
                                                                                    f"{self.user['id']}"))

            self.cursor.close()
            self.connection.commit()
            return True
        except Exception as e:
            print(e, 'edit_user')
            self.user['Error'] = e
            self.cursor.close()
            self.connection.commit()

    def del_user(self):
        """ deletes user data in the database (delete profile) """
        try:
            sql = f""" DROP TABLE "{self.user['email']}";"""
            self.cursor.execute("""DELETE FROM users WHERE id = %s;""", (f"{self.user['id']}",))
            self.cursor.execute(sql)
            self.cursor.close()
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            self.user['Error'] = e
            return False

    def add_user(self):
        """ adds the user to the database after registration """
        if self.take_user():
            return False
        self.data_base()
        try:
            self.create_tab()
            self.data_base()
            self.cursor.execute(f"""INSERT INTO users(FIRST_NAME, LAST_NAME, USERNAME,
                                PASSWORD, EMAIL, ADDRESS, oper_date)
                                VALUES(%s, %s, %s, %s, %s, %s, %s);""", (f"{self.user['firstName']}",
                                                                         f"{self.user['firstName']}",
                                                                         f"{self.user['username']}",
                                                                         f"{self.user['password']}",
                                                                         f"{self.user['email']}",
                                                                         f"{self.user['address']}",
                                                                         f"{self.user['date']}"))
            self.cursor.close()
            self.connection.commit()
            return True
        except Exception as e:
            print(e, 'add_user')
            self.connection.rollback()
            self.user['Error'] = e
            return False

    def del_user_views(self):
        """ deletes the data on which the user conducts analytics """
        try:
            sql = f"""DELETE FROM "{self.user['email']}" WHERE ID={self.user['stock']['id']} """
            self.cursor.execute(sql)

            self.user['stock']['symbol'] = 'profit'
            self.user['stock']['prevclose'] = self.user['stock']['profit']
            self.user['stock']['trade_date'] = f'від {self.user["stock"]["trade_date"]} до {datetime.datetime.today()}'
            user = self.add_user_views()
            self.cursor.close()
            self.connection.commit()
            return True
        except Exception as e:
            print(e, 'del_user_views')
            self.connection.rollback()
            self.user['Error'] = e
            return False

    def add_user_views(self):
        """ adds the data on which the user conducts analytics """
        user = self.take_user()
        self.data_base()
        try:
            if user:
                sql = f"""INSERT INTO "{self.user['email']}"
                                                   (symbol, description, exch, type, open, high, low, bid, ask,
                                                    change_percentage, prevclose, week_52_high, week_52_low, trade_date)
                                                    VALUES('{self.user['stock']['symbol']}',
                                                           '{self.user['stock']['description']}',
                                                           '{self.user['stock']['exch']}',
                                                           '{self.user['stock']['type']}',
                                                           {self.user['stock']['open']},
                                                           {self.user['stock']['high']},
                                                           {self.user['stock']['low']},
                                                           {self.user['stock']['bid']},
                                                           {self.user['stock']['ask']},
                                                           {self.user['stock']['change_percentage']}, 
                                                           {self.user['stock']['prevclose']},
                                                           {self.user['stock']['week_52_high']},
                                                           {self.user['stock']['week_52_low']},
                                                           '{self.user['stock']['trade_date']}');"""
                self.cursor.execute(sql)
                self.cursor.close()
                self.connection.commit()
                return user
        except Exception as e:
            print(e, 'add_user_views')
            self.connection.rollback()
            self.user['Error'] = e
            return False

    def take_user_views(self):
        """ takes data on which the user conducts analytics """
        self.data_base()
        try:
            sql = f"""SELECT * FROM "{self.user['email']}" where not symbol ='profit';"""
            self.cursor.execute(sql)

            user = self.cursor.fetchall()
            stock = [dict(s) for s in user]
            if user:
                self.cursor.close()
                self.connection.commit()
                return stock
            self.cursor.close()
            self.connection.commit()
            return False
        except Exception as e:
            self.cursor.close()
            self.connection.commit()
            self.user['Error'] = e
            print('take_user_views', e)
            return False

    def take_user_views_symbol(self):
        """ checks for stock in the database """
        self.data_base()
        try:
            sql = f"""SELECT * FROM "{self.user['email']}" WHERE symbol='{self.user['stock']['symbol']}';"""
            self.cursor.execute(sql)

            user = self.cursor.fetchall()
            if user:
                self.cursor.close()
                self.connection.commit()
                return True
            self.cursor.close()
            self.connection.commit()
            return False
        except Exception as e:
            self.cursor.close()
            self.connection.commit()
            self.user['Error'] = e
            print('take_user_views_symbol', e)
            return False

    def take_user_profit(self):
        """ takes data about all profit """
        self.data_base()
        try:
            sql = f"""SELECT * FROM "{self.user['email']}" WHERE symbol='profit';"""
            self.cursor.execute(sql)

            user = self.cursor.fetchall()
            list_profit = [dict(s) for s in user]
            if user:
                self.cursor.close()
                self.connection.commit()
                return list_profit
            self.cursor.close()
            self.connection.commit()
            return False
        except Exception as e:
            self.cursor.close()
            self.connection.commit()
            self.user['Error'] = e
            print('take_user_views_symbol', e)
            return False

    def create_tab(self):
        """ creating a table of users and a table of wishes of users """
        try:
            sql = f"""CREATE TABLE IF NOT EXISTS "{self.user['email']}"( ID serial PRIMARY KEY NOT NULL,
                                                                          symbol VARCHAR(500) NOT NULL,
                                                                          description text NOT NULL,
                                                                          exch VARCHAR(70) NOT NULL,
                                                                          type VARCHAR(70) NOT NULL,
                                                                          open double precision NOT NULL,
                                                                          high double precision NOT NULL,
                                                                          low double precision NOT NULL,
                                                                          bid double precision NOT NULL,
                                                                          ask double precision NOT NULL,
                                                                          change_percentage double precision NOT NULL,
                                                                          prevclose double precision NOT NULL,
                                                                          week_52_high double precision NOT NULL,
                                                                          week_52_low double precision NOT NULL,
                                                                          trade_date VARCHAR(500) NOT NULL                                           
                                                                          );"""
            self.cursor.execute(sql)
            self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS users (
                                                  ID serial PRIMARY KEY NOT NULL,
                                                  FIRST_NAME VARCHAR(500) NOT NULL,
                                                  LAST_NAME VARCHAR(500) NOT NULL,
                                                  USERNAME VARCHAR (500) NOT NULL,
                                                  PASSWORD VARCHAR NOT NULL,
                                                  EMAIL VARCHAR (500) NOT NULL,
                                                  ADDRESS VARCHAR(500) NOT NULL,
                                                  oper_date VARCHAR(500) NOT NULL                                          
                                                  );""")
            self.cursor.close()
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            self.user['Error'] = e
            return print(f'Помилка з\'єднання з базою даних : {e}')

    def add_message(self):
        """ adds sent user messages to the database """
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS message (
                                                              ID serial PRIMARY KEY NOT NULL,                                                              
                                                              USERNAME VARCHAR (500) NOT NULL,                                                              
                                                              EMAIL VARCHAR (500) NOT NULL,
                                                              message text NOT NULL,
                                                              oper_date VARCHAR(500) NOT NULL                                          
                                                              );""")
            self.cursor.execute("""INSERT INTO message(USERNAME, EMAIL, message, oper_date)
                                VALUES(%s, %s, %s, %s);""", ( f"{self.user['username']}",
                                                              f"{self.user['email']}",
                                                              f"{self.user['message']}",
                                                              f"{self.user['date']}",))
            self.cursor.close()
            self.connection.commit()
            return True
        except Exception as e:
            print(e, 'add_message')
            self.connection.rollback()
            self.user['Error'] = e
            return False
