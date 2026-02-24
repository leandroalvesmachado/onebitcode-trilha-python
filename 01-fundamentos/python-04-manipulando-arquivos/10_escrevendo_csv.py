"""
Escrevendo Dados em CSV.
"""

# Abre o arquivo "cursos2.csv" em modo leitura ("r")
# encoding="utf-8" garante que caracteres com acento sejam lidos corretamente
# O "with" garante que o arquivo será fechado automaticamente ao final do bloco
with open("cursos2.csv", "r", encoding="utf-8") as file: