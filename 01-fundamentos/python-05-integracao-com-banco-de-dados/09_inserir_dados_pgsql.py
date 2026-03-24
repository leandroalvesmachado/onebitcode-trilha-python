from conexao_pgsql import conn

# Criando um cursor
"""
Cursos é um interador que permite navegar e manipular os registros em um BD
"""
cursor = conn.cursor()

games = [
    ('Star Wars Survivor', 2023, 9.5),
    ('The Last of Us', 2023, 8.5)
]

for game in games:
    cursor.execute("""
        INSERT into game(name, year, score) VALUES (%s, %s, %s)"""
    , game)

conn.commit()

# Fechando conexão
cursor.close()
conn.close()