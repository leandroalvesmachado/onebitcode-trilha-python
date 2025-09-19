"""Utilizando construtor e str."""


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


# Criando um objeto da classe Movie
movie = Movie("Super Mario", 2023, False, 10.0, 120)

# Acessando diretamente os atributos do objeto e imprimindo informações
print(f"Filme {movie.name} é de {movie.year_launch} e possui nota {movie.note}")
# Saída: Filme Super Mario é de 2023 e possui nota 10.0

# Usando o método __str__ do objeto (chamado automaticamente pelo print)
print(movie)
# Saída: Filme: Super Mario