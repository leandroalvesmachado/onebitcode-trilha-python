from conexao_pgsql import conn

# Criando um cursor
"""
Cursos é um interador que permite navegar e manipular os registros em um BD
"""
cursor = conn.cursor()

# Lendo dados da tabela
cursor.execute("SELECT * FROM game")
result = cursor.fetchall()

# [(1, 'The Last of Us Part I', 2022, 9.0), (2, 'God of War Ragnarok', 2022, 10.0), ...
print(result)

# Fechando conexão
cursor.close()
conn.close()