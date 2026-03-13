import sqlite3

# 1 - Conectando ao banco de dados
connection = sqlite3.connect("title.db")

# 2 - Criando um cursor
"""
Cursos é um interador que permite navegar e manipular os registros em um BD
"""
cursor = connection.cursor()

# 3 - Criando a tabela