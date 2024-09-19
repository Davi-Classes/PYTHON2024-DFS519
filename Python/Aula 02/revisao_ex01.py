import random as rd

numeros = []
positivos = []
negativos = []

# Entrada
# for n in range(1, 9):
#     numero = float(input(f'Digite o {n}º numero: '))
#     numeros.append(numero)

for _ in range(50):
    numero_aleatorio = rd.randint(-200, 200)
    numeros.append(numero_aleatorio)

# Processamento
for numero in numeros:
    if numero > 0:
        positivos.append(numero)
    elif numero < 0:
        negativos.append(numero)

# Saída
print(f'Numeros: {sorted(numeros)}')
print(f'Positivos: {sorted(positivos)}')
print(f'Negativos: {sorted(negativos)}')