import psycopg2


class DataBase:
    def __init__(self, user: dict):
        self.connection = None
        self.cursor = None
        self.user = user
        self.data_base()

        print(5)

    def data_base(self):

        try:
            self.connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                          user='postgres', password='postgres')
            self.cursor = self.connection.cursor()

        except:
            self.cursor.close()


    def take_user(self):

        try:
            print(77)
            self.cursor.execute(""" SELECT * FROM users WHERE users.email = %s""", (self.user['email'],))
            user = self.cursor.fetchone()
            if user:
                print(user, 88)
                return user
            print(99)
            return False
        except Exception as e:
            return False

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
        print(self.user)
        my_add = self.user['email'][:5]
        try:

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                                                  ID serial PRIMARY KEY NOT NULL,
                                                  FIRST_NAME VARCHAR(20) NOT NULL,
                                                  LAST_NAME VARCHAR(20) NOT NULL,
                                                  USERNAME VARCHAR (20) NOT NULL,
                                                  PASSWORD VARCHAR NOT NULL,
                                                  EMAIL VARCHAR (20) NOT NULL,
                                                  ADDRESS VARCHAR(100) NOT NULL,
                                                  oper_date VARCHAR(20) NOT NULL                                          
                                                  );""")
            print(2999)
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