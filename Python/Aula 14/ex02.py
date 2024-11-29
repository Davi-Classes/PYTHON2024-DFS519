from dataclasses import dataclass

@dataclass
class Item:
    nome: str
    categoria: str
    preco_unitario: float
    quantidade: int = 1