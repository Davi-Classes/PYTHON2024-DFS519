# Lista para armazenar os dados.
numeros = []

# For para preencher os dados.
for _ in range(5):
    numero = float(input('Digite um numero: '))
    numeros.append(numero)

# For para mostrar os dados armazenados.
print('---- Numeros Inseridos ----')
for numero in numeros:
    print(f'- {numero:.2f}')