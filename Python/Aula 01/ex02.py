nomes = []

for n in range(3):
    nome = input(f'Digite o {n + 1}º nome: ')
    nomes.append(nome)

print('----- Nomes Inseridos -----')
for nome in nomes:
    print(f'-> {nome}')

# for index in range(3):
#     print(f'-> {nomes[index]}')

