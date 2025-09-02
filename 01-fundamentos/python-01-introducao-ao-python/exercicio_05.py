"""
1 - Conta letras maiúsculas e minúsculas.

Escreva uma função Python que receba uma string e conte
o número de letras maiúsculas e minúsculas desta string.

2 - Lista números pares e ímpares de uma lista.

Escreva uma função Python para imprimir os números pares e
ímpares em duas listas separadas para cada uma.
"""


# 1 - Conta letras maiúsculas e minúsculas.
def conta_maiusculas_minusculas(texto):
    """Conta letras maiúsculas e minúsculas."""
    # Inicializa contadores
    maiusculas = 0
    minusculas = 0

    # Percorre cada caractere da string
    for char in texto:
        if char.isupper():      # Verifica se é letra maiúscula
            maiusculas += 1
        elif char.islower():    # Verifica se é letra minúscula
            minusculas += 1

    # Retorna os resultados em forma de dicionário
    return {
        "Maiúsculas": maiusculas,
        "Minúsculas": minusculas
    }


# Testando a função
texto = "Python É Muito Legal!"
resultado = conta_maiusculas_minusculas(texto)

print(f"Texto: {texto}")
print(f"Número de maiúsculas: {resultado['Maiúsculas']}")
print(f"Número de minúsculas: {resultado['Minúsculas']}")
# Texto: Python É Muito Legal!
# Número de maiúsculas: 4
# Número de minúsculas: 13


# 2 - Lista números pares e ímpares de uma lista.
def separar_pares_impares(lista):
    """Lista números pares e ímpares de uma lista."""
    # Cria duas listas vazias
    pares = []
    impares = []

    # Percorre cada número da lista
    for num in lista:
        if num % 2 == 0:   # Se for par
            pares.append(num)
        else:              # Caso contrário, ímpar
            impares.append(num)

    # Imprime as duas listas
    print("Números pares:", pares)
    print("Números ímpares:", impares)

    # Também pode retornar as listas, caso precise usá-las
    return pares, impares


# Testando a função
numeros = [10, 21, 4, 45, 66, 93, 1, 2, 7]
separar_pares_impares(numeros)
# Números pares: [10, 4, 66, 2]
# Números ímpares: [21, 45, 93, 1, 7]
