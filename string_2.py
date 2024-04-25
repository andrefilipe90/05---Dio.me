nome = "Guilherme"
idade = 28
profissao = "programador"
linguagem = "Python"
saldo = 45.435

print ("nome: %s idade: %d" % (nome,idade))
print ("nome: {} idade: {}".format(nome,idade))
print ("nome: {name} idade: {age}".format(name=nome,age=idade))
print (f"nome: {nome} idade: {idade}")

dados = {"nome": "Guilherme", "idade": 29}

print ("Nome: {nome} Idade: {idade}".format(**dados))

print (f"Nome: {nome} idade: {idade} Saldo: {saldo:.2f}")