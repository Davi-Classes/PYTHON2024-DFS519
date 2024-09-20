# Ex04. Faça uma função chamada "metros_para_cm" que receba um valor em metros e retorne o valor em centimetros.
def metros_para_cm(metros):
    conversao = metros * 100
    return conversao

metros = float(input('Digite um tamanho em metros: '))

centimetros = metros_para_cm(metros)

print(f'{metros}m equivalem a {centimetros}cm')