"""Criando o primeiro módulo."""

# Importa o módulo inteiro chamado 'calc'
import calc

# Importa apenas a função 'div' do módulo 'calc'
from calc import div

# Chama a função 'sum' do módulo 'calc' passando os argumentos 2 e 4
# Espera-se que some os dois números → saída: 6
print(calc.sum(2, 4))

# Chama a função 'sub' do módulo 'calc' passando os argumentos 2 e 4
# Deve calcular 2 - 4 → saída: -2
print(calc.sub(2, 4))

# Chama a função 'mult' do módulo 'calc' passando os argumentos 2 e 4
# Deve calcular 2 * 4 → saída: 8
print(calc.mult(2, 4))

# Aqui a função 'div' foi importada de duas formas:
# 1) via 'import calc' → calc.div(2, 4)
# 2) via 'from calc import div' → poderia usar apenas div(2, 4)
# Neste caso está usando pela 1ª forma → saída: 0.5
print(calc.div(2, 4))
