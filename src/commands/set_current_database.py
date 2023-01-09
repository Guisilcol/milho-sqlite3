from util import Config, JsonHandler, DynamicDataclass, TerminalQuiz as tq, ApplicationFlow as af
from dataclasses import dataclass

@dataclass(init=False)
class SetCurrentDatabaseArgs(DynamicDataclass):
    current_database: str
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class SetCurrentDatabase:
    def __init__(self):
        raise NotImplementedError("This class cannot be instantiated")
        
    @staticmethod
    def run(config: Config):
        try:
            arguments = SetCurrentDatabase.__show_terminal_quiz(config)
            config.current_db_filepath = arguments.current_database
            JsonHandler.save_json_file(config.config_filepath, config.dict())
            
        except KeyboardInterrupt:
            af.print_returning_to_menu()

    @staticmethod
    def __show_terminal_quiz(config: Config):
        current_database = tq.ask_for_list("Choose the database you want to set as current", config.db_filepath_list)
        return SetCurrentDatabaseArgs(current_database = current_database)