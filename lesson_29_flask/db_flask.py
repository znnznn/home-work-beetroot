import psycopg2


class DataBase:
    def __init__(self, connection, cursor, user: dict):
        self.connection = connection
        self.cursor = cursor
        self.user = user
        self.create_tab()

    def take_user(self):

        try:
            self.cursor.execute(""" SELECT * FROM users WHERE EMAIL = %;""", (self.user['email']))
            user = self.cursor.fetchone()
            if user:
                return user
            return False
        except Exception as e:
            return f'{e}'

    def edit_user(self):
        pass

    def del_user(self):
        pass

    def add_user(self):

        pass

    def edit_user_views(self):
        pass

    def del_user_views(self):
        pass

    def add_user_views(self):
        pass

    def take_user_views(self):
        pass

    def create_tab(self):

        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS &% (
                                      ID serial PRIMARY KEY NOT NULL,
                                      STOCK_NAME VARCHAR(20) NOT NULL,
                                      STICKER_STOCK VARCHAR(20) NOT NULL,
                                      BID integer (20) NOT NULL,
                                      ASK integer (20) NOT NULL
                                      oper_date VARCHAR(20) NOT NULL                                           
                                      );""", (self.user, ))
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                                                  ID serial PRIMARY KEY NOT NULL,
                                                  FIRST_NAME VARCHAR(20) NOT NULL,
                                                  LAST_NAME VARCHAR(20) NOT NULL,
                                                  USERNAME VARCHAR (20) NOT NULL,
                                                  PASSWORD VARCHAR NOT NULL
                                                  EMAIL VARCHAR (20) NOT NULL
                                                  ADDRESS VARCHAR(100) NOT NULL
                                                  oper_date VARCHAR(20) NOT NULL                                          
                                                  );""")
            self.cursor.close()
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            return f'Помилка з\'єднання з базою даних : {e}'


""" 
    WMT : Wal-Mart Stores, Inc.
    MCD : McDonald’s Corp.
    JNJ : Johnson & Johnson Inc.
    JPM : JPMorgan Chase and Co.
    MSFT: Microsoft Corp.
"""