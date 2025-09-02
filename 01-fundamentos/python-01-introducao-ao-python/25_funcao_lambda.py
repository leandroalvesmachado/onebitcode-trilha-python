"""Função Lambda (funções anônimas)."""
# Lambdas são funções curtas, sem nome, criadas em uma única linha.
# Sintaxe: lambda argumentos: expressão
# Elas são úteis quando queremos uma função simples e rápida.

# 1 - Função de potência de número
power = lambda num: num ** 2

print(power(5))  # 25
print(power(9))  # 81

# 2 - Função para saber se o número é par
pair = lambda x: x%2==0

print(pair(27))  # False (27 é ímpar)
print(pair(30))  # True  (30 é par)

# 3 - Função para dividir dois números
divNum = lambda x,y : x/y

print(divNum(10, 2))  # 5.0
print(divNum(7, 2))   # 3.5

# 4 - Função para inverter string
# s[::-1] usa fatiamento (slice) para inverter a string.
reverse = lambda s: s[::-1]

print(reverse("Função"))     # "oãçnuF"
print(reverse("Tecnologia")) # "aigolonceT"