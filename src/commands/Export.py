from argparse import Namespace
from sqlite3 import connect
from pandas import read_sql_query


def run(arguments: Namespace):
    CONNECTION = connect(arguments.db)
    STATEMENT = None
    if not str(arguments.sql_file) == '.':
        STATEMENT = open(arguments.sql_file, 'r').read()
    else:
        STATEMENT = arguments.statement
    
    try:
        dataframe = read_sql_query(STATEMENT, CONNECTION)

        if arguments.type == 'csv':
            dataframe.to_csv(arguments.to_file, sep=arguments.delimiter,
                                                index=False)
        elif arguments.type == 'excel':
            dataframe.to_excel(arguments.to_file, index=False)
    except Exception as error:
        print("> Ocorreu o seguinte erro durante a exportação: ", error)


