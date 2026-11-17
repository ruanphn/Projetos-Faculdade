"""
Módulo de definição da estrutura do Nó para Árvore Binária de Busca.
"""
from typing import Optional
from produto import Produto

class No:
    """
    Representa um nó individual em uma Árvore Binária de Busca (ABB).
    
    Atributos:
        produto (Produto): Objeto contendo os dados do produto (chave = produto.codigo).
        esquerda (Optional[No]): Referência para o filho à esquerda (códigos menores).
        direita (Optional[No]): Referência para o filho à direita (códigos maiores).
    """
    def __init__(self, produto: Produto):
        self.produto: Produto = produto
        self.esquerda: Optional['No'] = None
        self.direita: Optional['No'] = None

    def __repr__(self) -> str:
        return f"No(codigo={self.produto.codigo}, produto='{self.produto.nome}')"
