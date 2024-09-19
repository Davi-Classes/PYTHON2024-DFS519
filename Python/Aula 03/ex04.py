numeros = []

while True:
    numero = int(input('Digite um numero: '))

    if numero < 0:
        break

    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

# numeros_str = [str(numero) for numero in numeros]
# print(f'Numeros Digitados: {" - ".join(numeros_str)}')

print(f'Numeros Digitados: {numeros}')
print(f'Soma dos Numeros: {soma}')
print(f'Média dos numeros: {media}')