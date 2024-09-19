# Conjuntos
# O Conjunto é uma estrutura não ordenada e sem valores duplicados
meu_conjunto = {1, 6, 7, 3}
print(meu_conjunto)

# Lista com Repetições
nomes = ["Davi", "Vitor", "Julia", "Mateo", "Julia", "Davi", "Mateo"]

# Criador do Conjunto a partir de um iteravel
nomes = list(set(nomes)) # Remover Duplicados
nomes.sort()

for nome in nomes:
    print(nome)

# Conjuntos também é interessante para valores estáticos
vogais = {'a', 'e', 'i', 'o', 'u'}
if 'a' in vogais:
    print('É uma vogal.')