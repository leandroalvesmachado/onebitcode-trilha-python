from pathlib import Path

# Define o diretório base onde os arquivos estão localizados
root_dir = Path("dados")

# Cria um gerador que "aponta" para todos os itens dentro da pasta 'dados'
file_paths = root_dir.iterdir()

# O loop 'for' vai iterar sobre cada objeto Path (arquivo ou pasta) encontrado
for path in file_paths:
    nome = path.stem  # path.stem: Pega apenas o nome (ex: "teste")
    extensao = path.suffix  # path.suffix: Pega a extensão com o ponto (ex: ".txt")
    
    # Cria uma nova string para o nome, adicionando o prefixo "new-"
    new_filename = f"new-{nome}{extensao}"
    
    # Imprime no console para controle do usuário
    print(new_filename) 
    # Saídas esperadas: new-teste.txt, new-b.txt, new-a.txt

    # .with_name(): Cria um NOVO objeto Path trocando o nome antigo pelo novo,
    # mas mantendo o mesmo diretório pai ('dados/new-teste.txt')
    new_filepath = path.with_name(new_filename)
    
    # .rename(): Executa a ação real no sistema de arquivos, 
    # movendo/renomeando o arquivo original para o novo caminho
    path.rename(new_filepath)