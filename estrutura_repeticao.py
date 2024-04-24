a = int(input("informe um numero inteiro."))

print(a)

a += 1
print (a)

a += 1
print (a)

# comando for (para repetições de limite conhecido)

letras = input("informe um texto: ")

VOGAIS = "AEIOU"

for letra in letras:
    if letra.upper() in VOGAIS:
        print (letra, end="")

print()