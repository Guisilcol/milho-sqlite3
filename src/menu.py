from util import TerminalQuiz as tq, ApplicationFlow as af, Config
import commands

class Menu:    
    @classmethod
    def __get_set_current_database_function(cls):
        """Returns a function (command) that sets the current database"""
        return commands.SetCurrentDatabase.run

    @classmethod
    def __get_manage_databases_function(cls):
        """Returns a function (command) that manages databases"""
        return commands.ManageDatabase.run

    @classmethod
    def __get_use_current_database_function(cls):
        """Returns a function (command) that enters in current database"""
        return commands.Use.run

    @classmethod
    def __get_export_data_from_current_database_function(cls):
        """Returns a function (command) that exports data from current database"""
        return commands.Export.run

    @classmethod
    def __get_create_index_in_current_database_function(cls):
        """Returns a function (command) that creates an index in current database"""
        return commands.Index.run

    @classmethod
    def __get_load_data_file_into_current_database_function(cls):
        """Returns a function (command) that loads a data file into current database"""
        return commands.LoadV2.run

    @classmethod
    def __get_define_a_rpt_file_layout_function(cls):
        """Returns a function (command) that defines a RPT file layout"""	
        return commands.RptFilesColsLayout.run

    @classmethod
    def __show_menu(cls, last_command: str | None):
        """Shows the menu and returns the function (command) to be executed"""
        if last_command == None:
            last_command = "Set current database"

        commands = {
            "Set current database": cls.__get_set_current_database_function,
            "Manage databases": cls.__get_manage_databases_function,
            "Use current database": cls.__get_use_current_database_function,
            "Export data from current database": cls.__get_export_data_from_current_database_function,
            "Create index in current database": cls.__get_create_index_in_current_database_function, 
            "Load data file into current database": cls.__get_load_data_file_into_current_database_function,
            "Define a RPT file layout": cls.__get_define_a_rpt_file_layout_function
        }

        options = [key for key in commands.keys()]
        choose =  tq.ask_for_list("Choose an option (press Ctrl + C to exit)", options, last_command)
        get_function = commands[choose]
        return (get_function(), choose)
    
    @classmethod
    def run(cls, config: Config):   
        last_command = None
        while True:
            try:
                if config.current_db_filepath == None:
                    print("Current database not set, please set it first.")
                    command = cls.__get_set_current_database_function()
                    command(config)
                    continue
                
                command, last_command = cls.__show_menu(last_command)
                command(config)

            except KeyboardInterrupt:
                af.exit_application_successfully()
            except:
                print("An error has occurred: ")
                af.print_traceback()
                continue
    
    def __init__(self) -> None:
        raise NotImplementedError('This class is not meant to be instantiated')
