from sqlite3 import connect
from tabulate import tabulate
from dataclasses import dataclass, fields

@dataclass(init=False)
class ExecuteCommandArgs:
    db: str
    statement: str
    from_file: str = '.' # valor padrão no arquivo arguments.py

    def __init__(self, **kwargs):
        fields_name = set([field.name for field in fields(self)])
        for key, value in kwargs.items():
            if key in fields_name:
                setattr(self, key, value)

                
class Execute: 
    
    def __init__(self) -> None:
        raise NotImplementedError()
        
    @staticmethod
    def run(arguments: ExecuteCommandArgs):
        CONNECTION = connect(arguments.db)
        statement = None
        if not str(arguments.from_file) == '.':
            statement = open(arguments.from_file, 'r').read()
        else:
            statement = arguments.statement

        cursor = CONNECTION.execute(statement)
        if not cursor.description == None:
            data = cursor.fetchall()
            headers = [tup[0] for tup in cursor.description]
            print(tabulate(data, headers=headers))
    



