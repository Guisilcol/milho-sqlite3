from pandas import (read_excel,
                    read_fwf,
                    read_csv)
from sqlite3 import connect
from dataclasses import dataclass, fields
import typing as types

@dataclass(init=False)
class LoadArgs:
    db: str
    to_table: str
    from_file: str
    file_type: types.Literal['excel', 'csv', 'fixed']
    delimiter: str
    drop_table: bool = False # valor padrão no arquivo arguments.py
    truncate: bool = False # valor padrão no arquivo arguments.py
    cols_width: str = "1,1" # valor padrão no arquivo arguments.py
    header: bool = True # valor padrão no arquivo arguments.py
    ignore_first_n_rows: int = 0 # valor padrão no arquivo arguments.py
    ignore_last_n_rows: int = 0 # valor padrão no arquivo arguments.py

    def __init__(self, **kwargs):
        fields_name = set([field.name for field in fields(self)])
        for key, value in kwargs.items():
            if key in fields_name:
                setattr(self, key, value)
class Load:
    
    def __init__(self) -> None:
        raise NotImplementedError()

    @staticmethod
    def run(arguments: LoadArgs):
        dataframe = None

        if arguments.file_type == "excel":
            have_header = 0 if arguments.header else None
            dataframe = read_excel(arguments.from_file,
                                    header=have_header,
                                    skiprows=arguments.ignore_first_n_rows,
                                    skipfooter=arguments.ignore_last_n_rows)

        elif arguments.file_type == 'fixed':
            cols_width = str(arguments.cols_width).split(",")
            cols_width = [int(width) for width in cols_width]
            dataframe = read_fwf(arguments.from_file,
                                    widths=cols_width)

        else:
            have_header = 0 if arguments.header else None
            dataframe = read_csv(arguments.from_file,
                                    delimiter=arguments.delimiter,
                                    header=have_header,
                                    skiprows=arguments.ignore_first_n_rows,
                                    skipfooter=arguments.ignore_last_n_rows)

        dataframe = (dataframe
                    .convert_dtypes()
                    .rename(columns = lambda x: str(x).strip()))

        SQLITE3_CONNECTION = connect(arguments.db)

        #Dropar a tabela?
        if (arguments.drop_table):
            SQLITE3_CONNECTION.execute(
                f"DROP TABLE IF EXISTS {arguments.to_table};")

        #Dar truncate na tabela?
        if (arguments.truncate):
            SQLITE3_CONNECTION.execute(
                f"DELETE FROM {arguments.to_table};")

        dataframe.to_sql(name=arguments.to_table,
                        con=SQLITE3_CONNECTION,
                        index=False)