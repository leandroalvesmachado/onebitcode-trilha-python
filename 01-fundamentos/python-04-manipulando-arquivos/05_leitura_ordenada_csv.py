"""
Ordenando Valores na Leitura.
"""

# Lista
cursos = []

# O "with" garante que o arquivo será fechado automaticamente após o uso
with open("cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        cursos.append(f"{language}-{category}")

for curso in sorted(cursos):
    print(curso)
    # JavaScript- Back-end
    # JavaScript- Front-end
    # JavaScript- Mobile
    # Python- Análise de Dados
    # Python- Automação
    # Python- IA
    # Ruby- Back-end

# parametro reverse=True inverte o resultado
for curso in sorted(cursos, reverse=True):
    print(curso)
    # Ruby- Back-end
    # Python- IA
    # Python- Automação
    # Python- Análise de Dados
    # JavaScript- Mobile
    # JavaScript- Front-end
    # JavaScript- Back-end