class Conta:
    def __init__(self, titular: str, numero: str, saldo: float = 0):
        self.titular = titular
        self.numero = numero

        if saldo < 0:
            raise ValueError('Não é possivel criar uma conta com saldo negativo.')

        self.saldo = saldo
    
    def depositar(self, valor: float) -> float:
        if valor < 0:
            raise ValueError('Não é possivel depositar valores negativos.')

        self.saldo += valor
        return self.saldo

    def sacar(self, valor: float) -> float:
        if valor < 0:
            raise ValueError('Não é possivel sacar valores negativos.')

        if self.saldo < valor:
            raise ValueError('Não é possivel sacar mais do que há na conta.')

        self.saldo -= valor
        return self.saldo

    def transferir(self, valor: float, conta_destino: 'Conta') -> float:
        self.sacar(valor)
        conta_destino.depositar(valor)

    def get_saldo(self):
        return f'R$ {self.saldo:.2f}'
    
    def __repr__(self):
        return f'<Conta - {self.titular} ({self.numero})>'


# nome = input('Digite o titular da conta: ')
# codigo = input('Digite o numero da conta: ')
# montante = float(input('Digite o valor que deseja inserir na abertura: '))

try:
    c2 = Conta('Julia', '65356', -23)
    print(c2.titular, c2.get_saldo(), sep=': ')

    c2.depositar(-1)

    print(c2.titular, c2.get_saldo(), sep=': ')

    c2.sacar(50)

    print(c2.titular, c2.get_saldo(), sep=': ')

    c1 = Conta('Mateo', '1234')
    print(c1.titular, c1.get_saldo(), sep=': ')

    c2.transferir(20, c1)
    print(c2.titular, c2.get_saldo(), sep=': ')
    print(c1.titular, c1.get_saldo(), sep=': ')
except ValueError as err:
    # Capturando Error que está sendo estourado.
    print(err.args[0])