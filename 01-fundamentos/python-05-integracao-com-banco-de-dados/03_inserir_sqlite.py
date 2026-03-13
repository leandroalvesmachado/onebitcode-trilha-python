import sqlite3

# 1 - Conectando ao banco de dados
connection = sqlite3.connect("title.db")

# 2 - Criando um cursor
"""
Cursos é um interador que permite navegar e manipular os registros em um BD
"""
cursor = connection.cursor()

# 3 - Inserindo dados
cursor.execute("""
    INSERT INTO movies (name, year, score) VALUES ('Super Mario Bros', 2023, 9.5)
""")

cursor.execute("""
    INSERT INTO movies (name, year, score) VALUES ('Avatar', 2023, 10.0)
""")

cursor.execute("""
    INSERT INTO movies (name, year, score) VALUES ('Velozes & Furiosos', 2023, 8.5)
""")

# 4 - Gravando Dados no BD
connection.commit()
print('Dados inseridos com sucesso.')

# 5 - Fechando conexão
connection.close()