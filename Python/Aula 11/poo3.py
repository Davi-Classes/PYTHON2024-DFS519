class Contador:
    def __init__(self):
        self.value = 0

    def add(self, value: int):
        self.value += value

    def sub(self, value: int):
        self.value -= value

    def __str__(self):
        return f'<Contador - {self.value}>'


contador = Contador()
opcao = input('Deseja adicionar (1) ou subtrair (2)?')

if opcao == '1':
    valor = int(input('Digite quanto deseja adicionar: '))
    contador.add(valor)
elif opcao == '2':
    valor = int(input('Digite quanto deseja adicionar: '))
    contador.sub(valor)

print(f'Valor Final: {contador.value}')
