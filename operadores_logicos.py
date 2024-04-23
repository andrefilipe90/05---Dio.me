saldo = 1000
saque = 200
limite = 100
conta_especial = True
contatos_emergencia = []

exp_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp_1)

print(exp_2)

not 1000 > 1500

not contatos_emergencia

not "saque 1500"

not ""