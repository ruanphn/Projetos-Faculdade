"""
Módulo de definição da entidade Produto.
Representa um item do catálogo da loja de informática.
"""

class Produto:
    """
    Representa um produto comercializado pela loja de informática.
    
    Atributos:
        codigo (int): Identificador único do produto (chave da ABB).
        nome (str): Descrição/nome do produto.
        preco (float): Preço unitário em Reais (R$).
    """
    def __init__(self, codigo: int, nome: str, preco: float):
        if not isinstance(codigo, int):
            raise TypeError("O código do produto deve ser um número inteiro.")
        if preco < 0:
            raise ValueError("O preço do produto não pode ser negativo.")
        self.codigo = int(codigo)
        self.nome = str(nome).strip()
        self.preco = float(preco)

    def __repr__(self) -> str:
        return f"Produto(codigo={self.codigo}, nome='{self.nome}', preco={self.preco:.2f})"

    def __str__(self) -> str:
        return f"[Cód: {self.codigo:03d}] {self.nome:<12} | Preço: R$ {self.preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
