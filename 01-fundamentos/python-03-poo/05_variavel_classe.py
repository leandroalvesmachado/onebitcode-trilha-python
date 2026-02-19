"""
Utilizando Variável de Classe.
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

    # Variável de Classe (variável comum para todos os objetos da classe Movie)
    platform = "OneBitCodeFilmes"
    
    def __init__(self, name, year_launch, include_plan, duration_minutes):
        # Construtor da classe. É chamado automaticamente quando criamos um objeto Movie.
        # Permite inicializar os atributos do objeto com os valores passados como argumentos.
        self.name = name
        self.year_launch = year_launch
        self.include_plan = include_plan
        self.total_evaluation = 0
        self.duration_minutes = duration_minutes
        self.evaluators = 0
    

    def __str__(self):
        # Método especial que define como o objeto será representado como string.
        # Chamado, por exemplo, quando usamos print(objeto)
        return f"Filme: {self.name}"


    def technical_sheet(self):
        # Método para exibir ficha do filme
        # Método de Classe
        print("## Dados do Filme ##")
        print(f"Plataforma: {Movie.platform}") # imprimindo variável de classe
        print(f"Nome do Filme: {self.name}")
        print(f"Ano de Lançamento: {self.year_launch}")
        print(f"Está no plano? {self.include_plan}")
        print(f"Avaliação do Filme: {self.total_evaluation}")
        print(f"Duração do Filme: {self.duration_minutes}")
        print(f"Total de Avaliadores: {self.evaluators}")


    def evaluate(self, note):
        self.total_evaluation += note # total_evaluation = total_evaluation + note
        self.evaluators += 1 # evaluators = evaluators + 1
    

    def average(self):
        print(f"Média do Filme {self.name}: {self.total_evaluation / self.evaluators}")


mario = Movie("Super Mario Bros", 2023, False, 135)

# aplicando notas
mario.evaluate(9.5)
mario.evaluate(10.0)

mario.technical_sheet()
## Dados do Filme ##
# Plataforma: OneBitCodeFilmes
# Nome do Filme: Super Mario Bros
# Ano de Lançamento: 2023
# Está no plano? False
# Avaliação do Filme: 19.5
# Duração do Filme: 135
# Total de Avaliadores: 2

mario.average()
# Média do Filme Super Mario Bros: 9.75

# Alterando a variável de classe (alterou para todos os objetos abaixo)
Movie.platform = "MGM"

mario.technical_sheet()
## Dados do Filme ##
# Plataforma: MGM
# Nome do Filme: Super Mario Bros
# Ano de Lançamento: 2023
# Está no plano? False
# Avaliação do Filme: 19.5
# Duração do Filme: 135
# Total de Avaliadores: 2
