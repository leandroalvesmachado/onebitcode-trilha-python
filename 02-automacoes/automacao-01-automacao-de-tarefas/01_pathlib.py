from pathlib import Path

# Cria um objeto de caminho. O pathlib ajusta automaticamente as barras 
# de acordo com o sistema operacional (ex: / no Linux ou \ no Windows).
p1 = Path('dados', 'teste.txt')

print(p1)           
# Saída: dados/teste.txt (ou dados\teste.txt no Windows)
# Explicação: Mostra a representação do caminho completo que definimos.

print(type(p1))     
# Saída: <class 'pathlib.PosixPath'> ou <class 'pathlib.WindowsPath'>
# Explicação: Confirma que não é uma string comum, mas um objeto da classe Path.

print(p1.name)      
# Saída: teste.txt
# Explicação: Retorna o nome completo do arquivo (nome + extensão).

print(p1.stem)      
# Saída: teste
# Explicação: Retorna apenas o nome do arquivo, sem a extensão.

print(p1.suffix)    
# Saída: .txt
# Explicação: Retorna apenas a extensão do arquivo.

print(p1.exists())  
# Saída: True ou False
# Explicação: Verifica se o arquivo realmente existe no disco naquele caminho.

# Bloco condicional para leitura segura
if p1.exists():
    # Abre o arquivo para leitura ('r') usando o objeto Path diretamente
    with open(p1, 'r', encoding='utf-8') as file:
        print(file.read())
        # Saída: [O conteúdo que estiver escrito dentro do seu arquivo teste.txt]

# Manipulando diretórios
p2 = Path('dados')
print(list(p2.iterdir()))
# Saída: [PosixPath('dados/teste.txt'), PosixPath('dados/outro_arquivo.csv'), ...]
# Explicação: 'iterdir()' gera um iterador com todos os arquivos e pastas 
# dentro de 'dados'. O 'list()' transforma isso em uma lista visível.