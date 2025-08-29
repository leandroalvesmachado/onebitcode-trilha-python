"""Utilizando Função Recursiva."""


def factorial(num: int) -> int:
    """
    Calcula o fatorial de um número de forma recursiva.

    Exemplos:
        3 -> 3 * 2 * 1 = 6
        5 -> 5 * 4 * 3 * 2 * 1 = 120

    :param num: Número inteiro para calcular o fatorial.
    :return: Resultado do fatorial.
    """
    if num == 1:
        return 1
    return num * factorial(num - 1)


number = int(input("Digite o número para fatorial: "))
print(f"O fatorial de {number} é: {factorial(number)}")


def total_sum(num: int) -> int:
    """
    Calcula a soma de todos os números inteiros até o valor informado.

    Exemplos:
        3 -> 3 + 2 + 1 = 6
        5 -> 5 + 4 + 3 + 2 + 1 = 15

    :param num: Número inteiro até onde será feita a soma.
    :return: Resultado da soma.
    """
    if num == 1:
        return 1
    return num + total_sum(num - 1)


num = int(input("Digite um número para soma: "))
print(f"A soma total do {num} é: {total_sum(num)}")
