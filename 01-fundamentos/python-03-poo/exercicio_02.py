"""
Classe Produto e método desconto

Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes.
Segue o escopo das funcionalidades:

1. Cada produto deve ter um preço e um nome.

2. A classe deve ter um método construtor e o método dundle str.

3. A classe deve ter um método para desconto. O método deve receber o desconto em percentual e realizar o 
cálculo de quanto ficaria o preço final com o desconto.
"""

"""This file calculates required dietary requirements for kiwis."""
class Product:
    """Represents a product."""


    def __init__(self, name: str, price: float) -> None:
        """Initialize a Product instance."""
        self.name = name
        self.price = price


    def __str__(self) -> str:
        """Return string representation of the product."""
        return f"Produto {self.name} - R$ {self.price} reais"


    def discount(self, percent_discount: float) -> int:
        """Calculate final price after applying a discount percentage."""
        discount_value = self.price * (percent_discount / 100)
        final_price = self.price - discount_value
        return int(final_price)



xbox = Product("Xbox Series X", 4500)
iphone = Product("Iphone 14", 7500)

print(xbox)
print(iphone)

print(xbox.discount(10))
print(iphone.discount(15))
