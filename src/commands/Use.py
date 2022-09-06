from argparse import Namespace
import sqlite3
from tabulate import tabulate 

def run(arguments: Namespace):
    CONNECTION = sqlite3.connect(arguments.db)
    
    while(True):
        cursor = None
        have_errors = False
        command = input("milho-sqlite3: ")

        if(command.strip() == '.exit'):
            break
        
        try:
            cursor = CONNECTION.execute(command)
        except:
            print("> Ocorreu um erro com o comando de entrada")
            have_errors = True

        if not have_errors and cursor.description != None:
            data = cursor.fetchall()
            headers = [tup[0] for tup in cursor.description]
            print()
            print(tabulate(data, headers=headers))
            print()