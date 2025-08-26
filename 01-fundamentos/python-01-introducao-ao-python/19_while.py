"""Utilizando o Laço de Repetição While."""
game_name = input("Digite o nome do jogo: \n")
qtd_rating = 0
total_rating = 0
rating = 0
average = 0

while rating != -1:
    rating = float(input("Informe a nota do jogo: \n"))

    if rating != -1:
        # total_rating = total_rating + rating
        total_rating += rating
        # qtd_rating = qtd_rating + 1
        qtd_rating += 1
        average = total_rating / qtd_rating

print(f"Média das avaliações do jogo {game_name} é {average:.2f}")