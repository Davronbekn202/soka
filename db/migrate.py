import os
from db.connect import DBManager

MIGRATIONS_PATH = "migrations"


def ensure_migrate_table():
    with DBManager() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS migrations (
            id SERIAL PRIMARY KEY,
            filename TEXT UNIQUE
        );
        """)


def run_migration():
    ensure_migrate_table()
    files_to_migrate = []
    files = sorted(os.listdir(MIGRATIONS_PATH))

    with DBManager() as cursor:
        migrated = []
        cursor.execute("SELECT filename FROM migrations;")

        for i in cursor.fetchall():
            migrated.append(i[0])

        print(migrated)

        for filename in files:
            if filename not in migrated:
                files_to_migrate.append(filename)

    for filename in files_to_migrate:
        if not filename.endswith(".py"):
            with open(os.path.join(MIGRATIONS_PATH, filename), "r") as f:
                sql = f.read()

            with DBManager() as cursor:
                cursor.execute(sql)

            print(f'applied {filename}')

            with DBManager() as cursor:
                cursor.execute("INSERT INTO migrations (filename) VALUES (%s)",(filename,)
                )


# print(os.listdir(MIGRATIONS_PATH))
if __name__ == '__main__':
    run_migration()

