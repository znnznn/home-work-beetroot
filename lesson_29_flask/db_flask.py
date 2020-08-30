import psycopg2

from psycopg2.extras import RealDictCursor



class DataBase:
    def __init__(self, user: dict):
        self.connection = None
        self.cursor = None
        self.user = user
        self.data_base()



    def data_base(self):

        try:
            self.connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                               user='postgres', password='postgres')
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

        except:
            self.cursor.close()


    def take_user(self):

        try:
            print(self.user['email'])
            self.cursor.execute("SELECT * FROM users WHERE email = %s", (f"{self.user['email']}",))
            user = self.cursor.fetchone()
            print(dict(user))
            if user:

                return dict(user)

            return False
        except Exception as e:
            print(e, 'take_user')
            return False

    def take_user_id(self, user_id):

        try:
            print(self.user['email'])
            self.cursor.execute("SELECT * FROM users WHERE email = %s", (f"{user_id}",))
            user = self.cursor.fetchone()
            print(dict(user))
            if user:

                return dict(user)

            return False
        except Exception as e:
            print(e, 'take_user')
            return False

    def edit_user(self):
        pass

    def del_user(self):
        pass

    def add_user(self):

        if self.take_user():
            return False
        try:
            print(5)
            self.cursor.execute("""INSERT INTO users(FIRST_NAME, LAST_NAME, USERNAME,
                                PASSWORD, EMAIL, ADDRESS, oper_date)
                                VALUES(%s, %s, %s, %s, %s, %s, %s);""", (f"{self.user['firstName']}",
                                                                          f"{self.user['firstName']}",
                                                                          f"{self.user['username']}",
                                                                          f"{self.user['password']}",
                                                                          f"{self.user['email']}",
                                                                          f"{self.user['address']}",
                                                                          f"{self.user['date']}",))
            self.cursor.close()
            self.connection.commit()
            return True
        except Exception as e:
            print(e, 'add_user')
            self.connection.rollback()
            self.user['None'] = e
            return False

    def edit_user_views(self):

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
        pass

    def add_user_views(self):
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
            #self.cursor.execute("""CREATE TABLE IF NOT EXISTS %s( ID serial PRIMARY KEY NOT NULL,
            #                                                      STOCK_NAME VARCHAR(500) NOT NULL,
            #                                                      STICKER_STOCK VARCHAR(500) NOT NULL,
            #                                                      BID integer NOT NULL,
            #                                                      ASK integer NOT NULL,
            #                                                      oper_date VARCHAR(500) NOT NULL
            #                                                      );""" % (self.user['email'],))
            self.cursor.close()
            self.connection.commit()
            return True

    def take_user_views(self):
        pass

    def create_tab(self):

        my_add = self.user['email'][:5]
        try:

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                                                  ID serial PRIMARY KEY NOT NULL,
                                                  FIRST_NAME VARCHAR(500) NOT NULL,
                                                  LAST_NAME VARCHAR(500) NOT NULL,
                                                  USERNAME VARCHAR (500) NOT NULL,
                                                  PASSWORD VARCHAR NOT NULL,
                                                  EMAIL VARCHAR (500) NOT NULL,
                                                  ADDRESS VARCHAR(500) NOT NULL,
                                                  oper_date VARCHAR(500) NOT NULL                                          
                                                  );""")

            self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {my_add} (
                                                  ID serial PRIMARY KEY NOT NULL,
                                                  STOCK_NAME VARCHAR(20) NOT NULL,
                                                  STICKER_STOCK VARCHAR(20) NOT NULL,
                                                  BID integer NOT NULL,
                                                  ASK integer NOT NULL,
                                                  oper_date VARCHAR(20) NOT NULL                                           
                                                  );""")
            self.cursor.close()
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            return print(f'Помилка з\'єднання з базою даних : {e}')


""" 
    WMT : Wal-Mart Stores, Inc.
    MCD : McDonald’s Corp.
    JNJ : Johnson & Johnson Inc.
    JPM : JPMorgan Chase and Co.
    MSFT: Microsoft Corp.
"""