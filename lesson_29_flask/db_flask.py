import psycopg2


class DataBase:
    def __init__(self, connection, cursor, user):
        self.connection = connection
        self.cursor = cursor
        self.user = user
        self.create_tab()

    def create_tab(self):

        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS ? (
                                      ID serial PRIMARY KEY NOT NULL,
                                      STOCK_NAME VARCHAR(20) NOT NULL,
                                      STICKER_STOCK VARCHAR(20) NOT NULL,
                                      BID integer (20) NOT NULL,
                                      ASK integer (20) NOT NULL
                                      oper_date VARCHAR(20) NOT NULL                                           
                                      );""", (self.user, ))
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