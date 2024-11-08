# POO 1
# Classes
class Celular:
    # Metódo Construtor
    def __init__(self, modelo: str, marca: str, cor: str):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ligado = False

    def info(self) -> str:
        infos = f'{self.marca}: {self.modelo} ({self.cor})'
        return infos

# Objeto 1
celular1 = Celular('Samsung A31', 'Samsung', 'Preto')

print(celular1.info())
print(celular1.ligado)

celular1.ligar()

print(celular1.ligado)

print('-'*20)

# Objeto 2
celular2 = Celular('Iphone XR', 'Apple', 'Branco')

print(celular2.info())