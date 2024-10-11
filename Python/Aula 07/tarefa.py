tarefas = [
    {
        'id': 1,
        'nome': 'Aprofundar SP Security',
        'descricao': 'Estudar ...',
        'concluido': False
    },
    {
        'id': 2,
        'nome': 'Implementar Serviço ISP',
        'descricao': 'Implementar conexão ...',
        'concluido': False
    }
]

def gerar_id():
    maior = 1

    for tarefa in tarefas:
        if tarefa.get('id') > maior:
            maior = tarefa.get('id')

    return maior + 1


def listar_tarefas():
    print('=' * 40)
    print('Tarefas Cadastradas:\n')
    for tarefa in tarefas:
        concluido = 'x' if tarefa.get('concluido') == True else ' '
        print(f'{tarefa.get("id")}. {tarefa.get("nome")} - [{concluido}]')
        print(f'-> {tarefa.get("descricao")}')
        print()


def listar_tarefas_nao_concluidas():
    for tarefa in tarefas:
        if tarefa.get('concluido') == False:
            print(f'{tarefa.get("id")}. {tarefa.get("nome")}')


def cadastrar_tarefa():
    print('=' * 40)
    print('Insira os dados:\n')

    while True:
        nome = input('Digite o nome da tarefa: ')
        
        if nome.strip() != '':
            break
            
        print('O nome da tarefa é obrigatório.')

    descricao = input('Digite a descrição da tarefa (opcional): ')

    tarefa = {
        'id': gerar_id(),
        'nome': nome,
        'descricao': descricao,
        'concluido': False
    }

    tarefas.append(tarefa)

def concluir_tarefa():
    print('=' * 40)
    print('Selecione o ID da tarefa que deseja concluir: \n')

    listar_tarefas_nao_concluidas()
    
    print()
    identificador = int(input('-> '))

    for tarefa in tarefas:
        if tarefa.get('id') == identificador:
            tarefa['concluido'] = True
            print('Tarefa concluida com sucesso!\n')
    

def excluir_tarefa():
    print('=' * 40)
    print('Selecione o ID da tarefa que deseja excluir: \n')

    listar_tarefas()

    identificador = int(input('-> '))

    for index, tarefa in enumerate(tarefas):
        if tarefa.get('id') == identificador:
            tarefas.pop(index)
            print('Tarefa excluida com sucesso!\n')
