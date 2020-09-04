import psycopg2

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
            print('take_user', self.user['email'])
            self.cursor.execute("SELECT * FROM users WHERE email = %s", (f"{self.user['email']}",))
            user = self.cursor.fetchone()
            print('take_user', dict(user))
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
            print('tas', self.user)
            self.cursor.execute(f"SELECT * FROM users WHERE id = {self.user};")
            print('oops')
            user = self.cursor.fetchone()
            print(dict(user))
            if user:
                self.cursor.close()
                self.connection.commit()
                return dict(user)
            print('sad')
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
            self.cursor.close()
            self.connection.commit()

    def del_user(self):
        """ deletes user data in the database (delete profile) """
        try:
            print(5)
            self.cursor.execute("""DELETE FROM users WHERE id = %s;""", (f"{self.user['id']}",))
            self.cursor.close()
            self.connection.commit()
            return True
        except Exception as e:
            print(e, 'add_user')
            self.connection.rollback()
            self.user['None'] = e
            return False

    def add_user(self):
        """ adds the user to the database after registration """
        if self.take_user():
            return False
        self.data_base()
        try:
            self.create_tab()
            self.data_base()
            print(5)
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
            self.user['None'] = e
            return False

    def edit_user_views(self):
        """ changes the data on which the user conducts analytics """
        try:
            user = self.take_user()
            user_id = user['id']
            self.cursor.execute(f"SELECT * FROM {user_id}")
            user = self.cursor.fetchall()
            print(user)
            if user:
                return user

            return False
        except Exception as e:
            print(e, 'take_user')
            return False

    def del_user_views(self):
        """ deletes the data on which the user conducts analytics """
        pass

    def add_user_views(self):
        """ adds the data on which the user conducts analytics """
        user = self.take_user()
        if user:
            print(user)
            sql = f"""CREATE TABLE IF NOT EXISTS {self.user['email']}( ID serial PRIMARY KEY NOT NULL,
                                                                  STOCK_NAME VARCHAR(500) NOT NULL,
                                                                  STICKER_STOCK VARCHAR(500) NOT NULL,
                                                                  BID integer NOT NULL,
                                                                  ASK integer NOT NULL,
                                                                  oper_date VARCHAR(500) NOT NULL                                           
                                                                  );"""
            self.cursor.execute(sql)
            self.cursor.close()
            self.connection.commit()
            return True

    def take_user_views(self):
        """ takes data on which the user conducts analytics """
        pass

    def create_tab(self):
        """ creating a table of users and a table of wishes of users """
        try:
            sql = f"""CREATE TABLE IF NOT EXISTS "{self.user['email']}"( ID serial PRIMARY KEY NOT NULL,
                                                                              STOCK_NAME VARCHAR(500) NOT NULL,
                                                                              STICKER_STOCK VARCHAR(500) NOT NULL,
                                                                              BID integer NOT NULL,
                                                                              ASK integer NOT NULL,
                                                                              oper_date VARCHAR(500) NOT NULL                                           
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
            return print(f'Помилка з\'єднання з базою даних : {e}')

    def add_message(self):
        """ adds sent user messages to the database """
        try:
            print(5)
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
            self.user['None'] = e
            return False



""" 
    WMT : Wal-Mart Stores, Inc.
    MCD : McDonald’s Corp.
    JNJ : Johnson & Johnson Inc.
    JPM : JPMorgan Chase and Co.
    MSFT: Microsoft Corp.
"""