from sqlite3 import connect
from tabulate import tabulate
from util import ApplicationFlow as af, Config

class Use:
    def __init__(self):
        raise NotImplementedError("This class cannot be instantiated")

    @staticmethod
    def __show_help():
        text = ("""Commands:"""
               """\n.tables - list the tables in the database"""
               """\n.desc <table> - show table details""")
        print(text)

    @staticmethod
    def run(config: Config):
        CONNECTION = connect(config.current_db_filepath)

        while (True):
            try:
                cursor = None
                command = input("milho-sqlite3 (input .help to show all commands): ").strip()

                if command.startswith('.tables'):
                    command = "SELECT name FROM sqlite_master WHERE type='table';"

                elif command.startswith(".desc"):
                    table = command[6:]
                    command = f"PRAGMA table_info('{table}');"
                
                elif command.startswith(".help"):
                    Use.__show_help()
                    continue

                cursor = CONNECTION.execute(command)

                if cursor.description != None:
                    data = cursor.fetchall()
                    headers = [tup[0] for tup in cursor.description]
                    print('\n', tabulate(data, headers=headers), '\n')

            except KeyboardInterrupt:
                af.print_returning_to_menu()
                break

            except Exception as error:
                print("an error occurred with the input command: ", error)
