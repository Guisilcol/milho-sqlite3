from pandas import (read_excel,
                    read_fwf,
                    read_csv)
from argparse import Namespace
from sqlite3 import connect


def run(arguments: Namespace):
    dataframe = None

    if arguments.file_type == "excel":
        have_header = 0 if arguments.header else None
        dataframe = read_excel(arguments.from_file,
                               header=have_header,
                               skiprows=arguments.ignore_first_n_rows,
                               skipfooter=arguments.ignore_last_n_rows)

    elif arguments.file_type == 'fixed':
        cols_width = str(arguments.cols_width).split(",")
        cols_width = [int(width) for width in cols_width]

        dataframe = read_fwf(arguments.from_file,
                             widths=cols_width)

    else:
        have_header = 0 if arguments.header else None
        dataframe = read_csv(arguments.from_file,
                             delimiter=arguments.delimiter,
                             header=have_header,
                             skiprows=arguments.ignore_first_n_rows,
                             skipfooter=arguments.ignore_last_n_rows)

    dataframe = (dataframe
                 .convert_dtypes()
                 .rename(columns = lambda x: x.strip()))

    SQLITE3_CONNECTION = connect(arguments.db)

    #Dropar a tabela?
    if (arguments.drop_table):
        SQLITE3_CONNECTION.execute(
            f"DROP TABLE IF EXISTS {arguments.to_table};")

    #Dar truncate na tabela?
    if (arguments.truncate):
        SQLITE3_CONNECTION.execute(
            f"TRUNCATE TABLE IF EXISTS {arguments.to_table};")

    dataframe.to_sql(name=arguments.to_table,
                     con=SQLITE3_CONNECTION,
                     index=False)
