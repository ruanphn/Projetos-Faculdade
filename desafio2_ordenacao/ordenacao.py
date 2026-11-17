"""
Módulo de implementação manual dos algoritmos de ordenação.
Restrição: PROIBIDO o uso de sort() ou sorted() nativos do Python.
"""
from typing import List, Tuple
from aluno import Aluno

def bubble_sort(lista_original: List[Aluno]) -> Tuple[List[Aluno], int]:
    """
    Ordena uma lista de objetos Aluno pela nota em ordem crescente utilizando Bubble Sort.
    
    Instrumentação:
    - Contabiliza estritamente as comparações realizadas entre as notas dos alunos.
    - Não contabiliza testes de controle de laços ou índices.
    
    Retorna:
        Tuple[List[Aluno], int]: (Lista ordenada, total de comparações de notas)
    """
    lista = list(lista_original)
    n = len(lista)
    comparacoes = 0
    
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            comparacoes += 1
            if lista[j].nota > lista[j + 1].nota:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
            
    return lista, comparacoes

def merge_sort(lista_original: List[Aluno]) -> Tuple[List[Aluno], int]:
    """
    Ordena uma lista de objetos Aluno pela nota em ordem crescente utilizando Merge Sort.
    
    Instrumentação:
    - Contabiliza estritamente as comparações entre notas durante a etapa de intercalação (merge).
    - Não contabiliza verificações de limites de lista ou testes de laço.
    
    Retorna:
        Tuple[List[Aluno], int]: (Lista ordenada, total de comparações de notas)
    """
    lista = list(lista_original)
    total_comparacoes = [0]  # Usado como referência mutável para acumular nas chamadas recursivas
    
    def _merge_sort_rec(sublista: List[Aluno]) -> List[Aluno]:
        if len(sublista) <= 1:
            return sublista
            
        meio = len(sublista) // 2
        esquerda = _merge_sort_rec(sublista[:meio])
        direita = _merge_sort_rec(sublista[meio:])
        
        return _merge(esquerda, direita)
        
    def _merge(esquerda: List[Aluno], direita: List[Aluno]) -> List[Aluno]:
        resultado: List[Aluno] = []
        i = 0
        j = 0
        len_esq = len(esquerda)
        len_dir = len(direita)
        
        while i < len_esq and j < len_dir:
            total_comparacoes[0] += 1
            # Comparação estrita entre as notas (usa <= para garantir algoritmo estável)
            if esquerda[i].nota <= direita[j].nota:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
                
        # Elementos restantes não exigem novas comparações de notas
        if i < len_esq:
            resultado.extend(esquerda[i:])
        if j < len_dir:
            resultado.extend(direita[j:])
            
        return resultado

    lista_ordenada = _merge_sort_rec(lista)
    return lista_ordenada, total_comparacoes[0]
