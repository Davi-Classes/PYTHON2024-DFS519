class Animal:
    def __init__(self, nome: str, idade: int, cor: str, especie: str):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.especie = especie

    def __repr__(self):
        return f'<Animal - {self.especie} ({self.nome})>'

    def emitir_som(self):
        print(f'{self.nome} está fazendo som...')


if __name__ == '__main__':
    a1 = Animal('Margot', 1, 'Preto e Amarelo', 'Gato')
    a1.emitir_som()

    a2 = Animal('Torby', 4, 'Preto', 'Cachorro')
    a2.emitir_som()