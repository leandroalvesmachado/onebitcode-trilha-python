"""Módulo Regex I."""

import re

# Texto base usado para os exemplos
text = 'OneBitCode: Transformamos pessoas em programadores sem limites'

# 1 - Encontrar índice inicial e final de uma palavra/frase dentro do texto
# re.search() retorna o primeiro "match" encontrado
match = re.search(r'pessoas em programadores', text)
print('Índice inicial:', match.start())  # .start() -> posição inicial no texto
print('Índice final:', match.end())      # .end() -> posição final no texto
# Exemplo: a substring "pessoas em programadores" começa na posição 26 e vai até 50


# 2 - Procurar o índice onde aparece um ponto "." em uma URL
# Como o "." é um caractere especial nas regex (significa "qualquer caractere"),
# precisamos escapar com "\" para procurar o ponto literal.
site = 'https://onebitcode.com'
match = re.search(r'\.', site)
print(match)  # mostra o objeto Match -> contém a posição (span) e o caractere encontrado
# Saída: <re.Match object; span=(18, 19), match='.'>


# 3 - Buscar todos os caracteres dentro de um intervalo [a-m]
# Aqui criamos um padrão: qualquer letra minúscula entre "a" e "m"
padrao = "[a-m]"
resultado = re.findall(padrao, text)  # retorna uma lista com todas as correspondências
print(text)        # imprime o texto original
print(resultado)   # imprime todas as letras encontradas que estão no intervalo [a-m]
# Exemplo de saída: ['e', 'i', 'd', 'e', 'a', 'f', ...]


# 4 - Verificar se uma string começa com determinado caractere usando ^
# "^A" significa: "a string precisa começar com a letra A"
rule = r'^A'  
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):  # re.match só verifica no INÍCIO da string
        print(f'Corresponde: {f}')
    else:
        print(f'Não corresponde: {f}')
# Apenas a primeira frase corresponde, pois começa com "A"


# 5 - Verificar se uma string termina com determinado caractere usando $
# "!$" significa: "a string precisa terminar com ponto de exclamação"
rule_end = r'!$'
phrases2 = 'O dia está lindo!'
matches = re.search(rule_end, phrases2)
if matches:
    print("Sim, corresponde.")  # Caso termine com !
else:
    print("Não corresponde.")   # Caso contrário
