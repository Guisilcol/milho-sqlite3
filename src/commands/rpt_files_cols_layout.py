from util import TerminalQuiz as tq, ApplicationFlow as af, Config, DynamicDataclass
import typing as types
from dataclasses import dataclass
import re

@dataclass(init=False)
class RptFilesColsLayoutArgs(DynamicDataclass):
    layout: str 
    type: types.Literal['header', 'separators']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class RptFilesColsLayout:
    def __init__(self):
        raise NotImplementedError("This class cannot be instantiated")
        
    @staticmethod
    def run(config: Config):
        try:
            args = RptFilesColsLayout.__show_terminal_quiz()
            if args.type == "separators":
                each_col_layout = args.layout.split(' ')
                
                normalized_col_layout = []
                
                for index, col_layout in enumerate(each_col_layout):
                    if index == len(each_col_layout) - 1:
                        normalized_col_layout.append(col_layout)
                        continue 
                    
                    normalized_col_layout.append(col_layout + ' ')

                col_len = [str(len(col)) for col in normalized_col_layout]
                col_layout = ','.join(col_len)
                print("Layout:")
                print(col_layout)

            elif args.type == "header":
                regex = r"([a-zA-Z0-9_]+( )+)"
                matches = re.findall(regex, args.layout)
                print(matches)
                col_len = [str(len(match[0])) for match in matches]
                col_layout = ','.join(col_len)
                print("Layout:")
                print(col_layout)

        except KeyboardInterrupt:
            af.print_returning_to_menu()

    @staticmethod
    def __show_terminal_quiz():
        layout = tq.ask_for_string("Enter the column layout")
        layout_type = tq.ask_for_list("Choose the type", ['header', 'separators'])
        return RptFilesColsLayoutArgs(layout = layout, type = layout_type)

            

        
