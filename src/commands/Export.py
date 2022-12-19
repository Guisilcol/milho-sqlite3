from sqlite3 import connect
from pandas import read_sql_query
from dataclasses import dataclass, fields
import typing as types

@dataclass(init=False)
class ExportArgs:
    db: str
    statement: str
    to_file: str
    type: types.Literal['excel', 'csv'] 
    delimiter: str
    sql_file: str = '.' # valor padrão no arquivo arguments.py
    
    def __init__(self, **kwargs):
        fields_name = set([field.name for field in fields(self)])
        for key, value in kwargs.items():
            if key in fields_name:
                setattr(self, key, value)


class Export:
    @staticmethod
    def run(arguments: ExportArgs):
        CONNECTION = connect(arguments.db)
        STATEMENT = None
        if not str(arguments.sql_file) == '.':
            STATEMENT = open(arguments.sql_file, 'r').read()
        else:
            STATEMENT = arguments.statement
        
        try:
            dataframe = read_sql_query(STATEMENT, CONNECTION)

            if arguments.type == 'csv':
                dataframe.to_csv(arguments.to_file, sep=arguments.delimiter,
                                                    index=False)
            elif arguments.type == 'excel':
                dataframe.to_excel(arguments.to_file, index=False)
        except Exception as error:
            print("> Ocorreu o seguinte erro durante a exportação: ", error)