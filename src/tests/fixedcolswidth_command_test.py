import unittest
from test_modules.subprocess import Subprocess

class FixedColsWidthTest(unittest.TestCase):

    ENTRYPOINT = 'python D:/Projetos/milho-sqlite3/src/milhosqlite3.py'
    COMMAND = 'fixedcolswidth'
    #CSV_FILEPATH = 'D:/Projetos/milho-sqlite3/src/tests/test_content/teste.csv'
    #EXCEL_FILEPATH = 'D:/Projetos/milho-sqlite3/src/tests/test_content/teste.xlsx'
    FIXED_WIDTH_FILEPATH = 'D:/Projetos/milho-sqlite3/src/tests/test_content/fixed_width_cols.txt'
    FIXED_WIDTH_FILEPATH_2 = 'D:/Projetos/milho-sqlite3/src/tests/test_content/fixed_width_cols_2.txt'
    #DB_FILEPATH = 'D:/Projetos/milho-sqlite3/src/tests/test_content/teste.db'
    
    def test_load_command_with_csv_input_file(self):
        args = f'''{FixedColsWidthTest.ENTRYPOINT} {FixedColsWidthTest.COMMAND} '''
        args += f'''--file="{FixedColsWidthTest.FIXED_WIDTH_FILEPATH}" '''
        args += f'''--row-number=1 '''
        args += f'''--separator=" " '''
        args += f'''--count-separator'''
        args += f''' --is-dev'''

        args2 = f'''{FixedColsWidthTest.ENTRYPOINT} {FixedColsWidthTest.COMMAND} '''
        args2 += f'''--file="{FixedColsWidthTest.FIXED_WIDTH_FILEPATH_2}" '''
        args2 += f'''--row-number=1 '''
        args2 += f'''--separator=" " '''
        args2 += f'''--count-separator'''
        args2 += f''' --is-dev'''

        self.assertEqual(Subprocess.call_subprocess(args), 0)
        self.assertEqual(Subprocess.call_subprocess(args2), 0)


if __name__ == '__main__':
    unittest.main()