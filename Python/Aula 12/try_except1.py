# Try Except 1
# Essa estrutura é utilizada para capturar erros em tempo de execução

# Ele irá tentar executar o "try"
try:
    valor = float(input('Quanto deseja depositar? '))

# Caso algum error aconteça, ele irá cair no except
except:
    print('Valor Inválido')

# Sempre será executado.
finally:
    print('Sempre Serei Executado!')
