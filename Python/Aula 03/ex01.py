produto = {}

produto['nome'] = input('Digite o nome do produto: ')
produto['preco_bruto'] = float(input('Digite o preço do produto: ').replace(',', '.'))
produto['desconto'] = float(input('Digite o valor do desconto: ').replace(',', '.'))

valor_desconto = produto['preco_bruto'] * produto['desconto']
produto['preco_liquido'] = produto['preco_bruto'] - valor_desconto

print(f'Produto: {produto["nome"]}')
print(f'Preço: {produto["preco_bruto"]:.2f}')
print(f'Valor Desconto: - R${valor_desconto:.2f}')
print(f'Valor Total: R${produto["preco_liquido"]:.2f}')
