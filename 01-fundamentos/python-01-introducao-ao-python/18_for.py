"""Utilizando o Laço de Repetição For."""

# Uma lista com esses elementos
games = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

# 1 - Iterando valores de uma lista
for game in games:
    print(game)

# 2 - Quando a condição for atendida, o loop será encerrado
for game in games:
    if game == "Red Dead 2":
        break # encerra a execução do loop
    print(game)

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
for game in games:
    if game == "Red Dead 2":
        continue
    print(game)

# 4 - Avaliação do jogo
game_name = input("Digite o nome do jogo: \n")
game_rating = int(input("Digite quantas avaliações deseja fazer no jogo: \n"))

sum = 0
for i in range(game_rating):
    note = float(input("Digite a nota para o jogo: \n"))
    sum += note
print(f"Média de avaliação do jogo {game_name} é: {sum/game_rating:.2f}")