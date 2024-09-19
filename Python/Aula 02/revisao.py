# Ex04. Faça um programa que peça 3 notas, e armazene-as em uma lista. Ao final, calcule a média das notas utilizando as funções "sum()" e "len()"

# Declarando nossa lista de notas
# Indexada - Posicional
#         0    1
# notas = [1.3, 5.4]
notas = []

for n in range(3):
    # Pedindo a nota
    nota = float(input(f'Digite a {n + 1}º nota: '))
    
    # Adicionando nota ao final da lista
    notas.append(nota)

    # Adicionando nota ao começo da lista
    # notas.insert(0, nota)
    
media = sum(notas) / len(notas)

print(f'A média do aluno foi: {media:.2f}')