"""Instanciando a Classe."""


class Movie:
    """
    Representa um filme.

    Attributes:
        name (str): Nome do filme.
        year_launch (int): Ano de lançamento do filme.
        include_plan (bool): Se está incluído em algum plano.
        note (float): Nota do filme.
        duration_minutes (int): Duração do filme em minutos.
    """

    name = ""
    year_launch = 0
    include_plan = False
    note = 0
    duration_minutes = 0

# Instância de classe
movie = Movie()
movie.name = "Super Mario Bros"
movie.year_launch = 2023
movie.include_plan = False
movie.note = 5.0
movie.duration_minutes = 130

print(movie)
# Saída: <__main__.Movie object at 0x7561a8ebf4d0> (objeto)

print("##Dados do Filme##")
print(f"Nome do filme: {movie.name} \n Ano de Lançamento: {movie.year_launch}")
