"""Módulo Webbrowser."""

# No WSL (Ubuntu/Debian dentro do Windows), o webbrowser.open() não consegue
# abrir diretamente o navegador, porque não há ambiente gráfico disponível.
# O jeito certo é usar o wslview, que serve justamente para abrir links
# no navegador do Windows a partir do WSL.

# Importa o módulo webbrowser da biblioteca padrão do Python.
# Esse módulo permite abrir URLs no navegador padrão do sistema.
import webbrowser

# Variável de controle para o loop.
done = False

# Loop principal: roda até que 'done' seja definido como True.
while not done:
    # Exibe o menu de opções para o usuário.
    print("O que você deseja fazer? \n")
    print("1. Aprender Python")
    print("2. Aprender sobre módulos")
    print("3. Aprender Python, Fullstack JS e No Code")
    print("4. Sair")

    # Aguarda a escolha do usuário digitada no terminal.
    choice = input(">")

    # Se a escolha for "1", abre o site oficial do Python.
    if choice == "1":
        webbrowser.open("https://www.python.org")

    # Se a escolha for "2", abre a documentação dos módulos do Python.
    elif choice == "2":
        webbrowser.open("https://docs.python.org/3/py-modindex.html")

    # Se a escolha for "3", abre o site da OneBitCode sobre programação.
    elif choice == "3":
        webbrowser.open("https://pages.onebitcode.com")

    # Se a escolha for "4", muda 'done' para True e encerra o loop.
    elif choice == "4":
        done = True

    # Se o usuário digitar algo diferente de 1 a 4, mostra mensagem de erro.
    else:
        print("Opção inválida. Escolha uma opção entre 1 a 4")
