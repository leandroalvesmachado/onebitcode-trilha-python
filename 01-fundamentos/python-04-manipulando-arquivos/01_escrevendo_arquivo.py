"""
Escrevendo em Arquivo Txt

r - leitura (Abre para leitura, Arquivo precisa existir, Se o arquivo não existir FileNotFoundError)
w - escrita (Abre para escrita, Cria o arquivo se não existir, Apaga todo conteúdo anterior se já existir)
a - append (Adiciona conteúdo ao final, Cria o arquivo se não existir, Não apaga o conteúdo anterior)
"""

name = input("Digite o seu nome: \n")

# Alternativa 1
# file = open("01_escrevendo_arquivo_01.txt", "w")
# file.write(name)
# file.close()

# Alternativa 2
with open("01_escrevendo_arquivo_02.txt", "a") as file:
    file.write(f"{name}\n")