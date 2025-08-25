"""
Utilizando Dicionários Aninhados

O que é pprint (pretty-print)

O módulo pprint (“pretty print”) formata estruturas Python (dicts, listas, tuplas…) de forma legível, 
quebrando linhas e alinhando chaves/valores.

É muito útil quando você imprime dicionários aninhados ou listas grandes: com print() 
fica uma linha só; com pprint fica organizado.
"""

import pprint 

games_dict = {
    "fifa 23" : {
        "yearLaunch" : 2022,
        "classification" : 8.5,
        "genre": ["esporte", "família"]
    },
    "mario odyssey" : {
        "yearLaunch" : 2017,
        "classification" : 10.0,
        "genre": ["aventura", "3d"]
    },
    "donkey kong country" : {
        "yearLaunch" : 1996,
        "classification" : 9.5,
        "genre": ["aventura", "plataforma"]
    }
}

# print(games_dict)

# Instanciar um "formatador" com opções
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(games_dict)

# Ordenar chaves alfabeticamente e recuar 2 espaços
pprint.pprint(games_dict, indent=2, sort_dicts=True)

# Respeitar ordem de inserção (Python 3.7+), largura 60 colunas
pprint.pprint(games_dict, width=60, sort_dicts=False)

# Instância configurada (reutilizável)
pp = pprint.PrettyPrinter(indent=2, width=60, sort_dicts=False)
pp.pprint(games_dict)

# 1 - Buscando informação dentro de um dicionário
print(games_dict["mario odyssey"]["genre"])

# 2 - Adicionando novo item
games_dict["mario odyssey"]["players"] = 1
print(games_dict['mario odyssey'])

# 3 - Excluindo um dicionário
del games_dict["fifa 23"]
pp.pprint(games_dict)