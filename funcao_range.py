#range(stop) -> range object
#range(start,stop[,step]) -> range object
#range(numero inicial, numero da soma final, taxa de iteração)
#ex range (0, 11, 5)
#0 5 10
#list (range(4))
#x = range(0,11)
#print(x)

for numero in range(0,11):
    print(numero, end=" ")

print("\n")
for numero in range(0,11,5):
    print(numero, end=" ")