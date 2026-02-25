import os

def add_contact():
    name = input("Informe o nome:\n")
    address = input("Informe o endereço:\n")
    phone = input("Informe o telefone:\n")

    contact = f"Nome: {name} \n Endereço: {address} \n Telefone: {phone} \n"

    with open("contatos.txt", "a", encoding="utf-8") as file:
        file.write(contact)

def view_contact():
    if not os.path.exists("contatos.txt"):
        print("Lista de contatos está vazia")