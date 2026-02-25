"""
Escrevendo Dados em CSV.
Este programa solicita ao usuário o nome de uma linguagem
e sua categoria, e salva essas informações em um arquivo CSV.
"""

# Importa a biblioteca padrão do Python para manipular arquivos CSV
import csv  

# Solicita ao usuário o nome da linguagem
# O \n quebra a linha após a mensagem
name = input("Informe o nome da linguagem que deseja aprender:\n")

# Solicita ao usuário a categoria da linguagem
category = input("Qual categoria que a linguagem se encaixa:\n")

# Abre (ou cria) o arquivo "cursos3.csv"
# "a" = modo append → adiciona conteúdo ao final do arquivo sem apagar o que já existe
# encoding="utf-8" permite salvar caracteres especiais (acentos, ç, etc.)
# O "with" garante que o arquivo será fechado automaticamente após o uso
with open("cursos3.csv", "a", encoding="utf-8") as file:
    
    # Cria um objeto writer responsável por escrever no formato CSV
    # lineterminator="\n" evita linhas em branco extras (principalmente no Windows)
    writer = csv.writer(file, lineterminator="\n")
    
    # Escreve uma nova linha no arquivo CSV
    # Os valores são passados em forma de lista
    # O csv.writer automaticamente separa os valores por vírgula
    writer.writerow([name, category])