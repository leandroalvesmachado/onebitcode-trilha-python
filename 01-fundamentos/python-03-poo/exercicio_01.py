"""
Avaliação e Média da Nota de Filmes.

Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes.
Segue o escopo das funcionalidades:

1. Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme passando uma nota com parâmetro e
que essa nota seja salva no atributo específico da classe.

2. Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme.
Obs: Considere criar um atributo específico para esse fim.

3. Para cada filme ter uma nota de avaliação média que consiste na divisão do total de avaliação pelo total de avaliadores.

"""

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