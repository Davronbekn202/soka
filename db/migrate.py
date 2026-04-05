
import os
from db.connect import DBManager
MIGRATIONS_PATH = "migration"


def run_migration():
    with DBManager() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS migration (
            id SERIAL PRIMARY KEY,
            filename TEXT UNIQUE
        );
        """)



if __name__ == '__main__':
    run_migration()
