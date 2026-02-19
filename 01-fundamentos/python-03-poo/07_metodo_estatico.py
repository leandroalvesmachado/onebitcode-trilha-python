"""
Utilizando Método Estático.

1 - O método estático não utiliza o parâmetro referente a classe.
2 - O método estático pode acessar, mas não pode modificar o estado da classe.
3 - Usamos o decorator @staticmethod para criar um método estático
"""

class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail
    
    @staticmethod
    def courses_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominando o Python", "Módulos e Pip", "Orientação a Objetos"]
        elif trail == "Automação com Python":
            courses = ["Automação de Tarefas", "Web Scraping", "Assistente Virtual"]
        else:
            courses = ["A definir"]
        return courses

# Como chamar o método estático
print(Course.courses_trail("Python Fundamentos"))  # ['Dominando o Python', 'Módulos e Pip', 'Orientação a Objetos']
print(Course.courses_trail("Automação com Python"))  # ['Automação de Tarefas', 'Web Scraping', 'Assistente Virtual']
print(Course.courses_trail("IA"))  # ['A definir']