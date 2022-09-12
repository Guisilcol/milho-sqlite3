# milho-sqlite3
Esse projeto foi criado como um "quebra-galho" para facilitar a carga de arquivos de dados (csv, fixed file e excel) para dentro de banco de dados SQLITE3. 
Foi criado pela necessidade de unificar e analisar diversos arquivos diferentes em ambientes que não se tem disponiveis ferramentas apropriadas para isso. 

Dentro da pasta "dist" haverá o build da última versão da aplicação, contendo: 
    1 - milhosqlite3onefile.exe -> Um executável "all-in-one", ou seja, para usar ele apenas faça o download desse arquivo e execute. Ele é mais demorado em comparação ao próximo item
    2 - milhosqlite3 -> pasta que contém o executável (milhosqlite3.exe) e todas as suas dependências. Sua inicialização em comparação a proposta anterior é muito mais rápida.

Foi usado o módulo virtualenv para o desenvolvimento da aplicação.
