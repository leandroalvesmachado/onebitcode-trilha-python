"""
Exemplo de utilização do tipo de dado Dicionário (dict) em Python.

Um dicionário é uma coleção **mutável** e **não ordenada** de pares chave-valor:
- Cada item é definido como: chave: valor
- Chaves devem ser únicas e imutáveis (strings, números, tuplas)
- Valores podem ser de qualquer tipo (números, strings, listas, outros dicionários, etc.)
"""

# Observações importantes sobre dicionários:
# - Ordem dos itens não é garantida em versões antigas do Python (<3.7), mas nas versões atuais ela mantém a ordem de inserção
# - Permite armazenar valores complexos, como listas e outros dicionários
# - Muito útil para representar dados estruturados, como registros de jogos, usuários ou produtos

# Criando um dicionário com informações de um jogo
game_fifa = {
    "name": "Fifa 23",              # Nome do jogo (string)
    "year_launch": 2022,            # Ano de lançamento (inteiro)
    "game_price": 2023,             # Preço do jogo (inteiro)
    "classification": 8.5,          # Classificação do jogo (float)
    "genre": ["esporte", "família"] # Gêneros do jogo (lista de strings)
}

# Imprime o dicionário inteiro
print(game_fifa)
# Saída: {'name': 'Fifa 23', 'year_launch': 2022, 'game_price': 2023, 'classification': 8.5, 'genre': ['esporte', 'família']}

# Quantidade de itens no dicionário (pares chave-valor)
print(len(game_fifa))
# Saída: 5

# Verifica o tipo da variável
print(type(game_fifa))
# Saída: <class 'dict'>

# 1 - Recuperando elementos pelo nome da chave
print(game_fifa['genre'])              # Acessa a lista de gêneros
print(game_fifa.get('classification')) # Método get() é mais seguro, retorna None se não existir a chave

# 2 - Buscando apenas as chaves do dicionário
print(game_fifa.keys())
# Saída: dict_keys(['name', 'year_launch', 'game_price', 'classification', 'genre'])

# 3 - Buscando apenas os valores do dicionário
print(game_fifa.values())
# Saída: dict_values(['Fifa 23', 2022, 2023, 8.5, ['esporte', 'família']])

# 4 - Retorna itens do dicionário como tuplas dentro de uma lista
print(game_fifa.items())
# Saída: dict_items([('name', 'Fifa 23'), ('year_launch', 2022), ('game_price', 2023), ('classification', 8.5), ('genre', ['esporte', 'família'])])

# 5 - Adicionando um novo item no dicionário
game_fifa["players"] = 2
print(game_fifa)
# Saída: {'name': 'Fifa 23', ..., 'players': 2}

# 6 - Atualizando um item existente
game_fifa.update({"players": 1})
print(game_fifa)
# Saída: {'name': 'Fifa 23', ..., 'players': 1}

# 7 - Removendo um item do dicionário
game_fifa.pop("players")
print(game_fifa)
# Saída: {'name': 'Fifa 23', 'year_launch': 2022, 'game_price': 2023, 'classification': 8.5, 'genre': ['esporte', 'família']}
