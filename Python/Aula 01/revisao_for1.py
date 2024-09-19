# 6. Sistema de Login com Tentativas Limitadas:
# Desenvolva um programa que simule um sistema de login.
# O programa deve solicitar o nome de usuário e senha até que o usuário insira as credenciais corretas ou até que o número máximo de tentativas seja atingido. 

usuario_db = 'davi.lucciola'
senha_db = '123'
logado = False

print('---- SISTEMA DE LOGIN ----')

qtd_tentativas = 3
# 1, 2, 3
for tentativa in range(1, qtd_tentativas + 1):
    usuario = input('Digite o usuário: ')
    senha = input('Digite sua senha: ')
    
    if usuario == usuario_db and senha == senha_db:
        logado = True
        break

    print(f'Usuário ou senha inválidos, você tem {qtd_tentativas - tentativa} tentativas')

if logado:
    print(f'Seja bem vindo {usuario}')
else:
    print('Não autorizado, crendenciais inválidas')