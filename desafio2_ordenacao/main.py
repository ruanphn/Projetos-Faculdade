"""
Programa Principal - Desafio 2: Comparação de Algoritmos de Ordenação
Executa a geração de alunos, medições com 3 rodadas, mediana de tempo e exibição da tabela comparativa.
"""
import json
import os
import sys
from experimento import executar_experimento

def formatar_tabela_markdown(resultados) -> str:
    linhas = []
    linhas.append("| Registros | Algoritmo | Tempo mediano (ms) | Comparações |")
    linhas.append("|---|---|---|---|")
    for r in resultados:
        linhas.append(f"| {r['tamanho']:,} | {r['algoritmo']} | {r['tempo_mediano_ms']:.3f} ms | {r['comparacoes']:,} |")
    return "\n".join(linhas)

def exibir_tabela_terminal(resultados):
    print("\n" + "="*70)
    print("      TABELA COMPARATIVA DE RESULTADOS - DESAFIO 2")
    print("="*70)
    print(f"{'Registros':<12} | {'Algoritmo':<14} | {'Tempo mediano (ms)':<20} | {'Comparações':<15}")
    print("-" * 70)
    for r in resultados:
        tamanho_fmt = f"{r['tamanho']:,}".replace(",", ".")
        comps_fmt = f"{r['comparacoes']:,}".replace(",", ".")
        tempo_fmt = f"{r['tempo_mediano_ms']:,.3f} ms".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"{tamanho_fmt:<12} | {r['algoritmo']:<14} | {tempo_fmt:<20} | {comps_fmt:<15}")
    print("="*70 + "\n")

def main():
    seed = 42
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        seed = int(sys.argv[1])
        
    resultados = executar_experimento(seed=seed)
    exibir_tabela_terminal(resultados)

    # Salva os resultados em arquivo JSON para ser consumido pelos gráficos e relatório
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_json = os.path.join(diretorio_atual, "resultados_experimento.json")
    with open(caminho_json, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)
    print(f"[Info] Resultados salvos com sucesso em: {caminho_json}")

if __name__ == "__main__":
    main()
