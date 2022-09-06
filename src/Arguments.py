import argparse
import pathlib

def get_arg_parse():
    parser = argparse.ArgumentParser(description="Utilitário para usar SQLITE3")
    subparser = parser.add_subparsers(dest='command')
    parser.add_argument("db", help="Arquivo de banco de dados que será usado", type=pathlib.Path) 
    parser.add_argument("--is-dev", help="Arquivo de banco de dados que será usado", action=argparse.BooleanOptionalAction, type=bool, default=False) 

    execute_subparser = subparser.add_parser("use", help='Argumentos do comando "use"')

    execute_subparser = subparser.add_parser("execute", help='Argumentos do comando "execute"')
    execute_subparser.add_argument("--from-file", help="Executar o conteudo do arquivo especificado no banco de dados", type=pathlib.Path, default='') 
    execute_subparser.add_argument("--statement", help="Comando SQL que será executado no banco de dados", type=str, default='')

    load_subparser = subparser.add_parser("load", help='Argumentos do comando "load"')
    load_subparser.add_argument("--from-file", help="Diretorio do arquivo CSV que será carregado", type=pathlib.Path)
    load_subparser.add_argument("--file-type", help="Extensão do arquivo que será carregado (csv | excel | fixed)", type=str)
    load_subparser.add_argument("--delimiter", help="Delimitador do arquivo CSV", type=str)
    load_subparser.add_argument("--cols-width", help="Comprimento das colunas do arquivo tabular (fixed). Ex: '1,7,23,5,1'", type=str, default="1,1")
    load_subparser.add_argument("--to-table", help="Tabela que será exportada para arquivo", type=str)
    load_subparser.add_argument("--truncate", help="Flag de truncate na tabela", action=argparse.BooleanOptionalAction, type=bool, default=False)
    load_subparser.add_argument("--drop-table", help="Flag de drop table", action=argparse.BooleanOptionalAction, type=bool, default=False)
    load_subparser.add_argument("--header", help="O arquivo possui cabeçalho?", action=argparse.BooleanOptionalAction, type=bool, default=True)
    load_subparser.add_argument("--ignore-first-n-rows", help="Ignorar as primeiras N linhas do arquivo", type=int, default=0)
    load_subparser.add_argument("--ignore-last-n-rows", help="Ignorar as ultimas N linhas do arquivo", type=int, default=0)

    export_subparser = subparser.add_parser("export", help='Argumentos do comando "export"')
    export_subparser.add_argument("--from-table", help="Tabela que será exportada para arquivo", type=str)
    export_subparser.add_argument("--from-sql", help="Diretorio do arquivo SQL que será executado no banco para extrair os dados", type=pathlib.Path)

    return parser