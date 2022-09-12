from argparse import Namespace
from sqlite3 import connect
from tabulate import tabulate


def run(arguments: Namespace):
    CONNECTION = connect(arguments.db)
    statement = None
    if not str(arguments.from_file) == '.':
        statement = open(arguments.from_file, 'r').read()
    else:
        statement = arguments.statement

    cursor = CONNECTION.execute(statement)
    if not cursor.description == None:
        data = cursor.fetchall()
        headers = [tup[0] for tup in cursor.description]
        print(tabulate(data, headers=headers))
