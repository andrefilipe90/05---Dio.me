'''opcao = -1

print("Escolha o que deseja fazer:\n")
while opcao != 0:
    opcao = int(input("[1]sacar\n[2]Extrato\n[0]Sair\n"))
    
    if opcao == 1:
        print("sacando")
    elif opcao == 2:
        print("Extrato:")

while True:
    numero = int(input("informe um numero:"))

    if numero == 10:
        break
numero = 0

if numero in range(0,10):
    if numero == 2:
        continue
    print(numero)'''

for numero in range(20):
    if numero == 12:
        break
    print(numero, end=" ")

for numero in range(20):
    if numero == 12:
        continue
    print(numero, end=" ")