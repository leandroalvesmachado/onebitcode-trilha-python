"""Utilizando List Comprehension."""
# List Comprehension é uma forma mais curta e legível
# de criar listas em Python, substituindo o uso de loops
# e condicionais tradicionais.

# 1 - Liste os valores de 0 a 10 que sejam menores do que 4.
for i in range(10):
    if i < 4:  # condição: apenas os números menores que 4
        print(i)
        # Saída: 0, 1, 2, 3

# 2 - A mesma coisa acima só que feito com List Comprehension
# Aqui, dentro dos colchetes, criamos a lista em uma única linha.
numbers = [i for i in range(10) if i < 4]
print(numbers)
# Saída: [0, 1, 2, 3]

# Criamos uma lista de jogos
games = ["Mario", "Star Wars", "Donkey Kong", "Kirby"]

# 3 - Filtrar jogos que possuem a letra "a"
# Para cada x (jogo) dentro da lista games, incluímos apenas os que têm "a"
games_new = [x for x in games if "a" in x]
print(games_new)
# Saída: ['Mario', 'Star Wars']

# 4 - Criar uma nova lista com todos os jogos, exceto "Kirby"
# Condição: incluir apenas jogos diferentes de "Kirby"
games_list = [x for x in games if x != "Kirby"]
print(games_list)
# Saída: ['Mario', 'Star Wars', 'Donkey Kong']
