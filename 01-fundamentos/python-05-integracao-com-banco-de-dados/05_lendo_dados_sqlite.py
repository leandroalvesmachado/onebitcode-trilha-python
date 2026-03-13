import sqlite3

# 1 - Conectando ao banco de dados
connection = sqlite3.connect("title.db")

# 2 - Criando um cursor
"""
Cursos é um interador que permite navegar e manipular os registros em um BD
"""
cursor = connection.cursor()

# 3 - Lendo dados da tabela
data = cursor.execute("SELECT * FROM movies")
print(data.fetchall())

# 4 - Iterando os Dados
print("\nIterando os Dados")
for row in cursor.execute("SELECT * FROM movies"):
    print(f"{row}")
    
# 5 - Ordenando pelo Score
print("\nFilmes Ordenados pelo Score")
for row in cursor.execute("SELECT * FROM movies ORDER BY score desc"):
    print(f"{row}")