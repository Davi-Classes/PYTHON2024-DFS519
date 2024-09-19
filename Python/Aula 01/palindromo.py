palavra = input('Digite algo: ')

if palavra == palavra[::-1]:
    print('É palindromo')
else:
    print('Não é palimdromo')