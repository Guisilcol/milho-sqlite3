from util import (Config, JsonHandler, DynamicDataclass, TerminalQuiz as tq, 
                    ApplicationFlow as af)
import typing as type 
from dataclasses import dataclass

@dataclass(init=False)
class ManageDatabaseArgs(DynamicDataclass):
    choice: type.Literal["Add database", "Remove database"]
    filepath_to_add: str | None
    filepaths_to_remove: list
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ManageDatabase:
    def __init__(self):
        raise NotImplementedError("This class cannot be instantiated")
        
    @staticmethod
    def run(config: Config):
        try:
            arguments = ManageDatabase.__show_terminal_quiz(config)
            if arguments.choice == "Add database":
                config.db_filepath_list.append(arguments.filepath_to_add)

            elif arguments.choice == "Remove database":
                for filepath in arguments.filepaths_to_remove:
                    config.db_filepath_list.remove(filepath)
            
            JsonHandler.save_json_file(config.config_filepath, config.dict())
            
        except KeyboardInterrupt:
            af.print_returning_to_menu()
        


    @staticmethod
    def __show_terminal_quiz(config: Config):
        choice = tq.ask_for_list("Choose an option", ["Add database", "Remove database"])

        filepath_to_add = None
        filepaths_to_remove = []

        if choice == "Add database":
            filepath_to_add = tq.ask_for_string("Enter the filepath of the database you want to add: ")
        elif choice == "Remove database":
            filepaths_to_remove = tq.ask_for_checkbox("Choose the database you want to remove", config.db_filepath_list)
        return ManageDatabaseArgs(choice = choice, filepath_to_add = filepath_to_add, filepaths_to_remove = filepaths_to_remove)