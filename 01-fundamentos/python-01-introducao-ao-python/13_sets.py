"""
Exemplo de utilização do tipo de dado Set em Python.

Um set (conjunto) é uma coleção **não ordenada** de elementos **únicos**, ou seja:
- Não aceita elementos duplicados
- Não mantém ordem
- Pode ser alterado (é mutável), mas não permite fatiamento
"""

# Observações importantes sobre sets:
# - Não é possível acessar elementos por índice ou fatiamento
# - Ideal para armazenar itens únicos e realizar operações como união, interseção, diferença
# - Elementos devem ser imutáveis (strings, números, tuplas), não pode adicionar listas ou dicionários diretamente

# Criando um set de jogos
games_set = {"Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2"}

# Imprime o set
print(games_set)
# Saída: {'The Legend of Zelda', 'Star Wars', 'Red Dead 2', 'Fifa23'}
# Note que a ordem pode mudar e o "Red Dead 2" duplicado foi removido

# Verifica a quantidade de elementos únicos no set
print(len(games_set))
# Saída: 4

# Exemplo 1: sets consideram True e 1 como o mesmo elemento
example_set = {"Fifa23", True, 1, 90.50} 
print(example_set)
# Saída: {True, 90.5, 'Fifa23'}
# - True e 1 são considerados iguais, por isso só aparece uma vez
# - 90.50 é considerado como float separado

# Exemplo 2: adicionando um item ao set
games_set.add("Resident Evil 4")
print(games_set)
# Saída: {'Red Dead 2', 'The Legend of Zelda', 'Fifa23', 'Resident Evil 4', 'Star Wars'}

# Exemplo 3: adicionando itens de outro set (update)
games_set.update(example_set)
print(games_set)
# Todos os elementos de example_set são adicionados, sem duplicatas

# Exemplo 4: removendo elementos do set
games_set.remove(True)  # Remove o True (ou 1)
games_set.remove(90.5)  # Remove o float
print(games_set)
# Saída: {'Resident Evil 4', 'The Legend of Zelda', 'Star Wars', 'Red Dead 2', 'Fifa23'}
