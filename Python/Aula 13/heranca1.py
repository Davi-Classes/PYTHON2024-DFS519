# Herança
# A herança é a capacidade que uma classe tem de
# herdar os atributos e metódos de outra classe, 
# sem precisar implementar

# Polimorfismo
# O polimorfismo é a capacidade que uma classe filha
# sobreescreva um metódo herdado de uma classe pai, 
# definindo suas proprias especificidades.
from revisao import Animal


class Gato(Animal):
    # Aqui a classe "Gato" está definindo o proprio construtor
    # Sobreescrevendo o construtor do pai com o polimorfismo
    def __init__(self, nome: str, idade: int, cor: str, cor_olhos: str):
        # Ao chamar o "super()" a classe filha está chamando um metódo da classe pai para reaproveitar as propriedades em comum
        super().__init__(nome, idade, cor, 'Gato')
        self.cor_olhos = cor_olhos

    def emitir_som(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):
    # Aqui a classe "Cachorro" está utilizando o construtor de Animal.
    # Mas está sobreescrevendo o metódo "emitir_som" com o polimorfismo
    def emitir_som(self):
        print(f'{self.nome} está latindo...')


gato1 = Gato('Floki', 0, 'Preto', 'Amarelo')
print(gato1)
gato1.emitir_som()

cachorro1 = Cachorro('Torby', 4, 'Preto', 'Cachorro')
print(cachorro1)
cachorro1.emitir_som()