def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("valor sacado")
    print("obrigado por ser nosso cliente")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(100)

#def sacar(self, valor: float) None:
#    if self.saldo >= valor:
#        self.saldo -= valor
#