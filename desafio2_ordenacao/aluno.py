import random
from typing import List

class Aluno:
    def __init__(self, matricula: int, nome: str, nota: float):
        self.matricula = int(matricula)
        self.nome = str(nome)
        self.nota = float(nota)

    def __repr__(self) -> str:
        return f"Aluno(mat={self.matricula}, nome='{self.nome}', nota={self.nota:.2f})"

    def __str__(self) -> str:
        return f"[Mat: {self.matricula}] {self.nome} - Nota: {self.nota:5.2f}"

def gerar_alunos(quantidade: int, seed: int = 42) -> List[Aluno]:
    if seed is not None:
        random.seed(seed)
    
    alunos: List[Aluno] = []
    for i in range(1, quantidade + 1):
        matricula = 20260000 + i
        nome = f"Aluno {i:05d}"
        nota = round(random.uniform(0, 10), 2)
        alunos.append(Aluno(matricula, nome, nota))
    
    return alunos
