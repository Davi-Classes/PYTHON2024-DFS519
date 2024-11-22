class Conta:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor: float):
        if valor > self.saldo:
            raise Exception('Não é possivel sacar mais do que há na conta.')
        
        self.saldo -= valor

    def render(self) -> float:
        return 0
    

class ContaCorrente(Conta):
    def __init__(self, titular: str, saldo: float = 0, cheque_especial: float = 0):
        super().__init__(titular, saldo)
        self.cheque_especial = cheque_especial

    def sacar(self, valor):
        if valor > (self.saldo + self.cheque_especial):
            raise Exception('Não é possivel sacar mais do que há na conta.')
        
        self.saldo -= valor

    def render(self):
        total = self.saldo * 0.01
        self.saldo += total
        return total


c1 = ContaCorrente('Davi', 5000, cheque_especial=100)
print(c1.saldo)
c1.sacar(5101)
print(c1.saldo)
