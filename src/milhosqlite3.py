from menu import Menu
from util import Config, JsonHandler
import os 

def main():
    CONFIG_FILEPATH = os.path.join(os.path.dirname(__file__), "config.json")

    config = None
    if os.path.exists(CONFIG_FILEPATH):
        json = JsonHandler.load_json_file(CONFIG_FILEPATH)
        config = Config(**json)
    else:
        config = Config(**{"current_db_filepath": None, "db_filepath_list": [":memory:"], "config_filepath": CONFIG_FILEPATH})
        JsonHandler.save_json_file(CONFIG_FILEPATH, config.dict())

    Menu.run(config)


if __name__ == "__main__":
    main()