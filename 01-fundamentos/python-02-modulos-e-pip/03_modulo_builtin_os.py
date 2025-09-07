"""
Módulo OS.

O módulo os é um módulo builtin do Python que permite a interação com o sistema operacional.

Funcionalidades principais:
- Criar, remover e navegar entre diretórios.
- Listar arquivos e pastas.
- Acessar variáveis de ambiente.
- Executar comandos do sistema.
- Manipular caminhos de arquivos de forma independente do sistema operacional
  (funciona em Windows, Linux e macOS).

Exemplos de uso:
----------------
import os

# Obter o diretório atual de trabalho
print(os.getcwd())

# Listar arquivos e pastas no diretório atual
print(os.listdir())

# Criar e remover diretório
os.mkdir("nova_pasta")
os.rmdir("nova_pasta")

# Trabalhar com caminhos
caminho = os.path.join("pasta", "arquivo.txt")
print(caminho)

# Acessar variável de ambiente
usuario = os.getenv("USER") or os.getenv("USERNAME")
print(usuario)

# Executar comando no sistema
os.system("echo Hello, World!")
"""

import os

# 1 - Consultar funcionalidades do módulo os
# help('os')

# 2 - Retornar a pasta atual
print(os.getcwd())
# Saída: /var/www/html/onebitcode-trilha-python

# 3 - Listar arquivos e pastas da pasta atual
print(os.listdir())

# 4 - Apresentar versão do SO (Somente windows comando "ver")
os.system('ver')

# 4 - Apresentar versão do SO (Linux)
# Nome do sistema
print("Sistema operacional:", os.name)          # 'nt' (Windows) ou 'posix' (Linux/macOS)

# Informações detalhadas
import platform
print("Plataforma:", platform.system())
print("Versão:", platform.version())
print("Release:", platform.release())
print("Detalhes completos:", platform.platform())

# Sistema operacional: posix
# Plataforma: Linux
# Versão: #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025
# Release: 6.6.87.2-microsoft-standard-WSL2
# Detalhes completos: Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35

# 6 - Limpar o terminal (Windows)
os.system('cls')

# 7 - Limpar o terminal (Linux)
os.system('clear')