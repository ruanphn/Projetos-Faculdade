"""
Módulo da entidade Aluno e rotina de geração de dados.
"""
import random
from typing import List

class Aluno:
    """
    Representa um estudante com matrícula, nome e nota acadêmica.
    
    Atributos:
        matricula (int): Identificador único sequencial (ex: 20260001).
        nome (str): Nome do aluno (ex: "Aluno 00001").
        nota (float): Nota acadêmica entre 0.00 e 10.00 com 2 casas decimais.
    """
    def __init__(self, matricula: int, nome: str, nota: float):
        self.matricula = int(matricula)
        self.nome = str(nome)
        self.nota = float(nota)

    def __repr__(self) -> str:
        return f"Aluno(mat={self.matricula}, nome='{self.nome}', nota={self.nota:.2f})"

    def __str__(self) -> str:
        return f"[Mat: {self.matricula}] {self.nome} - Nota: {self.nota:5.2f}"

def gerar_alunos(quantidade: int, seed: int = 42) -> List[Aluno]:
    """
    Gera uma lista com a quantidade solicitada de objetos Aluno.
    
    Regras da especificação:
    - Semente fixa para reprodutibilidade.
    - Matrículas únicas a partir de 20260001 (matricula = 20260000 + i).
    - Nomes no padrão "Aluno 00001", "Aluno 00002" etc.
    - Notas aleatórias entre 0 e 10 com 2 casas decimais.
    """
    if seed is not None:
        random.seed(seed)
    
    alunos: List[Aluno] = []
    for i in range(1, quantidade + 1):
        matricula = 20260000 + i
        nome = f"Aluno {i:05d}"
        nota = round(random.uniform(0, 10), 2)
        alunos.append(Aluno(matricula, nome, nota))
    
    return alunos
