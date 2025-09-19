"""
Módulo Hashlib.

O módulo hashlib do Python serve para gerar hashes criptográficos (funções de resumo)
de dados, como senhas, arquivos e strings. Ele é muito usado para verificação de integridade, autenticação e segurança.

O que é um hash?

Um hash é uma sequência de caracteres gerada a partir de dados de entrada.
É determinístico → a mesma entrada gera sempre a mesma saída.
É unidirecional → não dá pra "desfazer" o hash e recuperar a entrada original.
"""

import hashlib  # Importa o módulo hashlib para trabalhar com hashes

# Todos os algoritmos disponíveis no sistema (dependem do OpenSSL instalado)
print(hashlib.algorithms_available)

# Todos os algoritmos garantidos pelo Python (funcionam em qualquer plataforma)
print(hashlib.algorithms_guaranteed)

# Criando um objeto SHA-256 vazio
algorithm = hashlib.sha256()
print(algorithm.digest)  # Mostra o método digest do objeto SHA-256 (ainda não gera hash)

# Mensagem que queremos transformar em hash (é necessário converter para bytes)
message = "A melhor forma de prever o futuro é criá-lo".encode()

# Alimenta o objeto SHA-256 com a mensagem em bytes
algorithm.update(message)

# Obtém o hash SHA-256 da mensagem em formato hexadecimal
print(algorithm.hexdigest())  
# Exemplo de saída: f11ff5f17fece76cb03b57b61961dedaae827f7e96e69653162272d165bde83e

# Criando um objeto MD5 vazio
md5 = hashlib.md5()

# Alimenta o objeto MD5 com a mesma mensagem
md5.update(message)

# Obtém o hash MD5 da mensagem em formato hexadecimal
print(md5.hexdigest())  
# Exemplo de saída: 70ac1d219eb0a8f0e4eeaf9e2788195b
