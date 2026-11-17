"""
Gera gráficos de alta resolução para o relatório técnico comparativo.
Utiliza matplotlib para ilustrar:
1. Tempo Mediano de Execução (Bubble Sort vs Merge Sort)
2. Total de Comparações de Notas
3. Diagrama da Árvore Binária de Busca (Desafio 1)
"""
import os
import json
import matplotlib.pyplot as plt
import numpy as np

# Configurações de estilo
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.size'] = 11

def carregar_dados():
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(dir_atual, "..", "desafio2_ordenacao", "resultados_experimento.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def gerar_graficos():
    dados = carregar_dados()
    dir_graficos = os.path.join(os.path.dirname(os.path.abspath(__file__)), "graficos")
    os.makedirs(dir_graficos, exist_ok=True)

    tamanhos = [100, 1000, 5000]
    tempo_bubble = [d["tempo_mediano_ms"] for d in dados if d["algoritmo"] == "Bubble Sort"]
    tempo_merge = [d["tempo_mediano_ms"] for d in dados if d["algoritmo"] == "Merge Sort"]
    
    comp_bubble = [d["comparacoes"] for d in dados if d["algoritmo"] == "Bubble Sort"]
    comp_merge = [d["comparacoes"] for d in dados if d["algoritmo"] == "Merge Sort"]

    # -------------------------------------------------------------
    # Gráfico 1: Tempo de Execução (ms)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
    x = np.arange(len(tamanhos))
    largura = 0.35

    rects1 = ax.bar(x - largura/2, tempo_bubble, largura, label='Bubble Sort (O(n²))', color='#e74c3c', edgecolor='black')
    rects2 = ax.bar(x + largura/2, tempo_merge, largura, label='Merge Sort (O(n log n))', color='#2ecc71', edgecolor='black')

    ax.set_title('Comparação de Tempo Mediano de Execução (ms)', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Quantidade de Registros (Alunos)', fontsize=12, labelpad=10)
    ax.set_ylabel('Tempo Mediano (ms) - Escala Logarítmica', fontsize=12, labelpad=10)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{t:,}" for t in tamanhos])
    ax.set_yscale('log')
    ax.legend(frameon=True, facecolor='white', framealpha=0.9)
    ax.grid(True, which="both", ls="--", alpha=0.5)

    # Rótulos nas barras
    for rect in rects1:
        altura = rect.get_height()
        ax.annotate(f'{altura:.2f} ms',
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 4), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
    for rect in rects2:
        altura = rect.get_height()
        ax.annotate(f'{altura:.2f} ms',
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 4), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()
    caminho_tempo = os.path.join(dir_graficos, "grafico_tempo.png")
    plt.savefig(caminho_tempo)
    plt.close()
    print(f"[Grafico] Salvo: {caminho_tempo}")

    # -------------------------------------------------------------
    # Gráfico 2: Comparações de Notas
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

    rects1 = ax.bar(x - largura/2, comp_bubble, largura, label='Bubble Sort', color='#c0392b', edgecolor='black')
    rects2 = ax.bar(x + largura/2, comp_merge, largura, label='Merge Sort', color='#27ae60', edgecolor='black')

    ax.set_title('Comparação do Total de Comparações entre Notas', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Quantidade de Registros (Alunos)', fontsize=12, labelpad=10)
    ax.set_ylabel('Comparações Efetuadas - Escala Logarítmica', fontsize=12, labelpad=10)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{t:,}" for t in tamanhos])
    ax.set_yscale('log')
    ax.legend(frameon=True, facecolor='white', framealpha=0.9)
    ax.grid(True, which="both", ls="--", alpha=0.5)

    for rect in rects1:
        altura = rect.get_height()
        ax.annotate(f'{altura:,.0f}'.replace(",", "."),
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 4), textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, fontweight='bold')
    for rect in rects2:
        altura = rect.get_height()
        ax.annotate(f'{altura:,.0f}'.replace(",", "."),
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 4), textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, fontweight='bold')

    plt.tight_layout()
    caminho_comp = os.path.join(dir_graficos, "grafico_comparacoes.png")
    plt.savefig(caminho_comp)
    plt.close()
    print(f"[Grafico] Salvo: {caminho_comp}")

    # -------------------------------------------------------------
    # Gráfico 3: Diagrama da Árvore Binária de Busca (Desafio 1)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=300)
    ax.set_title('Topologia da Árvore Binária de Busca (Desafio 1)', fontsize=14, fontweight='bold', pad=15)

    # Coordenadas fixas para os 7 nós da ABB montada com a tabela oficial
    posicoes = {
        50: (0.5, 0.85),
        30: (0.25, 0.55),
        70: (0.75, 0.55),
        20: (0.125, 0.25),
        40: (0.375, 0.25),
        60: (0.625, 0.25),
        80: (0.875, 0.25),
    }

    nomes = {
        50: "Notebook\nR$ 3.500",
        30: "Mouse\nR$ 80",
        70: "Monitor\nR$ 900",
        20: "Teclado\nR$ 150",
        40: "Webcam\nR$ 250",
        60: "SSD\nR$ 420",
        80: "Impressora\nR$ 1.200",
    }

    conexoes = [
        (50, 30), (50, 70),
        (30, 20), (30, 40),
        (70, 60), (70, 80)
    ]

    for p_pai, p_filho in conexoes:
        x_vals = [posicoes[p_pai][0], posicoes[p_filho][0]]
        y_vals = [posicoes[p_pai][1], posicoes[p_filho][1]]
        ax.plot(x_vals, y_vals, color='#7f8c8d', lw=2, zorder=1)

    for cod, (px, py) in posicoes.items():
        cor_no = '#f39c12' if cod == 50 else ('#3498db' if cod == 60 else '#ecf0f1')
        borda = '#d35400' if cod == 50 else ('#2980b9' if cod == 60 else '#7f8c8d')
        texto_cor = 'black' if cod not in [50, 60] else 'white'
        
        ax.scatter(px, py, s=1800, color=cor_no, edgecolor=borda, lw=2.5, zorder=2)
        ax.text(px, py + 0.015, f"Cód: {cod}", ha='center', va='center', fontsize=10, fontweight='bold', color=texto_cor, zorder=3)
        ax.text(px, py - 0.055, nomes[cod], ha='center', va='center', fontsize=8, color='#2c3e50', zorder=3)

    ax.text(0.5, 0.05, "Destaques: [50] Raiz da ABB | [60] Nó localizado em 3 passos (50 -> 70 -> 60)",
            ha='center', va='center', fontsize=10, fontstyle='italic', bbox=dict(boxstyle="round,pad=0.4", fc="#e8f8f5", ec="#1abc9c", lw=1.5))

    ax.set_xlim(0.05, 0.95)
    ax.set_ylim(0.0, 1.0)
    ax.axis('off')
    plt.tight_layout()
    caminho_arvore = os.path.join(dir_graficos, "grafico_arvore.png")
    plt.savefig(caminho_arvore)
    plt.close()
    print(f"[Grafico] Salvo: {caminho_arvore}")

if __name__ == "__main__":
    gerar_graficos()
