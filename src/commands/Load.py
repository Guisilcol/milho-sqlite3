import pandas as pd
from argparse import Namespace
import sqlite3

def run(arguments: Namespace):
    DATAFRAME = None

    if arguments.file_type == "excel":
        have_header = 0 if arguments.header else None
        DATAFRAME = pd.read_excel(arguments.from_file, 
                                    header=have_header, 
                                    skiprows=arguments.ignore_first_n_rows,
                                    skipfooter=arguments.ignore_last_n_rows)
    
    elif arguments.file_type == 'fixed':
        cols_width = str(arguments.cols_width).split(",")
        cols_width = [int(width) for width in cols_width]
        DATAFRAME = pd.read_fwf(arguments.from_file, widths=cols_width)
    
    else:
        have_header = 0 if arguments.header else None
        DATAFRAME = pd.read_csv(arguments.from_file, 
                                    delimiter=arguments.delimiter,
                                    header=have_header,
                                    skiprows=arguments.ignore_first_n_rows,
                                    skipfooter=arguments.ignore_last_n_rows)

    DATAFRAME = DATAFRAME.convert_dtypes()
    DATAFRAME = DATAFRAME.rename(columns=lambda x: x.strip())
    SQLITE3_CONNECTION = sqlite3.connect(arguments.db)

    #Dropar a tabela?
    if(arguments.drop_table):
        SQLITE3_CONNECTION.execute(f"DROP TABLE IF EXISTS {arguments.to_table};")
    
    #Dar truncate na tabela?
    if(arguments.truncate):
        SQLITE3_CONNECTION.execute(f"TRUNCATE TABLE IF EXISTS {arguments.to_table};")

    DATAFRAME.to_sql(name=arguments.to_table, con=SQLITE3_CONNECTION, index=False)


