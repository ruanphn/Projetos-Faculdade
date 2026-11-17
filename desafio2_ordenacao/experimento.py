"""
Módulo de instrumentação, execução dos experimentos comparativos e validações.
"""
import copy
import statistics
import time
from typing import Dict, List, Tuple, Any
from aluno import Aluno, gerar_alunos
from ordenacao import bubble_sort, merge_sort

TAMANHOS_TESTE = [100, 1000, 5000]
REPETICOES = 3

def validar_ordenacao(lista_ordenada: List[Aluno], lista_original: List[Aluno]) -> Tuple[bool, str]:
    """
    Valida a integridade do algoritmo de ordenação:
    1. Verifica se todas as notas estão em ordem não-decrescente.
    2. Garante que o total de elementos foi preservado.
    3. Confere se os registros de aluno (matrícula, nome e nota) foram preservados.
    """
    if len(lista_ordenada) != len(lista_original):
        return False, f"Falha de integridade: tamanho divergente ({len(lista_ordenada)} vs {len(lista_original)})."
        
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i].nota > lista_ordenada[i + 1].nota:
            return False, f"Falha de ordenação na posição {i}: {lista_ordenada[i].nota} > {lista_ordenada[i+1].nota}"
            
    # Conferência por amostragem/conjunto de tuplas (matrícula, nome, nota)
    originais_set = {(a.matricula, a.nome, a.nota) for a in lista_original}
    ordenados_set = {(a.matricula, a.nome, a.nota) for a in lista_ordenada}
    if originais_set != ordenados_set:
        return False, "Falha de consistência: dados de aluno corrompidos durante a ordenação."

    return True, "Ordenação e integridade validadas com sucesso."

def executar_experimento(seed: int = 42) -> List[Dict[str, Any]]:
    """
    Executa a bateria de testes comparativos para 100, 1.000 e 5.000 alunos.
    Repete cada algoritmo 3 vezes para cada tamanho e calcula a mediana do tempo (ms).
    """
    resultados: List[Dict[str, Any]] = []

    print("\n" + "="*75)
    print(" INICIANDO EXPERIMENTO COMPARATIVO (BUBBLE SORT vs MERGE SORT)")
    print(f" Semente aleatória: {seed} | Repetições por algoritmo: {REPETICOES}")
    print("="*75)

    for tamanho in TAMANHOS_TESTE:
        print(f"\n[+] Gerando conjunto com {tamanho:,} alunos...")
        dados_originais = gerar_alunos(tamanho, seed=seed)
        
        algoritmos = [
            ("Bubble Sort", bubble_sort),
            ("Merge Sort", merge_sort)
        ]

        for nome_alg, funcao_alg in algoritmos:
            tempos_ms: List[float] = []
            comparacoes_rodadas: List[int] = []
            ultima_lista_ordenada: List[Aluno] = []

            for rodada in range(1, REPETICOES + 1):
                # Criação de cópia isolada sem impactar a medição de tempo
                copia_dados = copy.deepcopy(dados_originais)
                
                inicio = time.perf_counter()
                lista_ord, comps = funcao_alg(copia_dados)
                fim = time.perf_counter()
                
                tempo_ms = (fim - inicio) * 1000.0
                tempos_ms.append(tempo_ms)
                comparacoes_rodadas.append(comps)
                ultima_lista_ordenada = lista_ord

            mediana_tempo = statistics.median(tempos_ms)
            comparacoes = comparacoes_rodadas[0] # Determinístico para a mesma entrada

            # Validação técnica
            valido, msg_val = validar_ordenacao(ultima_lista_ordenada, dados_originais)
            if not valido:
                raise RuntimeError(f"Erro no algoritmo {nome_alg} com {tamanho} itens: {msg_val}")

            registro = {
                "tamanho": tamanho,
                "algoritmo": nome_alg,
                "tempos_ms_brutos": tempos_ms,
                "tempo_mediano_ms": mediana_tempo,
                "comparacoes": comparacoes,
                "status_validacao": msg_val
            }
            resultados.append(registro)
            
            print(f"  -> {nome_alg:<12} | N = {tamanho:5d} | Tempo Mediano: {mediana_tempo:9.3f} ms | Comparações: {comparacoes:12,d}")

    print("\n" + "="*75)
    print(" EXPERIMENTO CONCLUÍDO COM SUCESSO E DADOS VALIDADOS!")
    print("="*75)
    return resultados
