
// crie uma função que retorna o maior número impar da sequencia (sem usar o max)
lista = [1,2,3,4,5,6,7,8,19,10,37,11,12,13,14,16,25]
impares = []
vet = 0
for l in lista:
    if (l%2 != 0):
        impares.append(l)  
vet = impares[0]
print(impares)
for i in impares:
    if (len(impares) - 1 != impares.index(i)):
        if (vet > impares[impares.index(i) + 1]) :
            vet = vet
        elif (vet < impares[impares.index(i) + 1]):
            vet = impares[impares.index(i) + 1]
print(vet)