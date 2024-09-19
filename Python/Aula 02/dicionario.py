import random

aluno = {
    # Chave: Valor
    'nome': 'Mateo', # Items
}

notas = []

for n in range(3):
    nota = random.randint(0, 100) / 10
    notas.append(nota)

# Criar ou Alterar Chaves Existentes
aluno['notas'] = notas  
aluno['media'] = sum(notas) / len(notas)
aluno['situacao'] = 'APROVADO' if aluno['media'] >= 6 else 'REPROVADO'

# Acessar Valores através das chaves
print('Dicionario:', aluno)
print(aluno['nome'])
print(aluno.get('notas'))

# Caso a Chave não exista, ele quebra o codigo.
print(aluno.get('fasfasfas'))
# print(aluno['fhajisfhjias'])