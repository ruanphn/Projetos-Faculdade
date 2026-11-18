import copy
import statistics
import time
from typing import Dict, List, Tuple, Any
from aluno import Aluno, gerar_alunos
from ordenacao import bubble_sort, merge_sort

TAMANHOS_TESTE = [100, 1000, 5000]
REPETICOES = 3

def validar_ordenacao(lista_ordenada: List[Aluno], lista_original: List[Aluno]) -> Tuple[bool, str]:
    if len(lista_ordenada) != len(lista_original):
        return False, f"Tamanho divergente: {len(lista_ordenada)} vs {len(lista_original)}"
        
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i].nota > lista_ordenada[i + 1].nota:
            return False, f"Ordenação incorreta no índice {i}"
            
    originais_set = {(a.matricula, a.nome, a.nota) for a in lista_original}
    ordenados_set = {(a.matricula, a.nome, a.nota) for a in lista_ordenada}
    if originais_set != ordenados_set:
        return False, "Registros corrompidos durante ordenação"

    return True, "Validação aprovada"

def executar_experimento(seed: int = 42) -> List[Dict[str, Any]]:
    resultados: List[Dict[str, Any]] = []

    for tamanho in TAMANHOS_TESTE:
        dados_originais = gerar_alunos(tamanho, seed=seed)
        
        algoritmos = [
            ("Bubble Sort", bubble_sort),
            ("Merge Sort", merge_sort)
        ]

        for nome_alg, funcao_alg in algoritmos:
            tempos_ms: List[float] = []
            comparacoes_rodadas: List[int] = []
            ultima_lista: List[Aluno] = []

            for _ in range(REPETICOES):
                copia = copy.deepcopy(dados_originais)
                
                inicio = time.perf_counter()
                lista_ord, comps = funcao_alg(copia)
                fim = time.perf_counter()
                
                tempos_ms.append((fim - inicio) * 1000.0)
                comparacoes_rodadas.append(comps)
                ultima_lista = lista_ord

            mediana_tempo = statistics.median(tempos_ms)
            comparacoes = comparacoes_rodadas[0]

            valido, msg_val = validar_ordenacao(ultima_lista, dados_originais)
            if not valido:
                raise RuntimeError(f"Erro em {nome_alg} ({tamanho}): {msg_val}")

            resultados.append({
                "tamanho": tamanho,
                "algoritmo": nome_alg,
                "tempo_mediano_ms": mediana_tempo,
                "comparacoes": comparacoes
            })
            
    return resultados
