from argparse import Namespace
from sqlite3 import connect


def run(arguments: Namespace):
    CONNECTION = connect(arguments.db)
    table_name = arguments.table
    index_name = arguments.index
    cols = [col for col in str(arguments.cols).split(',')]
    cols = ", ".join(cols)

    create_index_statement = f"CREATE INDEX {index_name} ON {table_name} ({cols});"
    CONNECTION.execute(create_index_statement)
