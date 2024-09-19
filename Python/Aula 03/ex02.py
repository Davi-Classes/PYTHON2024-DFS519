idade = int(input('Digite a sua idade: '))

if idade <= 12:
    faixa_hetaria = 'Criança'
elif idade <= 17:
    faixa_hetaria = 'Adolescente'
elif idade <= 64:
    faixa_hetaria = 'Adulto'
else:
    faixa_hetaria = 'Idoso'

print(f'A sua faixa hetária é: {faixa_hetaria}')