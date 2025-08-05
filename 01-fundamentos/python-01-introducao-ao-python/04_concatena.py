"""Aprendendo a Concatenar Valores."""

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

# Alternativa 1
print("###Dados do Jogo####")
print("====================")
print("Nome do Jogo:", name)
print("Ano do Jogo:", year_launch)
print("Preço do Jogo:", game_price)
print("Avaliação do Jogo:", note_rating)

# Alternativa 2
print("Nome do Jogo:", name, "\n Ano de lançamento:", year_launch,
        "\n Preço do Jogo:", game_price, "\n Avaliação:", note_rating)

# Alternativa 3
print(f"Nome do Jogo: {name}, Ano Lançamento: {year_launch}, Preço do Jogo: {game_price}, Avaliação do Jogo: {note_rating}")
