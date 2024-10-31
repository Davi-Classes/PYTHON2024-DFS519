import cliente as c
from utils import menu

def main():
    options = {
        # Key : Value
        '1': 'Listar Clientes.', # Items
        '2': 'Cadastrar clientes.',
        '3': 'Atualizar um cliente.',
        '4': 'Excluir cliente.',
        '5': 'Sair',
    }

    while True:
        opcao = menu('Gerenciamento de Clientes', 30, options)

        if opcao == '1':
            c.listar_clientes()
        elif opcao == '2':
            c.cadasdrar_cliente()
        elif opcao == '3':
            c.atualizar_cliente()
        elif opcao == '4':
            c.excluir_cliente()
        elif opcao == '5':
            print('Fim do Programa. Volte sempre!')
            break

        print()
        input('Aperte <ENTER> para continuar')


if __name__ == '__main__':
    main()
