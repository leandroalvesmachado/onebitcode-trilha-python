"""Módulo Math."""

import math   # Importa o módulo math, que fornece funções matemáticas úteis.

# 1 - Acessar o número Pi
print(math.pi)            # Valor de PI completo: 3.141592653589793
print(f"{math.pi:.2f}")   # Valor de PI formatado com 2 casas decimais: 3.14

# 2 - Acessar o número de Euler (constante matemática e ≈ 2.718...)
print(math.e)             # Saída: 2.718281828459045
print(f"{math.e:.2f}")    # Formatado com 2 casas decimais: 2.72

# 3 - Arredondando número para cima e para baixo
number_one = 10.4
print(math.ceil(number_one))   # math.ceil() arredonda para cima → 11
print(math.floor(number_one))  # math.floor() arredonda para baixo → 10

# 4 - Fatorial de um número
# O usuário digita um número, e o programa calcula o fatorial dele.
# Exemplo: se o usuário digitar 5 → 5! = 5*4*3*2*1 = 120
number_two = int(input("Digite um número para o fatorial: \n"))
print(math.factorial(number_two))

# 5 - Potência de números
# math.pow(base, expoente) → retorna a base elevada ao expoente
print(math.pow(5, 5))   # 5^5 = 3125.0 (float).
# Obs: diferente do operador ** que retorna int se possível.

# 6 - Raiz quadrada
print(math.sqrt(169))   # math.sqrt(x) → retorna a raiz quadrada de x → 13.0

# 7 - Máximo divisor comum (MDC)
# Útil para simplificação de frações
mdc = math.gcd(25, 120)  # Maior divisor comum entre 25 e 120 é 5
print(mdc)

# 8 - Logaritmos
print(math.log(10))  # logaritmo natural de 10 (base e) ≈ 2.302585092994046
print(math.log(10, 3))  # logaritmo de 10 na base 3 ≈ 2.095903274289385
