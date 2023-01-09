from pandas import (read_excel,
                    read_fwf,
                    read_csv,
                    read_json)
from sqlite3 import connect
from dataclasses import dataclass
import typing as types
from pathlib import Path
from util import TerminalQuiz as tq, DynamicDataclass, ApplicationFlow as af, Config

@dataclass(init=False)
class LoadV2Args(DynamicDataclass):
    db: str
    to_table: str
    from_file: Path
    file_type: types.Literal['excel', 'csv', 'fixed']
    delimiter_or_cols_width: str
    drop_table: bool = False # valor padrão no arquivo arguments.py
    truncate: bool = False # valor padrão no arquivo arguments.py
    header: bool = True # valor padrão no arquivo arguments.py
    ignore_first_n_rows: int = 0 # valor padrão no arquivo arguments.py
    ignore_last_n_rows: int = 0 # valor padrão no arquivo arguments.py

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class LoadV2:
    def __init__(self):
        raise NotImplementedError("This class cannot be instantiated")
        
    @staticmethod
    def run(args: dict, interactive_mode: bool = False):
        """Executa o comando load_v2. Comando responsável por carregar dados de um arquivo para uma tabela do banco de dados informando os parâmetros de forma interativa no terminal.

        Args:
            args (dict): Argumentos de linha de comando inseridos pelo usuário.
        """        
        try:
            arguments = LoadV2.__show_terminal_quiz(args)
            dataframe = None
            match arguments.file_type:
                case "excel":
                    dataframe = LoadV2.__excel_file_to_dataframe(arguments)
                
                case "fixed":
                    dataframe = LoadV2.__fixed_file_to_dataframe(arguments)

                case "json":
                    dataframe = LoadV2.__json_file_to_dataframe(arguments)

                case "csv":
                    dataframe = LoadV2.__csv_file_to_dataframe(arguments)


            dataframe = dataframe.convert_dtypes().rename(columns = lambda x: str(x).strip())

            SQLITE3_CONNECTION = connect(arguments.db)

            #Dropar a tabela?
            if (arguments.drop_table):
                SQLITE3_CONNECTION.execute(f"DROP TABLE {arguments.to_table};")
                SQLITE3_CONNECTION.commit()

            #Dar truncate na tabela?
            if (arguments.truncate):
                SQLITE3_CONNECTION.execute(f"DELETE FROM {arguments.to_table};")
                SQLITE3_CONNECTION.commit()

            dataframe.to_sql(name=arguments.to_table, con=SQLITE3_CONNECTION, if_exists='append', index=False)
            SQLITE3_CONNECTION.close()

        except KeyboardInterrupt:
            af.print_returning_to_menu()

    @staticmethod
    def __show_terminal_quiz(config: Config) -> LoadV2Args:
        """Cria um quiz no terminal para o usuário preencher os argumentos do comando.

        Args:
                args (dict): Argumentos informados na inicialização do programa. Precisa conter os argumentos "db" e "from_file".

        Returns:
            LoadV2Args: Argumentos que serão utilizados no comando.
        """        

        db = config.current_db_filepath
        from_file = tq.ask_for_string("Filepath of file to load", "")
        to_table = tq.ask_for_string("Table name", "")
        file_type = tq.ask_for_list("Filetype", ["excel", "csv", "fixed", "json"], "excel")
        
        delimiter_or_cols_width = None if file_type not in ["csv", "fixed"]\
            else tq.ask_for_string("Delimiter (CSV file) or columns Width (Fixed file)", "")
        
        drop_table = tq.ask_yes_or_no("Drop table?", False)
        truncate = tq.ask_yes_or_no("Truncate table?", False)
        header = tq.ask_yes_or_no("File have header?", True)
        ignore_first_n_rows = tq.ask_for_integer("How many lines to ignore at the beginning of the file?", 0)
        ignore_last_n_rows = tq.ask_for_integer("How many lines to ignore at the end of the file?", 0)

        return LoadV2Args(db=db, from_file=from_file, to_table=to_table, file_type=file_type, delimiter_or_cols_width=delimiter_or_cols_width, 
                    drop_table=drop_table, truncate=truncate, header=header, ignore_first_n_rows=ignore_first_n_rows, ignore_last_n_rows=ignore_last_n_rows)

    @staticmethod
    def __csv_file_to_dataframe(arguments: LoadV2Args):
        have_header = 0 if arguments.header else None
        return read_csv(arguments.from_file, delimiter=arguments.delimiter_or_cols_width, header=have_header,
                                skiprows=int(arguments.ignore_first_n_rows), skipfooter=int(arguments.ignore_last_n_rows))

    @staticmethod
    def __excel_file_to_dataframe(arguments: LoadV2Args):
        have_header = 0 if arguments.header else None
        return read_excel(arguments.from_file, header=have_header, skiprows=int(arguments.ignore_first_n_rows), 
                                skipfooter=int(arguments.ignore_last_n_rows))

    @staticmethod
    def __fixed_file_to_dataframe(arguments: LoadV2Args):
        cols_width = str(arguments.delimiter_or_cols_width).split(",")
        cols_width = [int(width) for width in cols_width]
        return read_fwf(arguments.from_file, widths=cols_width)

    @staticmethod
    def __json_file_to_dataframe(arguments: LoadV2Args):
        return read_json(arguments.from_file)


        