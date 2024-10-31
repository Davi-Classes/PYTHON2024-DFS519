from tabulate import tabulate

# Modelando a Estrutura de Dados do Cliente
# Quais são os campos que eu preciso armazenar no sistema?
# - id
# - nome
# - cpf_cnpj
# - endereco
clientes = [
    {
        'id': 1,
        'nome': 'Mateo',
        'cpf_cnpj': '12354365666',
        'endereco': 'Savassi, Belo Horizonte - MG'
    },
    {
        'id': 2,
        'nome': 'Davi',
        'cpf_cnpj': '53465665677',
        'endereco': 'Boca do Rio, Salvador - BA'
    }
]


def listar_clientes():
    # Pega as Colunas
    fields = list(clientes[0].keys()) if len(clientes) > 0 else []

    # Pega os Valores
    # data = [tuple(cliente.values()) for cliente in clientes]
    data = []

    for cliente in clientes:
        data.append(tuple(cliente.values()))

    # Recebe os dados e as Colunas, e retorna a STRING da TABELA
    table = tabulate(data, headers=fields) 

    line_width = len(table.split('\n')[1])
    print('=' * line_width)
    print(table)
    print('=' * line_width)
    
    # Poderia ter opções abaixo...

def cadasdrar_cliente():
    pass

def atualizar_cliente():
    pass

def excluir_cliente():
    pass

