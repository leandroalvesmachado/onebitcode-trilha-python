"""
Módulo de strings.

Escreva um módulo em python para tratar algumas strings e
que possua as seguintes funcionalidades:
1 - Inverter uma string de trás pra frente.
2 - Retornar apenas letras com índice par.
3 - Retornar apenas letras com índice ímpar.
"""

import strings

name = "Olá mundo"

# 1 - Inverter uma string de trás pra frente.
print(strings.inverse(name))
# Saída: odnum álO

# 2 - Retornar apenas letras com índice par.
print(strings.even_characters(name))
# Saída: Oámno

# 3 - Retornar apenas letras com índice ímpar.
print(strings.odd_characters(name))
# Saída: l ud
