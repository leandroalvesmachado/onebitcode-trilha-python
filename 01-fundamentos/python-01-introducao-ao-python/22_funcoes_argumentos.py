"""Utilizando Função com Argumentos."""


# 1 - Crie uma função que receba dois argumentos
def full_name(first_name, last_name):
    """Recebe dois argumentos (primeiro nome e sobrenome) e exibe o nome completo."""
    print(f"Nome: {first_name} {last_name}")


# Chamando a função passando dois valores como parâmetros
full_name("Leandro", "Machado")


# 2 - Crie uma função que some dois números via parâmetros
def sum(x, y):
    """Recebe dois números (x e y) como argumentos e retorna a soma deles."""
    return x + y


# Exibindo o resultado da soma de 10 e 50
print(sum(10, 50))  # Saída: 60


# 3 - Argumentos default numa função
def address(country="Brasil"):
    """Exibe o país informado como parâmetro. Caso nenhum valor seja passado, usa o valor padrão."""
    print(f"Eu moro no {country}")


# Chamada sem argumento -> usa o valor padrão "Brasil"
address()

# Chamada passando argumento -> substitui o padrão
address("EUA")
