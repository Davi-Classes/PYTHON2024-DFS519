# Ex03. Faça uma função chamada "categorizar_imc" que receba o valor do imc e retorne uma string com a categoria de acordo com a tabela IMC.
# -> Abaixo do Peso até 18.5
# -> Peso Ideal até 25
# -> Sobrepeso até 30
# -> Obesidade I até 35
# -> Obesidade II até 40
# -> Obesidade III a partir de 40

# Defição.
def calcular_imc(peso, altura):
    return peso / altura ** 2

def categorizar_imc(imc):
    if imc <= 18.5:
        return 'Abaixo do Peso'
    elif imc <= 25:
        return 'Peso Ideal'
    elif imc <= 30:
        return 'Sobrepeso'
    elif imc <= 35:
        return 'Obesidade I'
    elif imc < 40:
        return 'Obesidade II'
    else:
        return 'Obesidade III'


# Codigo Principal
# Entrada
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite o sua altura: '))

# Processamento
imc = calcular_imc(peso, altura)
categoria = categorizar_imc(imc)

# Saída
print(f'Seu Imc é: {imc}')
print(f'Categoria: {categoria}')
