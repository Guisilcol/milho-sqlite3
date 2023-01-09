import sqlite3

class Database:

    @staticmethod
    def get_sqlite3_table_list(db_filepath: str) -> list:
        connection = sqlite3.connect(db_filepath)
        cursor = connection.execute("SELECT DISTINCT name FROM sqlite_master WHERE type='table';")
        table_list = [tup[0] for tup in cursor.fetchall()]
        connection.close()
        return table_list

    @staticmethod
    def get_columns_from_sqlite3_table(db_filepath: str, table_name: str) -> list:
        connection = sqlite3.connect(db_filepath)
        cursor = connection.execute(f"PRAGMA table_info('{table_name}');")
        columns = [tup[1] for tup in cursor.fetchall()]
        connection.close()
        return columns