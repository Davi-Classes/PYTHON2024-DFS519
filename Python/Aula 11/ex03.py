class Conta:
    def __init__(self, titular: str, numero: str, saldo: float = 0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
    
    def depositar(self, valor: float) -> float:
        self.saldo += valor
        return self.saldo

    def sacar(self, valor: float) -> float:
        self.saldo -= valor
        return self.saldo

    def transferir(self, valor: float, conta_destino: 'Conta') -> float:
        self.sacar(valor)
        conta_destino.depositar(valor)

    def get_saldo(self):
        return f'R$ {self.saldo:.2f}'
    
    def __repr__(self):
        return f'<Conta - {self.titular} ({self.numero})>'


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
