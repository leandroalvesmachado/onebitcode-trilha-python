"""
1 - Cálculo da Distância.

Escreva um programa que pergunte a distância que um passageiro
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50
por km para viagens de até 200 km, e R$ 0,35 para viagens mais longas.

2 - Aumento salário funcionário.

Escreva um programa que pergunte o salário do funcionário
e calcule o valor do aumento. Para salários superiores a
R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, de 15%.
"""

# 1 - Cálculo da Distância.
distance = float(input("Digite a distância a percorrer: \n"))

if distance <= 200:
    ticket = 0.5 * distance
else:
    ticket = 0.35 * distance

print(f"Preço da passagem: R$ {ticket:.2f}")

# 2 - Aumento salário funcionário.
salary = float(input("Digite o salário: \n"))

if salary > 1250:
    increase = 0.10
else:
    increase = 0.15

print(f"Seu aumento será de: R$ {(salary * increase):.2f}")