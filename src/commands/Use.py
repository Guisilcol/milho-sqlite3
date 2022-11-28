from sqlite3 import connect
from tabulate import tabulate
from dataclasses import dataclass, fields

@dataclass(init=False)
class UseCommandArgs:
    db: str
    
    def __init__(self, **kwargs):
        fields_name = set([field.name for field in fields(self)])
        for key, value in kwargs.items():
            if key in fields_name:
                setattr(self, key, value)


class Use:
    
    def __init__(self) -> None:
        raise NotImplementedError()

    @staticmethod
    def run(arguments: UseCommandArgs):
        CONNECTION = connect(arguments.db)

        while (True):
            try:
                cursor = None
                command = input("milho-sqlite3: ").strip()

                if (command.startswith('.exit')):
                    break
                elif (command.startswith('.tables')):
                    command = "SELECT name FROM sqlite_master WHERE type='table';"

                elif (command.startswith(".desc")):
                    table = command[6:]
                    command = f"PRAGMA table_info('{table}');"

                cursor = CONNECTION.execute(command)

                if cursor.description != None:
                    data = cursor.fetchall()
                    headers = [tup[0] for tup in cursor.description]
                    print()
                    print(tabulate(data, headers=headers))
                    print()
            except KeyboardInterrupt:
                break
            except Exception as error:
                print("> Ocorreu um erro com o comando de entrada: ", error)
