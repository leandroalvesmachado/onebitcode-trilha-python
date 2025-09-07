"""
Agendamento de desligamento.

Crie duas funções em python para agendar o desligamento 
do computador em uma hora e meia hora.
"""

import os
import platform

def desligar_em_uma_hora():
    """
    Agenda o desligamento do computador em 1 hora.
    Compatível com Windows e Linux.
    """
    if platform.system() == "Windows":
        os.system("shutdown -s -t 3600")  # 3600 segundos = 1 hora
    else:
        os.system("shutdown -h +60")      # +60 minutos no Linux/macOS

def desligar_em_meia_hora():
    """
    Agenda o desligamento do computador em 30 minutos.
    Compatível com Windows e Linux.
    """
    if platform.system() == "Windows":
        os.system("shutdown -s -t 1800")  # 1800 segundos = 30 minutos
    else:
        os.system("shutdown -h +30")      # +30 minutos no Linux/macOS


def cancelar_desligamento():
    """
    Cancela o desligamento agendado.
    """
    if platform.system() == "Windows":
        os.system("shutdown -a")          # Windows
    else:
        os.system("shutdown -c")          # Linux/macOS


desligar_em_uma_hora()
cancelar_desligamento()
desligar_em_meia_hora()
cancelar_desligamento()