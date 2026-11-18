from typing import Optional
from produto import Produto

class No:
    def __init__(self, produto: Produto):
        self.produto: Produto = produto
        self.esquerda: Optional['No'] = None
        self.direita: Optional['No'] = None

    def __repr__(self) -> str:
        return f"No(codigo={self.produto.codigo}, produto='{self.produto.nome}')"
