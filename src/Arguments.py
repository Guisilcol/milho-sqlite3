from argparse import ArgumentParser, BooleanOptionalAction
from pathlib import Path


def get_arg_parse():
    parser = ArgumentParser(description="Utilitário para usar SQLITE3")
    subparser = parser.add_subparsers(dest='command')
    parser.add_argument(
        "db", help="Arquivo de banco de dados que será usado", type=Path)
    parser.add_argument("--is-dev", help="Arquivo de banco de dados que será usado",
                        action=BooleanOptionalAction, type=bool, default=False)

    # EXECUTE
    execute_subparser = subparser.add_parser(
        "use", help='Argumentos do comando "use"')
    execute_subparser = subparser.add_parser(
        "execute", help='Argumentos do comando "execute"')
    execute_subparser.add_argument(
        "--from-file", help="Executar o conteudo do arquivo especificado no banco de dados", type=Path, default='')
    execute_subparser.add_argument(
        "--statement", help="Comando SQL que será executado no banco de dados", type=str, default='')

    # LOAD
    load_subparser = subparser.add_parser(
        "load", help='Argumentos do comando "load"')
    load_subparser.add_argument(
        "--from-file", help="Diretorio do arquivo CSV que será carregado", type=Path)
    load_subparser.add_argument(
        "--file-type", help="Extensão do arquivo que será carregado", type=str, choices=['csv', 'excel', 'fixed'])
    load_subparser.add_argument(
        "--delimiter", help="Delimitador do arquivo CSV", type=str)
    load_subparser.add_argument(
        "--cols-width", help="Comprimento das colunas do arquivo tabular (fixed). Ex: '1,7,23,5,1'", type=str, default="1,1")
    load_subparser.add_argument(
        "--to-table", help="Tabela que será exportada para arquivo", type=str)
    load_subparser.add_argument("--truncate", help="Flag de truncate na tabela",
                                action=BooleanOptionalAction, type=bool, default=False)
    load_subparser.add_argument("--drop-table", help="Flag de drop table",
                                action=BooleanOptionalAction, type=bool, default=False)
    load_subparser.add_argument("--header", help="O arquivo possui cabeçalho?",
                                action=BooleanOptionalAction, type=bool, default=True)
    load_subparser.add_argument(
        "--ignore-first-n-rows", help="Ignorar as primeiras N linhas do arquivo", type=int, default=0)
    load_subparser.add_argument(
        "--ignore-last-n-rows", help="Ignorar as ultimas N linhas do arquivo", type=int, default=0)

    #EXPORT
    export_subparser = subparser.add_parser(
        "export", help='Argumentos do comando "export"')
    export_subparser.add_argument(
        "--sql-file", help="Diretorio do arquivo SQL que será executado no banco para extrair os dados", type=Path, default='.')
    export_subparser.add_argument(
        "--statement", help="Comando SQL que será executado para extrair os dados", type=str)
    export_subparser.add_argument(
        "--to-file", help="Arquivo de output", type=Path)
    export_subparser.add_argument("--type", help="Tipo de arquivo de output (excel, csv)",
                                  type=str,
                                  choices=['excel', 'csv'])
    export_subparser.add_argument(
        "--delimiter", help="Delimitador do arquivo csv", type=str)

    #INDEX
    index_subparser = subparser.add_parser(
        "index", help='Argumentos do comando "index"')
    index_subparser.add_argument(
        "--table", help="Tabela que será criado o index", type=str)
    index_subparser.add_argument(
        "--index", help="Nome do index que será criado", type=str)
    index_subparser.add_argument(
        "--cols", help="Nome das colunas que serão usadas no index. Ex: 'coluna1,coluna4'", type=str, default=None)

    return parser
