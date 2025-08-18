""" 
Exemplo de utilização do tipo de dado Tupla em Python.

Uma tupla é uma coleção imutável de itens, ou seja, você não pode alterar, adicionar ou remover elementos depois de criada.
"""

# Observações importantes sobre tuplas:
# - Não é possível adicionar valores (tupla é imutável)
# - Não é possível remover valores
# - Não é possível ordenar os elementos diretamente
# - Pode conter elementos duplicados (como "Red Dead 2" neste exemplo)
# - Pode ser usada para armazenar dados heterogêneos (diferentes tipos)

# Criando uma tupla de jogos
games_tuple = ("Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2")

# Imprime a tupla inteira
print(games_tuple)
# Saída: ('Fifa23', 'Red Dead 2', 'Star Wars', 'The Legend of Zelda', 'Red Dead 2')

# Verifica o tipo da variável
print(type(games_tuple))
# Saída: <class 'tuple'>

# Acessando itens por índice (index) - fatiamento (slicing)
# Buscando os dois primeiros itens da tupla
print(games_tuple[0:2])
# Saída: ('Fifa23', 'Red Dead 2')

# Buscando o último item da tupla usando índice negativo
print(games_tuple[-1])
# Saída: 'Red Dead 2'

# Fatiamento: jogos até a posição 2 (não inclui o índice 2)
print(games_tuple[:2])
# Saída: ('Fifa23', 'Red Dead 2')

# Fatiamento: jogos a partir da posição 2 até o final
print(games_tuple[2:])
# Saída: ('Star Wars', 'The Legend of Zelda', 'Red Dead 2')

# Recupera o índice do item "Fifa23" na tupla
print(games_tuple.index("Fifa23"))
# Saída: 0
