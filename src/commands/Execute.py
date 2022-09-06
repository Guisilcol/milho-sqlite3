from argparse import Namespace
import sqlite3
from tabulate import tabulate

def run(arguments: Namespace):
    CONNECTION = sqlite3.connect(arguments.db)
    STATEMENT = None
    if not str(arguments.from_file) == '.':
        STATEMENT = open(arguments.from_file, 'r').read()
    else: 
        STATEMENT = arguments.statement

    cursor = CONNECTION.execute(STATEMENT)
    if not cursor.description == None:
        data = cursor.fetchall()
        headers = [tup[0] for tup in cursor.description]
        print(tabulate(data, headers=headers))
    
    
