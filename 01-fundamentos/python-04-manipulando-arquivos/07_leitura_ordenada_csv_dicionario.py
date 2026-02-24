"""
Ordenando Valores no Dicionário.
"""

# Criamos uma LISTA vazia.
# Ela irá armazenar vários dicionários (um para cada linha do CSV).
cursos = []

# O "with" abre o arquivo e garante que ele será fechado automaticamente.
# "r" -> modo leitura
# encoding="utf-8" -> permite ler acentos corretamente
with open("cursos.csv", "r", encoding="utf-8") as file:
    # Percorre o arquivo linha por linha
    for line in file:
        # Remove a quebra de linha (\n) do final
        # Divide a linha usando vírgula como separador
        # Exemplo:
        # "Python, Automação"
        # vira:
        # language = "Python"
        # category = " Automação"
        language, category = line.rstrip().split(",")

        # Cria um dicionário vazio
        curso = {}

        # Adiciona chave "language" com o valor da linguagem
        curso["language"] = language
        # Adiciona chave "category" com o valor da categoria
        curso["category"] = category

        # Adiciona o dicionário dentro da lista
        cursos.append(curso)

# Imprime a lista completa de dicionários
print(cursos)

# Resultado:
# [
#   {'language': 'Python', 'category': ' Automação'},
#   {'language': 'Python', 'category': ' Análise de Dados'},
#   ...
# ]

# Função que retorna o valor da chave "language"
# Será usada como critério de ordenação
def get_language(course):
    return course["language"]

# Função que retorna o valor da chave "category"
# Poderia ser usada para ordenar por categoria
def get_category(course):
    return course["category"]

# sorted() ordena a lista
# key=get_language significa:
# "use o retorno da função get_language como critério de ordenação"
for curso in sorted(cursos, key=get_language):
    
    # Acessando valores do dicionário
    # curso['language'] -> valor da linguagem
    # curso['category'] -> valor da categoria
    print(f"{curso['language']} - {curso['category']}")

    # Resultado ordenado por linguagem:
    # JavaScript -  Back-end
    # JavaScript -  Mobile
    # JavaScript -  Front-end
    # Python -  Automação
    # Python -  Análise de Dados
    # Python -  IA
    # Ruby -  Back-end