from util.dynamic_dataclass import DynamicDataclass
from dataclasses import dataclass

@dataclass(init=False)
class Config(DynamicDataclass):
    config_filepath: str
    current_db_filepath: str 
    db_filepath_list: list