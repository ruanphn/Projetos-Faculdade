class Produto:
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
