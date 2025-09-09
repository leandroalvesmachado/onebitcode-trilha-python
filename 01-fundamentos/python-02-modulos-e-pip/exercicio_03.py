"""
Verificar conteúdo da String.

Escreva um programa em Python para verificar se uma string contém apenas 
um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).
"""

import re  # importa o módulo de expressões regulares

def check_character(string):
    # Criamos uma regra com regex:
    # [^a-zA-Z0-9]
    # -> ^ dentro dos colchetes significa NEGAÇÃO
    # -> ou seja: "qualquer caractere que NÃO seja letra maiúscula (A-Z),
    #    nem letra minúscula (a-z) e nem número (0-9)"
    rule = re.compile(r'[^a-zA-Z0-9]')

    # Procuramos na string se existe algum caractere que viole a regra
    # (ou seja, que esteja FORA de a-z, A-Z ou 0-9)
    string = rule.search(string)

    # Se encontrar algo, retorna False. Se não encontrar, retorna True.
    # bool(string) -> será True se achou um caractere inválido
    # not bool(string) -> inverte: True se a string é válida
    return not bool(string)


# Testes
print(check_character("ABCDEFabcdef123450"))  
# Saída: True 
# -> todos os caracteres são válidos (somente letras e números)

print(check_character("*&%@#!}{"))  
# Saída: False
# -> contém caracteres inválidos (símbolos especiais)
