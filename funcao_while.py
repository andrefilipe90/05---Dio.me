opcao = -1

print("Escolha o que deseja fazer:\n")
while opcao != 0:
    opcao = int(input("[1]sacar\n[2]Extrato\n[0]Sair\n"))
    
    if opcao == 1:
        print("sacando")
    elif opcao == 2:
        print("Extrato:")