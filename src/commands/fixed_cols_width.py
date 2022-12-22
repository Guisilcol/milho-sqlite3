from dataclasses import dataclass, fields

@dataclass(init=False)
class FixedColsWidthArgs:
    layout: str 

    def __init__(self, **kwargs):
        fields_name = set([field.name for field in fields(self)])
        for key, value in kwargs.items():
            if key in fields_name:
                setattr(self, key, value)

class FixedColsWidth:
    @staticmethod
    def run(arguments: dict):
        args = FixedColsWidthArgs(**arguments)
        each_col_layout = args.layout.split(' ')
        
        normalized_col_layout = []
        
        for index, col_layout in enumerate(each_col_layout):
            if index == len(each_col_layout) - 1:
                normalized_col_layout.append(col_layout)
                continue 
            
            normalized_col_layout.append(col_layout + ' ')

        col_len = [str(len(col)) for col in normalized_col_layout]
        col_layout = ','.join(col_len)
        print(col_layout)

        

        


            

        
