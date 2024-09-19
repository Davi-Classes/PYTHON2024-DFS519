# 8. Faça um programa que peça uma frase para o usuário, depois mostre na tela quantas vogais existem naquela frase.
qtd_vogais = 0
frase = input('Digite uma frase: ')

for letra in frase:
   if letra.upper() in 'AEIOU':
      qtd_vogais += 1

print(f'A frase tem {qtd_vogais} vogais')