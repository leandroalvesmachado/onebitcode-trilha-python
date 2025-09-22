"""Utilizando métodos."""


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

    def __init__(self, name, year_launch, include_plan, note, duration_minutes):
        # Construtor da classe. É chamado automaticamente quando criamos um objeto Movie.
        # Permite inicializar os atributos do objeto com os valores passados como argumentos.
        self.name = name
        self.year_launch = year_launch
        self.include_plan = include_plan
        self.note = note
        self.duration_minutes = duration_minutes
    

    def __str__(self):
        # Método especial que define como o objeto será representado como string.
        # Chamado, por exemplo, quando usamos print(objeto)
        return f"Filme: {self.name}"


    def technical_sheet(self):
        # Método para exibir ficha do filme
        # Método de Classe
        print("##Dados do Filme##")
        print(f"Nome do Filme: {self.name}")
        print(f"Ano de Lançamento: {self.year_launch}")
        print(f"Está no plano? {self.include_plan}")
        print(f"Avaliação do Filme: {self.note}")
        print(f"Duração do Filme: {self.duration_minutes}")


# Criando um objeto da classe Movie

movie_mario = Movie("Super Mario", 2023, False, 10.0, 120)
movie_mario.technical_sheet()
# ##Dados do Filme##
# Nome do Filme: Super Mario
# Ano de Lançamento: 2023
# Está no plano? False
# Avaliação do Filme: 10.0
# Duração do Filme: 120


movie_top = Movie("Top Gun", 2025, False, 10.0, 160)
movie_top.technical_sheet()
# ##Dados do Filme##
# Nome do Filme: Top Gun
# Ano de Lançamento: 2025
# Está no plano? False
# Avaliação do Filme: 10.0
# Duração do Filme: 160