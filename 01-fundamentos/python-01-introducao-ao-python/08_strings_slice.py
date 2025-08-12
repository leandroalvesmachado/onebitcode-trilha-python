"""Gerando Substrings a partir de uma String (Fatiamento)."""

game_name = 'Fifa23'
game_description = '''
Fifa 23 é um jogo de futebol desenvolvido pela EA Sports
e que possibilita jogar localmente ou online.
'''

# string[início:fim] - índice começa com 0 | índice final -1

# Busque toda string a partir da primeira posição
print(game_name[0:])  # Fifa23

# Busque toda string até a posição 3
print(game_name[:3])  # Fif

# Busque toda string da primeira até a posição 6
print(game_name[0:6])  # Fifa23

"""
string[início:fim:passo]
    - índice começa com 0 | índice final -1 |
    passo - determina o incremento. Por padrão esse número é o 1
"""

# Busque toda a string de 2 em 2 caracteres.
print(game_name[::2])  # Ff2

# Imprime os caracteres nos índices ímpares
print(game_name[1::2])  # ia3

# Inverta uma string de trás pra frente
print(game_name[::-1])  # 32afiF
