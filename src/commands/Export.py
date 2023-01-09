from sqlite3 import connect
from pandas import read_sql_query
from dataclasses import dataclass
import typing as types
from util import Config, TerminalQuiz as tq, ApplicationFlow as af, DynamicDataclass
import datetime

@dataclass(init=False)
class ExportArgs(DynamicDataclass):
    db: str
    statement: str
    type: types.Literal['excel', 'csv', 'json'] 
    delimiter: str
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Export:
    def __init__(self):
        raise NotImplementedError("This class cannot be instantiated")

    @staticmethod
    def run(config: Config):
        try:
            arguments = Export.__show_terminal_quiz(config)
            CONNECTION = connect(arguments.db)
            dataframe = read_sql_query(arguments.statement, CONNECTION)

            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"Exported_{timestamp}"

            if arguments.type == 'csv':
                dataframe.to_csv(f"./{filename}.csv", sep=arguments.delimiter, index=False)

            elif arguments.type == 'excel':
                dataframe.to_excel(f"./{filename}.xlsx", index=False)

            elif arguments.type == 'json':
                dataframe.to_json(f"./{filename}.json", orient='records', index=False)

            print("Export completed successfully!")

        except KeyboardInterrupt:
            af.print_returning_to_menu()

    @staticmethod
    def __show_terminal_quiz(config: Config):
        file_type = tq.ask_for_list("Choose the file type", ['excel', 'csv', 'json'])

        delimiter = None 
        if file_type == 'csv':
            delimiter = tq.ask_for_string("Enter the delimiter")

        statement = tq.ask_for_string("Enter the SQL statement")

        return ExportArgs(db = config.current_db_filepath, statement = statement, type = file_type, delimiter = delimiter)