"""
Trabalhando com arquivos CSV
"""

# O "with" garante que o arquivo será fechado automaticamente após o uso
with open("cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        # rstrip() remove espaços em branco e a quebra de linha (\n) no final da string.
        # split(",") divide a linha em partes usando a vírgula como separador.
        # O resultado é uma lista (list) com os valores da linha.
        row = line.rstrip().split(",")

        # Exibe a lista resultante
        print(row)
        # ['Python', ' Automação']
        # ['Python', ' Análise de Dados']
        # ['Python', ' IA']
        # ['JavaScript', ' Back-end']
        # ['JavaScript', ' Mobile']
        # ['JavaScript', ' Front-end']
        # ['Ruby', ' Back-end']

        # row é uma LISTA.
        # Índices da lista:
        # row[0] -> primeiro elemento
        # row[1] -> segundo elemento
        # Aqui estamos acessando apenas o PRIMEIRO elemento da lista
        # Python, Python, Python, JavaScript, JavaScript, JavaScript, Ruby
        print(row[0])

        print(f"{row[0]} - {row[1]}")  # Ruby - Back-end

        # split(",")
        # Divide a string usando vírgula como separador
        # Resultado: ['Python', ' Automação']
        language, category = line.rstrip().split(",")

        # Aqui acontece o DESEMPACOTAMENTO:
        # O primeiro valor da lista vai para a variável "language"
        # O segundo valor da lista vai para a variável "category"
        print(language)  # Python
        print(category)  #  Automação