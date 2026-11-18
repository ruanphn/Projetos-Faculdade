import sys
from experimento import executar_experimento

def exibir_tabela(resultados):
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
    exibir_tabela(resultados)

if __name__ == "__main__":
    main()
