"""
Métodos Getter e Setter.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # ficou privado
    
    def show(self):
        print(f"Nome {self.name} - Salário {self.__salary}")

    # Método para buscar o dado
    def get_salary(self):
        return self.__salary
    
    # Método para modificar o atributo privado
    def set_salary(self, salary):
        self.__salary = salary


fulano = Employee("Fulano", 8000)
fulano.show()  # Nome Fulano - Salário 8000

# Alterando valor do atributo privado com o método setter
fulano.set_salary(25000)

# Alterou
fulano.show()  # Nome Fulano - Salário 25000