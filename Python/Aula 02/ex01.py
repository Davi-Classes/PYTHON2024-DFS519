# Primeira Forma - Dicionario Vazio e Criando a Chave
livro = {}

livro['titulo'] = input('Digite o titulo do livro: ')
livro['autor'] = input('Digite o autor do livro: ')
livro['ano'] = int(input('Digite o ano do livro: '))

# Segunda Forma, pedindo os valores e depois criando o dicionário
# titulo = input('Digite o titulo do livro: ')
# autor = input('Digite o autor do livro: ')
# ano = int(input('Digite o ano do livro: '))

# livro = {
#     'titulo': titulo,
#     'autor': autor,
#     'ano': ano
# }

print('----- Livro -----')
print(f'Titulo: {livro["titulo"]}')
print(f'Autor: {livro["autor"]}')
print(f'Ano: {livro["ano"]}')