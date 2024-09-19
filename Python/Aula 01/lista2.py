pessoas = []
alturas = []

qtd_pessoas = 3
for _ in range(qtd_pessoas):
    nome = input('Digite um nome: ')
    pessoas.append(nome)

    altura = float(input('Digite a altura: '))
    alturas.append(altura)


for index in range(qtd_pessoas):
    print(f'{pessoas[index]} - {alturas[index]}m')  

