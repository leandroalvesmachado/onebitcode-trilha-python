"""
Utilizando o Tipo de Dado Lista.

- Listas são coleções ordenadas e mutáveis.
- Podem conter elementos de tipos diferentes (str, int, float, bool, etc.).
"""

# ---------------------------------------------------------
# Criação de uma lista com tipos mistos
# ---------------------------------------------------------
# - String: "Fifa 23"
# - Inteiro: 2022
# - Float: 90.50 (na impressão vira 90.5, pois o Python remove zeros à direita)
# - Boolean: True
game_data = ["Fifa 23", 2022, 90.50, True]

# Exibe a lista completa
print(game_data)
# Saída: ['Fifa 23', 2022, 90.5, True]

game_list = ["Fifa 23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]
print(game_list)

# ---------------------------------------------------------
# 1) Buscar os dois primeiros itens da lista
# ---------------------------------------------------------
# game_list[0:2] usa fatiamento (slice) "início:fim"
# - Início = 0 (inclusivo) -> primeiro elemento
# - Fim    = 2 (exclusivo) -> para antes do índice 2
# Resultado: índices 0 e 1
print(game_list[0:2])
# Saída: ['Fifa 23', 'Star Wars']

# ---------------------------------------------------------
# 2) Buscar o último item da lista
# ---------------------------------------------------------
# Índice negativo -1 referencia o último elemento,
# -2 o penúltimo, e assim por diante.
print(game_list[-1])
# Saída: Red Dead 2

# ---------------------------------------------------------
# 3) Buscar jogos até uma posição (do início até antes do índice 2)
# ---------------------------------------------------------
# Se o "início" for omitido em [:2], o Python assume 0.
# Equivale a game_list[0:2].
print(game_list[:2])
# Saída: ['Fifa 23', 'Star Wars']

# ---------------------------------------------------------
# 4) Buscar jogos de uma posição em diante (do índice 2 até o fim)
# ---------------------------------------------------------
# Se o "fim" for omitido em [2:], o Python vai até o último elemento.
# Resultado: elementos de índice 2 e 3.
print(game_list[2:])
# Saída: ['The Legend of Zelda', 'Red Dead 2']
