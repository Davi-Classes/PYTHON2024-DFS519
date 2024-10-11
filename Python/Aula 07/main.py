import os
from tarefa import (
    listar_tarefas, cadastrar_tarefa, 
    concluir_tarefa, excluir_tarefa
)

# Create Read Update Delete
def menu():
    os.system('cls')
    
    print(' Gerenciador de Tarefas '.center(40, '='))
    print('[1] - Listar Tarefas')
    print('[2] - Cadastrar Nova Tarefa')
    print('[3] - Concluir uma tarefa')
    print('[4] - Excluir Tarefa')
    print('[5] - Sair')
    print('=' * 40)

    opcao = input('Selecione uma opção -> ')
    return opcao

def main():
    while True:
        opcao = menu()

        match opcao:
            case '1':
                listar_tarefas()

            case '2':
                cadastrar_tarefa()

            case '3':
                concluir_tarefa()

            case '4':
                excluir_tarefa()

            case '5':
                break

            case _:
                print('Opção Inválida! Digite Novamente!')

        input('Aperte <ENTER> para continuar...')

    print('Obrigado por utilizar nossos serviços!')

# Dunder Objects
if __name__ == '__main__':
    main()
