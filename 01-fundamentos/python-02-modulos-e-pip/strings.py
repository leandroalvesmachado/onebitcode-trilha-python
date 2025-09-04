"""Módulo String."""


def inverse(string):
    """Retorna o texto invertido."""
    return string[::-1]


# O fatiamento string[::2] começa no índice 0 e pula de 2 em 2.
def even_characters(string):
    """Retorna os caracteres com o índice par."""
    return string[::2]


# O fatiamento string[1::2] começa no índice 1 e pula de 2 em 2.
def odd_characters(string):
    """Retorna os caracteres com o índice ímpar."""
    return string[1::2]
