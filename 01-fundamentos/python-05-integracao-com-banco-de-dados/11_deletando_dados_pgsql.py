from conexao_pgsql import conn

# Criando um cursor
"""
Cursos é um interador que permite navegar e manipular os registros em um BD
"""
cursor = conn.cursor()

sql = """
    DELETE FROM game WHERE id = %s
"""

cursor.execute(sql, (6,))
conn.commit()

# Fechando cursos e conexão
cursor.close()
conn.close()