import unittest
from src.modules.subprocess import Subprocess
import os

class LoadCommandTest(unittest.TestCase):

    ENTRYPOINT = 'python D:/Projetos/milho-sqlite3/src/milhosqlite3.py'
    COMMAND = 'load'
    CSV_FILEPATH = 'D:/Projetos/milho-sqlite3/teste.csv'
    EXCEL_FILEPATH = 'D:/Projetos/milho-sqlite3/teste.xlsx'
    FIXED_WIDTH_FILEPATH = 'D:/Projetos/milho-sqlite3/teste.delimited'
    DB_FILEPATH = 'D:/Projetos/milho-sqlite3/teste.db'
    
    def test_load_command_with_csv_input_file(self):
        args = f'''{LoadCommandTest.ENTRYPOINT} {LoadCommandTest.COMMAND} '''
        args += f'''--from-file="{LoadCommandTest.CSV_FILEPATH}" '''
        args += f'''--file-type="csv" '''
        args += f'''--delimiter="|" '''
        args += f'''--to-table="teste_csv" '''
        args += f'''{LoadCommandTest.DB_FILEPATH}'''

        self.assertEqual(Subprocess.call_subprocess(args), 0)
        
    def test_load_command_with_excel_input_file(self):
        args = f'''{LoadCommandTest.ENTRYPOINT} {LoadCommandTest.COMMAND} '''
        args += f'''--from-file="{LoadCommandTest.EXCEL_FILEPATH}" '''
        args += f'''--file-type="excel" '''
        args += f'''--to-table="teste_excel" '''
        args += f'''{LoadCommandTest.DB_FILEPATH}'''

        self.assertEqual(Subprocess.call_subprocess(args), 0)

    def test_load_command_with_fixed_input_file(self):
        args = f'''{LoadCommandTest.ENTRYPOINT} {LoadCommandTest.COMMAND} '''
        args += f'''--from-file="{LoadCommandTest.FIXED_WIDTH_FILEPATH}" '''
        args += f'''--file-type="fixed" '''
        args += f'''--to-table="teste_fixed" '''
        args += f'''--cols-width="8,7,12" '''
        args += f'''{LoadCommandTest.DB_FILEPATH}'''

        self.assertEqual(Subprocess.call_subprocess(args), 0)

    def test_load_command_with_header_false(self):
        args = f'''{LoadCommandTest.ENTRYPOINT} {LoadCommandTest.COMMAND} '''
        args += f'''--from-file="{LoadCommandTest.EXCEL_FILEPATH}" '''
        args += f'''--file-type="excel" '''
        args += f'''--to-table="teste_header_false" '''
        args += f'''--no-header '''
        args += f'''{LoadCommandTest.DB_FILEPATH}'''

        self.assertEqual(Subprocess.call_subprocess(args), 0)

    def test_load_command_with_header_true(self):
        args = f'''{LoadCommandTest.ENTRYPOINT} {LoadCommandTest.COMMAND} '''
        args += f'''--from-file="{LoadCommandTest.EXCEL_FILEPATH}" '''
        args += f'''--file-type="excel" '''
        args += f'''--to-table="teste_header_true" '''
        args += f'''--header '''
        args += f'''{LoadCommandTest.DB_FILEPATH}'''

        self.assertEqual(Subprocess.call_subprocess(args), 0)

    def test_load_command_with_ignore_first_n_rows(self):
        args = f'''{LoadCommandTest.ENTRYPOINT} {LoadCommandTest.COMMAND} '''
        args += f'''--from-file="{LoadCommandTest.EXCEL_FILEPATH}" '''
        args += f'''--file-type="excel" '''
        args += f'''--to-table="teste_ignore_first_n_rows" '''
        args += f'''--ignore-first-rows=2 '''
        args += f'''{LoadCommandTest.DB_FILEPATH}'''

        self.assertEqual(Subprocess.call_subprocess(args), 0)

    def test_load_command_with_ignore_last_n_rows(self):
        args = f'''{LoadCommandTest.ENTRYPOINT} {LoadCommandTest.COMMAND} '''
        args += f'''--from-file="{LoadCommandTest.EXCEL_FILEPATH}" '''
        args += f'''--file-type="excel" '''
        args += f'''--to-table="teste_ignore_last_n_rows" '''
        args += f'''--ignore-last-rows=2 '''
        args += f'''{LoadCommandTest.DB_FILEPATH}'''

        self.assertEqual(Subprocess.call_subprocess(args), 0)

    def test_load_command_with_drop_table_true(self):
        args = f'''{LoadCommandTest.ENTRYPOINT} {LoadCommandTest.COMMAND} '''
        args += f'''--from-file="{LoadCommandTest.EXCEL_FILEPATH}" '''
        args += f'''--file-type="excel" '''
        args += f'''--to-table="teste_drop_table_true" '''
        args += f'''--drop-table '''
        args += f'''{LoadCommandTest.DB_FILEPATH}'''

        self.assertEqual(Subprocess.call_subprocess(args), 0)

    def test_load_command_with_drop_table_false(self):
        args = f'''{LoadCommandTest.ENTRYPOINT} {LoadCommandTest.COMMAND} '''
        args += f'''--from-file="{LoadCommandTest.EXCEL_FILEPATH}" '''
        args += f'''--file-type="excel" '''
        args += f'''--to-table="teste_drop_table_false" '''
        args += f'''--no-drop-table '''
        args += f'''{LoadCommandTest.DB_FILEPATH}'''

        self.assertEqual(Subprocess.call_subprocess(args), 0)

    def test_load_command_with_truncate_true_and_table_not_exists(self):
        args = f'''{LoadCommandTest.ENTRYPOINT} {LoadCommandTest.COMMAND} '''
        args += f'''--from-file="{LoadCommandTest.EXCEL_FILEPATH}" '''
        args += f'''--file-type="excel" '''
        args += f'''--to-table="teste_truncate_true" '''
        args += f'''--truncate '''
        args += f'''{LoadCommandTest.DB_FILEPATH}'''

        self.assertEqual(Subprocess.call_subprocess(args), 1)

    def test_load_command_with_truncate_false(self):
        args = f'''{LoadCommandTest.ENTRYPOINT} {LoadCommandTest.COMMAND} '''
        args += f'''--from-file="{LoadCommandTest.EXCEL_FILEPATH}" '''
        args += f'''--file-type="excel" '''
        args += f'''--to-table="teste_truncate_false" '''
        args += f'''--no-truncate '''
        args += f'''{LoadCommandTest.DB_FILEPATH}'''

        self.assertEqual(Subprocess.call_subprocess(args), 0)


if __name__ == '__main__':
    if os.path.exists(LoadCommandTest.DB_FILEPATH):
        os.remove(path=LoadCommandTest.DB_FILEPATH)

    unittest.main()