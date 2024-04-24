conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 20000
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado usando Cheque Especial.")
    else:
        print("Saldo Insuficiente.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo Insuficiente.")
elif conta_especial:
    if saldo >= saque:
        print("saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado usando Cheque Especial.")
    else:
        print("Saque realizado, com linha de credito especial.")
else:
    print("Conta não identificada.")