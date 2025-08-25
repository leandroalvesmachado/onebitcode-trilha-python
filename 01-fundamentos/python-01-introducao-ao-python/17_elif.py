"""Utilizando Condições com If, Elif e Else."""

number1 = float(input("Digite o número 1: \n"))
number2 = float(input("Digite o número 2: \n"))
operation = input("Digite a operação a realizar (+ - * /)\n")

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2
else:
    print("Operação inválida")
    result = 0

print(f"Resultado: {result}")
