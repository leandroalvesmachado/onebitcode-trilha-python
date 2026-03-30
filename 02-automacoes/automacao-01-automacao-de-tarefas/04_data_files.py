from pathlib import Path
from datetime import datetime

# Cria um objeto Path apontando para:
# files/dados2/teste.txt (caminho RELATIVO)
path = Path("files", "dados2", "teste.txt")

# Apenas imprime o caminho (não verifica se existe)
print(path)  # files/dados2/teste.txt

# Aqui ele tenta acessar informações do arquivo no sistema
# (tamanho, data de modificação, etc.)
print(path.stat())
# os.stat_result(
#     st_mode=33188, st_ino=385939, st_dev=2096, 
#     st_nlink=1, st_uid=1000, st_gid=1000, st_size=0, st_atime=1774814443, 
#     st_mtime=1774814443, st_ctime=1774814443)

# Obtém informações do arquivo/sistema (metadados)
# Isso retorna um objeto do tipo os.stat_result
# com dados como tamanho, datas, permissões, etc.
stats = path.stat()

# Pega o tempo de "criação" do arquivo
# No Linux isso normalmente NÃO é a criação real,
# e sim a última mudança de metadados (ctime = change time)
# O valor vem em formato timestamp (segundos desde 1970 - epoch)
second_created = stats.st_ctime

# Converte o timestamp (número) para um objeto datetime
# Isso transforma algo como 1710000000 em uma data legível
date_created = datetime.fromtimestamp(second_created)

# Formata a data para string no padrão desejado
# %Y = ano (2026), %m = mês (01-12), %d = dia (01-31)
# %H = hora (00-23), %M = minuto, %S = segundo
# Exemplo final: "2026-03-29_14:30:00"
date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S')

# Imprime todas as informações do stat (estrutura completa)
print(stats)

# Imprime o timestamp bruto (número em segundos)
print(second_created)

# Imprime a data em formato datetime (mais legível)
print(date_created)

# Imprime a data formatada como string
print(date_created_str)