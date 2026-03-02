import os
from fpdf import FPDF
from num2words import num2words
from datetime import date

# 1 - Variáveis
base_dir = os.path.dirname(__file__)
cliente = input("Informe o nome do cliente:\n")
consulta = input("Informe o tipo da consulta:\n")
consulta_valor = input("Informe o valor da consulta:\n")
consulta_valor_msg = f"{consulta_valor} reais"
consulta_valor_extenso = num2words(float(consulta_valor), lang="pt-br")
consulta_valor_extenso_msg = f"{consulta_valor_extenso} reais"
data = date.today()
dia = data.day
mes = data.month
ano = data.year

# 2 - Layout do Recibo
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "", 20)

# imagem na mesma pasta do .py
image_path = os.path.join(base_dir, "rec.jpg")
pdf.image(image_path, x=0, y=0)

# cliente
pdf.text(80, 86, cliente)

# consulta
pdf.text(162, 45, consulta_valor_msg)
pdf.text(80, 108, consulta_valor_extenso_msg)
pdf.text(80, 135, consulta)

# data
pdf.set_text_color(255, 255, 255)
pdf.text(30, 193, str(dia))
pdf.text(50, 193, str(mes))
pdf.text(70, 193, str(ano))

# saída na mesma pasta do .py
nome_arquivo = f"recibo_{cliente.strip()}_{dia}_{mes}_{ano}.pdf"
output_path = os.path.join(base_dir, nome_arquivo)
pdf.output(output_path)

print("Recibo gerado com sucesso")