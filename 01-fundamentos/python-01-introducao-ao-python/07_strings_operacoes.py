"""Utilizando Operações com Strings."""

# String multilinha
game_description = '''
    Fifa 23 é um jogo de futebol
    desenvolvido pela EA Sports
    e que possibilit
'''
line = '#'
game_name = "Fifa"
game_version = "23"
game_fullname = game_name + game_version

print(line*30)  # ############################## , 30 vezes o símbolo
print(game_fullname)
print(game_description)
# Procurar string dentro de outra string, True ou False
print("Fifa" in game_description)  # True
print("futebol" in game_description)  # True
print(line*30)  # ############################## , 30 vezes o símbolo
