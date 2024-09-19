# Adicionando Items
numeros = []

# Repete 3 vezes = Adiciona 3 items na lista
for _ in range(3):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)

# Percorrendo a lista de numeros 
for numero in numeros:
    print(numero)
