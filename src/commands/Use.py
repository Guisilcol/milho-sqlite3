from argparse import Namespace
import sqlite3
from tabulate import tabulate 

def run(arguments: Namespace):
    CONNECTION = sqlite3.connect(arguments.db)
    
    while(True):        
        try:
            cursor = None
            have_errors = False
            command = input("milho-sqlite3: ")

            if(command.strip().startswith('.exit')):
                break
            elif(command.strip().startswith('.tables ')):
                command = "SELECT name FROM sqlite_master WHERE type='table';"

            elif(command.strip().startswith(".desc ")):
                table = command[6:]
                command = f"PRAGMA table_info('{table}');"
            
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