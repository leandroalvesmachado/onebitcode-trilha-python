"""Principais Métodos em Strings."""

# Nome do jogo
game_name = 'Fifa 23'

# Descrição do jogo (string multilinha)
game_description = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports,
e que possibilita jogar 
localmente ou online.
'''

# Exibe o nome do jogo em maiúsculas
print(game_name.upper())  # "FIFA 23"

# Exibe o nome do jogo em minúsculas
print(game_name.lower())  # "fifa 23"

# Exibe a string com apenas a primeira letra maiúscula
print(game_name.capitalize())  # "Fifa 23"

# Exibe cada palavra com a primeira letra maiúscula
print(game_name.title())  # "Fifa 23"

# Centraliza o texto em 10 caracteres, preenchendo com '-'
print(game_name.center(10, '-'))  # "--Fifa 23-"

# Retorna o índice da primeira ocorrência da letra "f" (case sensitive)
print(game_name.find("f"))  # Retorna -1 se não encontrar

# Conta quantas vezes o caractere 'a' aparece
print(game_description.count('a'))

# Conta quantas vezes o caractere 'A' maiúsculo aparece
print(game_description.count('A'))

# Substitui "Fifa" por "Pes" na descrição
print(game_name.replace("Fifa", "Pes"))

# Divide o texto em uma lista, usando a vírgula como separador
# [
#   'Fifa 23 é um jogo de futebol desenvolvido pela EA Sports',
#   'e que possibilita jogar localmente ou online.'
# ]
print(game_description.split(','))
