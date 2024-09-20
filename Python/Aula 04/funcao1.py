# Funções I

# Para declarar uma função no python, precisamos utilizar a seguinte sintaxe:
# def nome_da_funcao(parametros...):
#   "corpo da função aqui..."

# Definição
def saudacao(nome): # Os parametros são recebidos na chamada 
    return f'Olá {nome}, Seja bem vindo!' # O retorno da função volta para onde ela foi chamada.


# Codigo Principal
nome_input = input('Digite seu nome: ')
mensagem = saudacao(nome_input)
print(mensagem)
print(saudacao(nome_input))