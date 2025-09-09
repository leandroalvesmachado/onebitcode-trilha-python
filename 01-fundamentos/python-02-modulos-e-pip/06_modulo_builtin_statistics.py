"""Módulo Statistic."""

# Importa o módulo statistics, que fornece funções estatísticas como média,
# mediana, moda, desvio padrão etc.
import statistics

# 1 - Aplicar a média
# A média aritmética é a soma dos valores dividida pela qtd de elementos.
# Exemplo: (3 + 2 + 3 + 8 + 9) / 5 = 25 / 5 = 5
print(statistics.mean([3, 2, 3, 8, 9]))
# Saída: 5

# 2 - Aplicar a mediana
# A mediana é o valor que fica no "meio" da lista quando ela está ordenada.
# Lista ordenada: [1, 2, 3, 8, 9]
# O valor central é 3.
print(statistics.median([1, 2, 3, 8, 9]))
# Saída: 3

# Caso a lista tenha um número par de elementos, a mediana
# é a MÉDIA dos dois números centrais.
# Lista ordenada: [1, 2, 3, 7, 8, 9]
# Os dois valores centrais são 3 e 7 → (3 + 7) / 2 = 5
print(statistics.median([1, 2, 3, 7, 8, 9]))
# Saída: 5.0

# 3 - Aplicar a moda
# A moda é o valor que mais aparece em um conjunto de dados.
# Lista: [2, 5, 3, 2, 8, 3, 9, 4, 2, 5, 6]
# O número 2 aparece 3 vezes (mais do que qualquer outro), logo é a moda.
print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4, 2, 5, 6]))
# Saída: 2

# 4 - Aplicar o desvio padrão
"""
O desvio padrão mede a dispersão (variação) dos dados em relação à média.

- Se o desvio padrão é próximo de 0 → os dados estão próximos da média (pouco espalhados).
- Se o desvio padrão é grande → os dados estão bem espalhados.

Exemplo:
Lista = [1,1.5,2,2.5,3,3.5,4,4.5,5]
A média ≈ 3.0
O desvio padrão mede, em média, o "quanto os números se afastam da média".
"""
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]))
# Saída: 1.3693063937629153
