"""Utilizando Principais Métodos da Listas."""

game_list = ["Fifa 23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]

# 1 - Tamanho da lista
print(len(game_list))
# Saída: 4

# 2 - Recupera o indice do item da lista
print(game_list.index("Red Dead 2"))
# Saída: 3

# 3 - Adicionar item ao final da lista
game_list.append("GTA V")
print(game_list)
# Saída: ['Fifa 23', 'Star Wars', 'The Legend of Zelda', 'Red Dead 2', 'GTA V']

# 4 - Ordenar a lista
game_list.sort()
print(game_list)
# Saída: ['Fifa 23', 'GTA V', 'Red Dead 2', 'Star Wars', 'The Legend of Zelda']

# 5 - Copia os itens de uma lista para outra
game_reset = game_list.copy()
game_reset.remove('Fifa 23')
game_reset.remove('Star Wars')
print(game_reset)
# Saída: ['GTA V', 'Red Dead 2', 'The Legend of Zelda']

# 6 - Remove todos os itens da lista
game_list.clear()
print(game_list)
# Saída: []