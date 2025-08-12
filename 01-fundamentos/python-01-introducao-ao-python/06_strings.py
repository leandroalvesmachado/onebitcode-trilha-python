"""Detalhando a Utilização de Strings."""

game_name = 'Fifa 23'
game_name2 = 'fifa 23'

# String multilinha
game_description = '''
    Fifa 23 é um jogo de futebol
    desenvolvido pela EA Sports
    e que possibilita jogar localmente ou online.
                '''
print(game_name)  # Fifa 23
print(game_name == game_name2)  # False, Python é case sensitive
print(game_description)
