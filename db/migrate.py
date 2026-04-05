import os
from db.connect import DBManager

MIGRATION_PATH = 'migrations'

def ensure_migrate():
    with DBManager() as cur:
        cur.execute("""
            create table in not exists migrations(
                id SERIAL PRIMARY KEY,
                filename TEXT UNIQUE
            );
        """)

if __name__ == '__main__':
    ensure_migrate()