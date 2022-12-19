from pandas import (read_excel,
                    read_fwf,
                    read_csv)
from sqlite3 import connect
from dataclasses import dataclass, fields
import typing as types
import inquirer as inq

@dataclass(init=False)
class LoadV2Args:
    db: str
    to_table: str
    from_file: str
    file_type: types.Literal['excel', 'csv', 'fixed']
    delimiter_or_cols_width: str
    drop_table: bool = False # valor padrão no arquivo arguments.py
    truncate: bool = False # valor padrão no arquivo arguments.py
    header: bool = True # valor padrão no arquivo arguments.py
    ignore_first_n_rows: int = 0 # valor padrão no arquivo arguments.py
    ignore_last_n_rows: int = 0 # valor padrão no arquivo arguments.py

    def __init__(self, **kwargs):
        fields_name = set([field.name for field in fields(self)])
        for key, value in kwargs.items():
            if key in fields_name:
                setattr(self, key, value)
class LoadV2:
    @staticmethod
    def run(args: dict):
        arguments = LoadV2.__get_arguments(args)
        print(arguments)
        dataframe = None

        if arguments.file_type == "excel":
            have_header = 0 if arguments.header else None
            dataframe = read_excel(arguments.from_file,
                                    header=have_header,
                                    skiprows=int(arguments.ignore_first_n_rows),
                                    skipfooter=int(arguments.ignore_last_n_rows))

        elif arguments.file_type == 'fixed':
            cols_width = str(arguments.delimiter_or_cols_width).split(",")
            cols_width = [int(width) for width in cols_width]
            dataframe = read_fwf(arguments.from_file,
                                    widths=cols_width)

        else:
            have_header = 0 if arguments.header else None
            dataframe = read_csv(arguments.from_file,
                                    delimiter=arguments.delimiter_or_cols_width,
                                    header=have_header,
                                    skiprows=int(arguments.ignore_first_n_rows),
                                    skipfooter=int(arguments.ignore_last_n_rows))

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
                        if_exists='append',
                        index=False)

    @staticmethod
    def __get_arguments(parsed_args: dict):
        args = {}
        args.update({
            "db": parsed_args.get("db"), 
            "from_file": parsed_args.get('from_file')
        })

        questions = [
            inq.Text("to_table", message="Nome da tabela"),
            inq.List("file_type", message="Tipo do arquivo",
                        choices=["excel", "csv", "fixed"]),
            inq.Text("delimiter_or_cols_width", message="Delimitador (CSV) ou tamanho das colunas do arquivo (FIXED). (Ignorar caso o arquivo seja Excel)"),

            inq.Confirm("drop_table", message="Deseja dropar a tabela?", default=False),
            inq.Confirm("truncate", message="Deseja truncar a tabela?", default=False),
            inq.Confirm("header", message="O arquivo possui cabeçalho?", default=True),
            inq.Text("ignore_first_n_rows", message="Quantas linhas ignorar no início do arquivo?", default='0'),
            inq.Text("ignore_last_n_rows", message="Quantas linhas ignorar no final do arquivo?", default='0')
        ]

        answers = inq.prompt(questions)
        args.update(answers)
        return LoadV2Args(**args)

        