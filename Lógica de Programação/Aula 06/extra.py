# 'arara' = 'arara' -> Palindromo
# 'ana' = 'ana'
# 'Socorram-me, subi no ônibus em Marrocos'
# 'Amor a Roma.'

print('Verificador de Palindromo')
texto = input('Digite uma frase: ')
texto_sem_espacos = texto.replace(' ', '')


# texto_invertido = ''
# contador = len(texto_sem_espacos) - 1 

# while contador >= 0:
#     texto_invertido += texto_sem_espacos[contador]
#     contador -= 1

if texto_sem_espacos[::-1] == texto_sem_espacos:
    print('É um palindromo.')
else:
    print('Não é um palindromo.')