"""
1 - Substituindo caractere repetido
Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de 
seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

Ex: fifa 23 → fi#a 23, restart→ resta#t

2 - Troca de caracteres
Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço 
e troque os dois primeiros caracteres de cada string.

Ex: abc xyz → xyc abz
"""

# =========================================================
# 1 - Substituindo caractere repetido
# =========================================================

# Texto base
name = "Fifa 23"

# Pega o primeiro caractere da string (índice 0) e o transforma em minúsculo.
# Aqui, name[0] é 'F', então .lower() transforma em 'f'.
character = name[0].lower()

# Substitui TODAS as ocorrências do caractere em minúsculo pela string '$'.
# Obs.: Isso não afeta o 'F' maiúsculo original, apenas o 'f' minúsculo.
new_name = name.replace(character, '$')

# Constrói a nova string: 
# mantém o primeiro caractere original (em minúsculo) e junta o resto da string modificada a partir do índice 1.
new_game = character + new_name[1:]

# Exibe o resultado da substituição (o '$' no lugar dos 'f' minúsculos)
print(new_name)  # Saída esperada: Fi$a 23


# =========================================================
# 2 - Troca de caracteres
# =========================================================

# Duas strings iniciais
st1 = "abc"
st2 = "xyz"

# Cria nova string pegando:
# - Os dois primeiros caracteres de st2 (st2[:2] → 'xy')
# - O último caractere de st1 (st1[2:] → 'c')
# Resultado: "xy" + "c" = "xyc"
new_st1 = st2[:2] + st1[2:]

# Cria nova string pegando:
# - Os dois primeiros caracteres de st1 (st1[:2] → 'ab')
# - O último caractere de st2 (st2[2:] → 'z')
# Resultado: "ab" + "z" = "abz"
new_st2 = st1[:2] + st2[2:]

# Exibe as duas novas strings no formato "xyc abz"
print(f"{new_st1} {new_st2}")  # Saída esperada: xyc abz
