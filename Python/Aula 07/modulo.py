# Um arquivo python é um modulo que pode ser importado, existem 2 tipos de importação:
# 1. Importando o modulo Todo
import random as rd

nomes = ['Caio', 'Mateo', 'Rafael', 'Junior']
sorteado = rd.choice(nomes)

numero_aleatorio = rd.randint(1, 10)

print(sorteado)

# 2. Importando funções especificas
# from datetime import * # Importa TUDO.
from datetime import datetime, date

hoje = datetime.now()
data_nascimento = input('Digite sua data de nascimento [dd/mm/yyyy]: ')
data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

diferenca = hoje - data_nascimento
idade = diferenca.days // 365
print(idade)
