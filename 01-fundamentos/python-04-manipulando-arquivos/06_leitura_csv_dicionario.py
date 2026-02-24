"""
Transformando em Dicionário.
"""

# Lista
cursos = []

# O "with" garante que o arquivo será fechado automaticamente após o uso
with open("cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        curso = {}  # dicionario

        curso["language"] = language
        curso["category"] = category
        cursos.append(curso)

# Imprimindo dicionario
print(cursos)
#  [{'language': 'Python', 'category': ' Automação'}, {'language': 'Python', 'category': ' Análise de Dados'}, {'language': 'Python', 'category': ' IA'}, {'language': 'JavaScript', 'category': ' Back-end'}, {'language': 'JavaScript', 'category': ' Mobile'}, {'language': 'JavaScript', 'category': ' Front-end'}, {'language': 'Ruby', 'category': ' Back-end'}]

for curso in cursos:
    # Acessando dicionario
    print(f"{curso['language']} - {curso['category']}")
    # Python -  Automação
    # Python -  Análise de Dados
    # Python -  IA
    # JavaScript -  Back-end
    # JavaScript -  Mobile
    # JavaScript -  Front-end
    # Ruby -  Back-end