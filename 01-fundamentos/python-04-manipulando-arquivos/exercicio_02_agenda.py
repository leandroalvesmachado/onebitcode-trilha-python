import os

def add_contact():
    name = input("Informe o nome:\n")
    address = input("Informe o endereço:\n")
    phone = input("Informe o telefone:\n")

    contact = f"Nome: {name} \n Endereço: {address} \n Telefone: {phone} \n"

    with open("contatos.txt", "a", encoding="utf-8") as file:
        file.write(contact)

def view_contacts():
    if not os.path.exists("contatos.txt"):
        print("Lista de contatos está vazia")
        return

    with open("contatos.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    
    print("Lista de Contatos")
    print(contacts)

def delete_contacts():
    if not os.path.exists("contatos.txt"):
        print("Lista de contatos está vazia")
        return

    with open("contatos.txt", "w", encoding="utf-8") as file:
        file.write("")
    
    print("Contatos deletados com sucesso")