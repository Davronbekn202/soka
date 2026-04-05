import psycopg2


class DBManager:
    def __init__(self, host="localhost", user="postgres", password="12", database="postgres", port=5432):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host,
                                     port=self.port)

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
            raise exc_type

        if self.conn:
            self.conn.commit()
            self.conn.close()