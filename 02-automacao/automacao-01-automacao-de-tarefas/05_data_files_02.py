# Importa a classe Path para trabalhar com arquivos e diretórios
from pathlib import Path

# Importa datetime para trabalhar com datas
from datetime import datetime

# Define o diretório raiz onde estão os arquivos
root_dir = Path("files")

# Percorre todos os arquivos e pastas dentro de "files"
# "**/*" significa: todos os níveis (subpastas também)
for path in root_dir.glob("**/*"):
    
    # Verifica se o item atual é um arquivo (ignora pastas)
    if path.is_file():
        
        # Obtém informações do arquivo (metadados)
        stats = path.stat()
        
        # Tempo de criação do arquivo (em segundos desde 1970 - timestamp)
        second_created = stats.st_ctime
        
        # Converte o timestamp para uma data legível
        date_created = datetime.fromtimestamp(second_created)
        
        # Formata a data no padrão: ANO-MES-DIA_HORA_MINUTO_SEGUNDO
        # Ex: 2026-03-30_14_25_10
        date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S')
        
        # Cria o novo nome do arquivo:
        # Ex: 2026-03-30_14_25_10-meuarquivo.txt
        new_filename = f'{date_created_str}-{path.name}'
        
        # Cria o novo caminho com o nome atualizado (mesma pasta)
        new_filepath = path.with_name(new_filename)
        
        # Renomeia o arquivo (move para o novo nome)
        path.rename(new_filepath)