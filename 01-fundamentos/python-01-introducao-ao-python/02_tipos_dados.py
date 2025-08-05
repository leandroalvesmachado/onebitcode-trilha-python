"""Tipos de dados primitivos em Python."""

# String (texto)
nome = "Leandro"         # str: sequência de caracteres
mensagem = 'Olá, mundo!'  # também é uma string

# Inteiro
# int: número inteiro, positivo ou negativo
idade = 30

# Ponto flutuante
# float: número com parte decimal
altura = 1.75

# Booleano
# bool: verdadeiro ou falso (True / False)
ativo = True
is_admin = False

# Lista (array mutável)
# list: pode conter qualquer tipo de dado
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4]

# Tupla (sequência imutável)
# tuple: usada para dados que não devem ser alterados
coordenadas = (10.0, 20.0)

# Conjunto (conjunto de valores únicos)
# set: elimina valores duplicados automaticamente
numeros_unicos = {1, 2, 3, 2, 1}

# Dicionário (chave-valor)
pessoa = {
    "nome": "Leandro",
    "idade": 30,
    "altura": 1.75
}  # dict: mapa de chaves para valores

# None (ausência de valor)
endereco = None  # usado quando ainda não há valor definido

# Exemplo de uso e exibição
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print(f"Está ativo? {ativo}")
print(f"Frutas: {frutas}")
print(f"Coordenadas: {coordenadas}")
print(f"Números únicos: {numeros_unicos}")
print(f"Pessoa: {pessoa}")
print(f"Endereço: {endereco}")

print(type(nome))  # <class 'str'>
print(type(idade))  # <class 'int'>
print(type(altura))  # <class 'float'>
print(type(ativo))  # <class 'bool'>
print(type(frutas))  # <class 'list'>
print(type(coordenadas))  # <class 'tuple'>
print(type(numeros_unicos))  # <class 'set'>
print(type(pessoa))  # <class 'dict'>
print(type(endereco))  # <class 'NoneType'>
