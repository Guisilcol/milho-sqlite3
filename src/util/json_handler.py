import json

class JsonHandler():
    "Class responsible for handling json files."
    
    def __init__(self):
        raise NotImplementedError("This class is not meant to be instantiated.")

    @staticmethod
    def load_json_file(json_filepath: str) -> dict:
        with open(json_filepath, "r") as file:
            return json.load(file)

    @staticmethod
    def save_json_file(json_filepath: str, data: dict) -> None:
        with open(json_filepath, "w") as file:
            json.dump(data, file, indent=4)