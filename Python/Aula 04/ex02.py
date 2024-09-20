# Ex02. Faça uma função chamada "imc" que receba peso e altura e retorne o valor do imc
# Formula: peso / altura ** 2

# Defição.
def calcular_imc(peso, altura):
    return peso / altura ** 2

# Codigo Principal
# Entrada
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite o sua altura: '))

# Processamento
imc = calcular_imc(peso, altura)

# Saída
print(f'Seu Imc é: {imc}')