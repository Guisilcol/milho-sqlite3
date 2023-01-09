from sqlite3 import connect
from dataclasses import dataclass, fields
from util import TerminalQuiz as tq, ApplicationFlow as af, Config, DynamicDataclass, Database
import difflib

@dataclass(init=False)
class IndexArgs(DynamicDataclass):
    db: str
    table: str
    index: str
    cols: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Index:
    def __init__(self) -> None:
        raise NotImplementedError()

    @staticmethod
    def run(config: Config):
        try:
            arguments = Index.__show_terminal_quiz(config)

            CONNECTION = connect(arguments.db)
            table_name = arguments.table
            index_name = arguments.index
            cols = [col for col in str(arguments.cols).split(',')]
            cols = ", ".join(cols)
            create_index_statement = f"CREATE INDEX {index_name} ON {table_name} ({cols});"
            CONNECTION.execute(create_index_statement)
            CONNECTION.commit()
            CONNECTION.close()

        except KeyboardInterrupt:
            af.print_returning_to_menu()

    @staticmethod
    def __show_terminal_quiz(config: Config):
        table_list = Database.get_sqlite3_table_list(config.current_db_filepath)
        print("Tables in the database: " + "\n" + "\n".join(table_list))
        def __match_table_name(text, state: str):
            values = difflib.get_close_matches(text, table_list, n=1)
            if len(values) > 0:
                return values[0]
                
            return state

        table = None
        while True:
            table = tq.ask_for_string("Choose the table you want to create an index on", autocomplete=__match_table_name)
            if table in table_list:
                break
            print("Table not found. Try again.")
        
        columns = tq.ask_for_checkbox("Choose the columns you want to create an index on", 
                                        Database.get_columns_from_sqlite3_table(config.current_db_filepath, table))

        index = tq.ask_for_string("Enter the name of the index")

        return IndexArgs(db=config.current_db_filepath, table=table, index=index, cols=",".join(columns))


