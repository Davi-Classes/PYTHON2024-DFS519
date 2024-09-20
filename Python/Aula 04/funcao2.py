# Funções II

# Quando definimos a função ela fica em memória 
def saudacao(nome, idade):
    print(f'Olá {nome}, Seja bem vindo!')
    print(f'Você está bem com {idade} anos')

# A passaagem de parametros ela é posicional
saudacao('Bruno', 39)

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

saudacao(nome)