"""
Utilizando o Módulo CSV.
"""
import csv  # Importa a biblioteca padrão do Python para trabalhar com arquivos CSV

# Criamos uma lista vazia.
# Ela irá armazenar vários dicionários (um para cada linha do CSV).
cursos = []

# Abre o arquivo "cursos2.csv" em modo leitura ("r")
# encoding="utf-8" garante que caracteres com acento sejam lidos corretamente
# O "with" garante que o arquivo será fechado automaticamente ao final do bloco
with open("cursos2.csv", "r", encoding="utf-8") as file:
    
    # DictReader transforma cada linha do CSV em um dicionário
    # IMPORTANTE: o CSV precisa ter cabeçalho (ex: language,category)
    reader = csv.DictReader(file)

    # Percorre cada linha do arquivo
    # Cada "row" já é um dicionário
    for row in reader:
        print(row)

        # Exemplo de saída:
        # {'language': 'Python', 'category': ' Automação'}
        # {'language': 'Python', 'category': ' Análise de Dados'}
        # {'language': 'Python', 'category': ' IA'}
        # {'language': 'JavaScript', 'category': ' Back-end'}
        # {'language': 'JavaScript', 'category': ' Mobile'}
        # {'language': 'JavaScript', 'category': ' Front-end'}
        # {'language': 'Ruby', 'category': ' Back-end'}

        # Aqui criamos um novo dicionário manualmente
        # Pegamos os valores usando as chaves do CSV
        cursos.append({
            "language": row["language"],
            "category": row["category"]
        })

# Agora vamos ordenar a lista de dicionários

# sorted() cria uma NOVA lista ordenada
# key=lambda curso: curso["language"]
# -> diz que a ordenação será baseada na chave "language"
# reverse=True -> ordena em ordem decrescente (Z → A)
for curso in sorted(cursos, key=lambda curso: curso["language"], reverse=True):
    
    # Acessando os valores do dicionário
    print(f"{curso['language']}-{curso['category']}")

    # Saída esperada (ordem decrescente por linguagem):
    # Ruby-Back-end
    # Python-Automação
    # Python-Análise de Dados
    # Python-IA
    # JavaScript-Back-end
    # JavaScript-Mobile
    # JavaScript-Front-end