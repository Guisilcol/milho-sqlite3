from sqlite3 import connect
from dataclasses import dataclass, fields

@dataclass(init=False)
class IndexCommandArgs:
    db: str
    table: str
    index: str
    cols: str

    def __init__(self, **kwargs):
        fields_name = set([field.name for field in fields(self)])
        for key, value in kwargs.items():
            if key in fields_name:
                setattr(self, key, value)


class Index:
    def __init__(self) -> None:
        raise NotImplementedError()

    @staticmethod
    def run(arguments: IndexCommandArgs):
        CONNECTION = connect(arguments.db)
        table_name = arguments.table
        index_name = arguments.index
        cols = [col for col in str(arguments.cols).split(',')]
        cols = ", ".join(cols)

        create_index_statement = f"CREATE INDEX {index_name} ON {table_name} ({cols});"
        CONNECTION.execute(create_index_statement)
        CONNECTION.commit()
        CONNECTION.close()