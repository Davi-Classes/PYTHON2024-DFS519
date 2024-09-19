pessoas = []

for _ in range(3):
    nome = input('Digite um nome: ')
    altura = float(input('Digite a altura: '))

    # Adicionando uma Tupla como Elemento
    pessoas.append((nome, altura))

# Desempacotando uma Tupla
for nome, altura in pessoas:
    print(f'{nome} - {altura}m')
