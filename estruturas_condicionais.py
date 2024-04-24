saldo = 2000.0
saque = float(input("informe o valor do saque: "))

if saldo >= saque:
    print("realizando o saque.")
    saldo -= saque
else:
    print("Saldo Insuficiente.")

#if saldo < saque:
#    print("Saldo Insuficiente.")

opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato:"))

if opcao == 1:
    valor = float(input("informe a quantia para o saque:"))

elif opcao == 2:
    print("o saldo atual é ",saldo)

else:
    print("opção não reconhecida.")