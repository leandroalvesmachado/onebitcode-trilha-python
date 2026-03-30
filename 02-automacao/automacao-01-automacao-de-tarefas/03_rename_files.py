from pathlib import Path

# Define o diretório base onde os arquivos estão localizados
root_dir = Path("files")

# O método glob("**/*") busca TODOS os arquivos e pastas
# dentro de root_dir, incluindo subpastas (recursivo)
# * → qualquer arquivo/pasta no nível atual
# ** → qualquer nível de subdiretórios (recursivo)
# "**/*" → tudo dentro da pasta, incluindo:
file_paths = root_dir.glob("**/*")

# Itera sobre cada caminho encontrado
for path in file_paths:
    # Imprime o caminho completo (relativo ao root_dir)
    # print(path)

    # checa se é um arquivo
    if path.is_file():
        print(path)
        parent_folder = path.parts[-2]
        new_filename = f'{parent_folder}-{path.name}'
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)