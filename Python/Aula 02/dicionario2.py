# Ex03. Faça um programa que cadastre o nome, peso e altura de 5 pessoas. Ao final, mostre todas as pessoas cadastradas e o seu IMC
pessoas = []

for _ in range(3):
    pessoa = {}

    pessoa['nome'] = input('Digite o nome da pessoa: ')
    pessoa['altura'] = float(input('Digite a altura da pessoa: '))
    pessoa['peso'] = float(input('Digite o peso da pessoa: '))
    pessoa['imc'] = pessoa['peso'] / pessoa['altura'] ** 2

    pessoas.append(pessoa)

for pessoa in pessoas:
    print('-' * 20)
    print('Nome:', pessoa['nome'])
    print('Altura:', pessoa['altura'])
    print('Peso:', pessoa['peso'])
    print('IMC:', pessoa['imc'])

print('-' * 20)
