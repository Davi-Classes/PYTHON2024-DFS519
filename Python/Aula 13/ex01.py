class Funcionario:
    def __init__(self, nome: str, salario: float, habilidades: list[str] = []):
        self.nome = nome
        self.salario = salario
        self.habilidades = habilidades
    
    def salario_liquido(self) -> float:
        ir = 0.08
        inss = 0.03
        return self.salario - (self.salario * (ir + inss))


class Gerente(Funcionario):
    def salario_liquido(self) -> float:
        ir = 0.15
        inss = 0.08
        return self.salario - (self.salario * (ir + inss))


class Atendente(Funcionario):
    def salario_liquido(self) -> float:
        ir = 0.08
        inss = 0.05
        sindicato = 0.03
        return self.salario - (self.salario * (ir + inss + sindicato))
    

gerente = Gerente('Mauricio Macias', 10000)
atendente = Atendente('Leandro', 4000)

print(f'Salário Gerente: {gerente.salario_liquido()}')
print(f'Salário Atendente: {atendente.salario_liquido()}')