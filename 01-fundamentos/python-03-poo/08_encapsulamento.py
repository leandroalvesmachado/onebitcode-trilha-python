"""
Fornecendo Maior Segurança com Encapsulamento.

Protegido = Um underline (_) indica que não deveria ser acessado fora da classe ou subclasses (É apenas convenção — ainda pode ser acessado).
Privado = Dois underlines (__) ativam name mangling.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # ficou privado, não é possível mais alterar
    

    def show(self):
        print(f"Nome {self.name} - Salário {self.__salary}")


fulano = Employee("Fulano", 8000)
sicrano = Employee("Sicrano", 18000)

fulano.show()  # Nome Fulano - Salário 8000
sicrano.show()  # Nome Sicrano - Salário 18000

# Não deve permitir isso, usar o encapsulamento para proteger, __ (ficou private)
fulano.__salary = 20000

# Não alterou
fulano.show()  # Nome Fulano - Salário 8000