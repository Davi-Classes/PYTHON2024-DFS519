# Try Except 2
# Você também pode especificar varios excepts para cada tipo de error

try:
    valor = float(input('Quanto deseja depositar? '))

# Especificando que se ocorrer um "ValueError", ele irá cair aqui.
except ValueError as err:
    print('Valor Inválido.')

# Especificando que se ocorrer um "Exception", ele irá cair aqui.
except Exception as err:
    print('Houve um error inesperado.')

# Sempre será executado.
finally:
    print('Sempre Serei Executado!')
