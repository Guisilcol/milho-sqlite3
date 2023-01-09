"""
    Esse script é responsável por criar o executável do programa.
    Para isso, ele utiliza o pyinstaller e o poetry.
    O pyinstaller é responsável por criar o executável e o poetry é responsável por instalar as dependências do programa.
    Para que o pyinstaller consiga criar o executável, ele precisa que todas as dependências estejam instaladas, assim como os módulos que são importados dinamicamente (--hidden-import).
"""

import subprocess
from os import remove as remove_file
from os.path import exists as path_exists
from shutil import rmtree as remove_folder, make_archive as create_zip, move as move_file

def main():

    hidden_imports = ["openpyxl"]


    # Create the dist folder and the executable file
    print("> Creating the dist folder and the executable file...")
    
    subprocess.run(["poetry", "run", "pyinstaller", "src/milhosqlite3.py", "--onedir", "--noconfirm", "--hidden-import", " ".join(hidden_imports)], shell=True)
    print("> Creating the dist folder and the executable file... OK")

    # Remove the build folder
    print("> Removing the build folder and useless files...")
    remove_file(".\\milhosqlite3.spec")
    remove_folder(".\\build")
    print("> Removing the build folder and useless files... OK")

    # Create the zip file
    print("> Creating the zip file...")
    if path_exists(".\\dist\\milhosqlite3.zip"):
        remove_file(".\\dist\\milhosqlite3.zip")
    create_zip("milhosqlite3", "zip", ".\dist\milhosqlite3")
    move_file(".\milhosqlite3.zip", ".\dist")
    print("> Creating the zip file... OK")

if __name__ == '__main__':
    main()