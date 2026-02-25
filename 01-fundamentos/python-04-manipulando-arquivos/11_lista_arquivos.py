"""
Compactando Arquivos em Zip
"""

import glob, os, zipfile

# 1 - Diretório de trabalho atual
os.getcwd()

# 2 - Listar todos os arquivos .txt
for file in glob.glob("*.txt"):
    print(file)
    # exercicio_01.txt
    # 01_escrevendo_arquivo_02.txt

# 3 - Listar todos os arquivos .csv
for file in glob.glob("*.csv"):
    print(file)
    # cursos2.csv
    # cursos.csv
    # cursos3.csv

# 4 - Compactar arquivos .txt
with zipfile.ZipFile("names.zip", "w") as zip:
    for file in glob.glob("*.txt"):
        zip.write(file)

# 5 - Compactar arquivos .csv
with zipfile.ZipFile("courses.zip", "w") as zip:
    for file in glob.glob("*.csv"):
        zip.write(file)

# 6 - Compactar todos os arquivos
with zipfile.ZipFile("todos.zip", "w") as zip:
    for file in glob.glob("*"):
        zip.write(file)