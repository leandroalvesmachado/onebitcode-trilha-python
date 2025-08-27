"""Utilizando Funções."""


def welcome():
    """Exibe uma mensagem de boas-vindas."""
    print("Hello World")


def sum():
    """Soma dois números fixos e retorna o resultado."""
    return 5 + 4


def create_game():
    """Solicita dados de um jogo e os exibe na tela."""
    game_name = input("Digite o nome do jogo: \n")
    release_year = int(input("Digite o ano de lançamento do jogo: \n"))
    game_price = float(input("Digite o preço do jogo: \n"))

    print(game_name)
    print(release_year)
    print(f"{game_price}")



welcome()
sum()
create_game()
