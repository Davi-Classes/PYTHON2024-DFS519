# Banco de Dados
usuarios = [
    {
        'usuario': 'caio.delas',
        'senha': '123'
    },
    {
        'usuario': 'julio.cria',
        'senha': '745'
    }
]

def login(user, senha):
    for usuario in usuarios:
        if usuario['usuario'] == user and usuario['senha'] == senha:
            return True
    
    return False


usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

if login(usuario, senha):
    print('Seja Bem Vindo!')
else:
    print('Não Autorizado.')