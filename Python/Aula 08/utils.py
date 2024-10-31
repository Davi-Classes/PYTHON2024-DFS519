def menu(title: str, line_width: int, options: dict[str, str]) -> str:
    print('=' * line_width)
    print(title.center(line_width))
    print('=' * line_width)

    for key, option in options.items():
        print(f'[{key}] - {option}')

    print('=' * line_width)

    while True:
        opcao = input('-> Selecione uma opção: ')

        if options.get(opcao) is not None:
            break

        print('Opção inválida, insira novamente.')

    return opcao