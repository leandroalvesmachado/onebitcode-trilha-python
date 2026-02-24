"""
Ordenando Valores na Leitura dos Dados.

A função sorted() no Python é usada para ordenar iteráveis (listas, tuplas, strings, dicionários etc.) e 
retorna uma nova lista ordenada, sem alterar o original.

sorted(iterable, key=None, reverse=False)

iterable → lista, tupla, string etc.
key → função usada como critério de ordenação
reverse → False (crescente) ou True (decrescente)
"""

names = []

# O "with" garante que o arquivo será fechado automaticamente após o uso
with open("01_escrevendo_arquivo_02.txt", "r", encoding="utf-8") as file:
    for line in file:
        # O método rstrip() serve para remover espaços (ou caracteres específicos) do final de uma string.
        # Ele não altera o começo da string — apenas o lado direito (right strip).
        names.append(line.rstrip())

print(names)  # ['Leandro', 'Roberto', 'Valdir', 'Conceição', 'Sábado']

print(sorted(names))  # ['Conceição', 'Leandro', 'Roberto', 'Sábado', 'Valdir']

# outra forma de ordenar diretamente no loop
for name in sorted(names):
    print(name)