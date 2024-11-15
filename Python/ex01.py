class Animal:
    def __init__(self, nome: str, idade: int, peso: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def aniversario(self):
        self.idade += 1

    def alterar_peso(self, peso: float):
        if peso < 0:
            raise ValueError('O peso do animal não pode ser negativo.')
        
        self.peso = peso

    def som(self, onomatopeia: str):
        if onomatopeia is None or onomatopeia == '':
            raise ValueError('A onomatopeia não pode ser vazia.')

        return f'O {self.nome} está fazendo {onomatopeia}'


animal1 = Animal('Café', 1, 6)
print(animal1.nome, animal1.idade, animal1.peso)

som = input('Qual é o som que o animal 1 faz? ')
print(animal1.som(som))

animal2 = Animal('Xena', 6, 10)
print(animal2.som('AU AU'))