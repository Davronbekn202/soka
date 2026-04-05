# db/connect.py
import psycopg2


class DBManager:
    def __init__(self, host="localhost", user="test", password="12", database="postgres", port=5432):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host,
                                     port=self.port)

    def __enter__(self):
        return  self.conn.cursor()             # cursor qaytarish kerak

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            self.conn.rollback()          # xatolikda rollback
            self.conn.close()
            raise

        if self.conn:
            self.conn.commit()          # muvaffaqiyatda commit
            self.conn.close()