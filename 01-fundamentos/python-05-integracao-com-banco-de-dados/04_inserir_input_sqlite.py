import sqlite3

# 1 - Conectando ao banco de dados
connection = sqlite3.connect("title.db")

# 2 - Criando um cursor
"""
Cursos é um interador que permite navegar e manipular os registros em um BD
"""
cursor = connection.cursor()

# 3 - Solicitando dados do usuario
name = input("Nome do Filme:\n")
year = int(input("Ano do Filme:\n"))
score = float(input("Nota do Filme:\n"))

# 4 - Inserindo dados
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES (?,?,?)
""", (name, year, score))

# 5 - Gravando Dados no BD
connection.commit()
print('Dados inseridos com sucesso.')

# 6 - Fechando conexão
connection.close()