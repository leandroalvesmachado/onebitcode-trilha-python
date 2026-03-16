import sqlite3

# 1 - Conectando ao banco de dados
connection = sqlite3.connect("title.db")

# 2 - Criando um cursor
cursor = connection.cursor()

# 3 - Solicitando Dados do Usuário
id = int(input("Informe o id do filme que deseja deletar:\n"))

# 4 - Deletando Dados
cursor.execute("""
    DELETE FROM movies WHERE id = ?
""", (id,))

connection.commit()
print('Dado removido com sucesso.')

# 5 - Fechando conexão
connection.close()