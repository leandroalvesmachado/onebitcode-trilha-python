"""
Lendo Dados de um Arquivo

r - leitura (Abre para leitura, Arquivo precisa existir, Se o arquivo não existir FileNotFoundError)
w - escrita (Abre para escrita, Cria o arquivo se não existir, Apaga todo conteúdo anterior se já existir)
a - append (Adiciona conteúdo ao final, Cria o arquivo se não existir, Não apaga o conteúdo anterior)
"""

# O "with" garante que o arquivo será fechado automaticamente após o uso
with open("01_escrevendo_arquivo_02.txt", "r", encoding="utf-8") as file:
    for line in file:
        # O método rstrip() serve para remover espaços (ou caracteres específicos) do final de uma string.
        # Ele não altera o começo da string — apenas o lado direito (right strip).
        print(f"Olá, {line.rstrip()}")