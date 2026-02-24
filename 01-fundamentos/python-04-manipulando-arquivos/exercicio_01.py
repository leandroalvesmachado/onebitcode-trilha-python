"""
Lendo n linhas de um arquivo

Escreva um programa Python para ler as primeiras n linhas de um arquivo.
    - O nome do arquivo e a quantidade de linhas devem ser passadas via parâmetro na função.
"""

def file_read_from_line(fname, n_lines):
    # Importa a função islice da biblioteca itertools.
    # islice permite "fatiar" iteradores (como arquivos) sem carregar tudo na memória.
    from itertools import islice
    
    # Abre o arquivo no modo leitura ("r")
    # encoding="utf8" garante que caracteres especiais (acentos, etc.) sejam lidos corretamente
    # O "with" garante que o arquivo será fechado automaticamente após o uso
    with open(fname, "r", encoding="utf8") as file:
        # islice(file, n_lines) pega apenas as primeiras n_lines linhas do arquivo
        # Isso evita ler o arquivo inteiro desnecessariamente
        for line in islice(file, n_lines):
            # Imprime cada linha lida
            # Observação: a linha já vem com quebra de linha (\n),
            # por isso o print já pula automaticamente para a próxima linha
            print(line)

# Chama a função passando:
# "exercicio_01.txt" -> nome do arquivo
# 5 -> quantidade de linhas que queremos ler
file_read_from_line("exercicio_01.txt", 5)