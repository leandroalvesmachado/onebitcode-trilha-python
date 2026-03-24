from conexao_pgsql import conn

# Criando um cursor
"""
Cursos é um interador que permite navegar e manipular os registros em um BD
"""
cursor = conn.cursor()

sql = """
    UPDATE game SET name = %s WHERE id = %s
"""

cursor.execute(sql, ('Atualizando', 6))
conn.commit()

# Fechando conexão
cursor.close()
conn.close()