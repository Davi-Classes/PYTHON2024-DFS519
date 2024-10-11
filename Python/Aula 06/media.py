def media(valores: list[float]) -> float:
    return sum(valores) / len(valores)

# def media(valores: list[float]) -> float:
#     soma = 0
#     qtd_valores = 0

#     for valor in valores:
#         soma += valor
#         qtd_valores += 1

#     return soma / qtd_valores


numeros = []
qtd_valores = int(input('Digite quantos valores deseja inserir: '))

for i in range(qtd_valores):
    valor = float(input(f'Digite o {i+1}º valor: '))
    numeros.append(valor)

print(media(numeros))