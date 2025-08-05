"""Lendo dados com o Input."""

# Solicita ao usuário que digite o nome do jogo e armazena como string na variável 'name'
name = input("Digite o nome do jogo \n")

# Solicita o ano de lançamento do jogo.
# A entrada é convertida para inteiro (int), pois anos são representados por números inteiros
year_launch = int(input("Digite o ano de lançamento\n"))

# Solicita o preço do jogo.
# A entrada é convertida para float, pois preços podem conter casas decimais
game_price = float(input("Digite o preço do jogo\n"))

# Solicita a nota de avaliação do jogo
# Converte para float, pois notas podem ter casas decimais (ex: 8.5)
note_rating = float(input("Digite a nota de avaliação do jogo\n"))

# Exibe na tela os dados informados pelo usuário
print(name)          # Nome do jogo
print(year_launch)   # Ano de lançamento
print(game_price)    # Preço do jogo
print(note_rating)   # Nota de avaliação
