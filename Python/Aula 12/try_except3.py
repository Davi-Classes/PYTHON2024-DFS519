# Try Except 3
# Também podemos lançar erros propositalmente com o "raise"

while True:
    try:
        valor = float(input('Digite um valor: '))

        if valor < 1: # Lançando Exception
            raise Exception('Valor não pode ser negativo.')
        
        if valor > 10: # Lançando Exception
            raise Exception('O valor não pode ser maior que 10.')

        break
    except Exception as err:
        # Buscando Mensagem da Exception que Estamos Lançando
        print(err.args[0]) 
    except ValueError as err: 
        # Tratamento da conversão de Str -> Float
        print('Você deve digitar somente numeros.')

# Aqui garanto que o valor está válido.
print(valor)