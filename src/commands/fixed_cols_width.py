from dataclasses import dataclass, fields

@dataclass(init=False)
class FixedColsWidthArgs:
    file: str
    row_number: int
    separator: str
    count_separators: bool

    def __init__(self, **kwargs):
        fields_name = set([field.name for field in fields(self)])
        for key, value in kwargs.items():
            if key in fields_name:
                setattr(self, key, value)

class FixedColsWidth:
    @staticmethod
    def run(arguments: FixedColsWidthArgs):
        with open(arguments.file, 'r') as file:
            line = file.readlines()[arguments.row_number]
            
            cols_width = []
            if arguments.count_separators:
                delimiters_without_separator = line.split(arguments.separator)
                cols_quantity = len(delimiters_without_separator)

                for index, delimiter in enumerate(delimiters_without_separator):
                    if index == cols_quantity - 1:
                        cols_width.append(len(delimiter) - 1)
                    else:
                        cols_width.append(len(delimiter) + 1)
            
            else:
                cols_width = [len(col) for col in line.split(arguments.separator)]

            print(",".join([str(width) for width in cols_width]))


            

        
