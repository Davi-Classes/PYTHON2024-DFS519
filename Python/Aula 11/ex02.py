class Carro:
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, velocidade_max: float):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def acelerar(self, velocidade: float):
        if self.velocidade_atual + velocidade >= self.velocidade_max:
            self.velocidade_atual = self.velocidade_max
        else:
            self.velocidade_atual += velocidade

        return self.velocidade_atual

    def frear(self, velocidade: float):
        if self.velocidade_atual - velocidade <= 0:
            self.velocidade_atual = 0
        else:
            self.velocidade_atual -= velocidade

        return self.velocidade_atual

    def __str__(self):
        return f'<Carro - {self.modelo} ({self.cor})>'


marca = input('Digite a Marca: ')
modelo = input('Digite a Modelo: ')
ano = int(input('Digite a Ano: '))
cor = input('Digite a Cor: ')
velocidade_max = float(input('Digite a Velocidade Máxima: '))

carro = Carro(marca, modelo, ano, cor, velocidade_max)

while True:
    print(f'Velocidade Atual: {carro.velocidade_atual}')
    opcao = input('Deseja Acelerar (1) ou Frear (2)? ')

    if opcao == '1':
        velocidade = float(input('Quanto deseja acelerar? '))
        carro.acelerar(velocidade)
    elif opcao == '2':
        velocidade = float(input('Quanto deseja frear? '))
        carro.frear(velocidade)
