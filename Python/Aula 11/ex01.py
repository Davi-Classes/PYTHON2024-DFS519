class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float, peso: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def info(self):
        infos = f'{self.nome} - {self.idade} - {self.altura}m - {self.peso}Kg'
        return infos
    
    def __str__(self):
        return f'<Pessoa - {self.nome}>'

pessoa1 = Pessoa('Victor', 24, 1.72, 60)
print(pessoa1)

pessoa2 = Pessoa('André', 34, 1.75, 82)
print(pessoa2)