numeros = [6, 8, 2, 8, 23, 76, 12, 0]
nomes = ['Davi', 'ana', 'Caio', 'mateo']
pessoas = [
    {
        'id': 1,
        'nome': 'Caio'
    },
    {
        'id': 2,
        'nome': 'Ana'
    },
    {
        'id': 3,
        'nome': 'Pedro'
    }
]

# Ordenando Numeros
numeros.sort()

# Ordenando Nomes com Key
nomes.sort(key=lambda nome: nome.lower())

# Ordenando Lista de Dicionários
pessoas.sort(key= lambda pessoa: pessoa.get('nome'))

# print(numeros)
# print(nomes)
print(pessoas)