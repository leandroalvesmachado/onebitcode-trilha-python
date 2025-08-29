"""Utilizando Funções com *args e **kwargs.

*args: argumentos posicionais variáveis (empacotados em uma tupla).
**kwargs: argumentos nomeados/keyword variáveis (empacotados em um dicionário).
"""


def soma(*numeros):
    """
    Soma uma quantidade variável de números.

    Parâmetros:
        *numeros: qualquer quantidade de valores numéricos (int/float).

    Funcionamento:
        - O Python empacota todos os argumentos posicionais recebidos
          em uma tupla chamada 'numeros'.
        - Iteramos por essa tupla e acumulamos o total.
    """
    total = 0
    for n in numeros:
        # Equivalente a: total = total + n
        total += n
    print(f"Soma é {total}")


# Chamadas de exemplo: note que a quantidade de argumentos varia
soma(7)                 # -> Soma é 7
soma(8, 7)              # -> Soma é 15
soma(4, 5, 9)           # -> Soma é 18
soma(6, 8, 3, 1)        # -> Soma é 18


def apresentacao(**dados):
    """
    Exibe pares chave-valor vindos de argumentos nomeados.

    Parâmetros:
        **dados: qualquer quantidade de pares chave=valor.
                 Ex.: nome="Python", categoria="Backend"

    Funcionamento:
        - O Python empacota todos os argumentos nomeados em um dicionário
          chamado 'dados'.
        - Iteramos por items() para obter (chave, valor) e exibir.
    """
    for chave, valor in dados.items():
        print(f"{chave} - {valor}")


print("###### Curso ######")

# Passando argumentos nomeados (viram um dicionário dentro da função)
apresentacao(nome="Python", categoria="Backend", nivel="Iniciante")


# BÔNUS: exemplo com parâmetros fixos + *args + **kwargs
def exemplo_completo(titulo, *args, destacado=False, **kwargs):
    """
    Mostra como misturar parâmetros fixos, *args e **kwargs.

    - 'titulo' é obrigatório e posicional.
    - '*args' recebe extras posicionais (tupla).
    - 'destacado' é nomeado com default (bool).
    - '**kwargs' recebe extras nomeados (dicionário).
    """
    print(f"Título: {titulo}")
    print(f"Posicionais extras (args): {args}")
    print(f"Destacado? {destacado}")
    print(f"Nomeados extras (kwargs): {kwargs}")


# Exemplo de chamada:
exemplo_completo(
    "Relatório",
    1, 2, 3,                      # vão para *args
    destacado=True,               # parâmetro nomeado com default
    autor="Leandro", versao="1.0" # vão para **kwargs
)
