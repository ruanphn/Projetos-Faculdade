# Atividade Prática — Estruturas de Dados
**Árvores Binárias de Busca e Algoritmos de Ordenação**

- **Estudante:** Ruan Pereira do Nascimento
- **Curso:** Análise e Desenvolvimento de Sistemas
- **Linguagem:** Python 3.13
- **Avaliação:** Prática (3,0 pontos)

---

## 📂 Estrutura do Repositório e da Entrega

```text
BARATA/
├── desafio1_arvore/              # DESAFIO 1: Árvore Binária de Busca (ABB)
│   ├── produto.py                # Classe Produto (modelo de dados)
│   ├── no.py                     # Classe No (nó com ponteiros esq/dir)
│   ├── arvore_binaria.py         # Classe ArvoreBinariaBusca (inserção, busca e percursos)
│   ├── main.py                   # Menu interativo CLI e modo demonstração (--demo)
│   └── README.md                 # Documentação e guia do Desafio 1
│
├── desafio2_ordenacao/           # DESAFIO 2: Comparação de Algoritmos de Ordenação
│   ├── aluno.py                  # Classe Aluno e gerador gerar_alunos()
│   ├── ordenacao.py              # Implementações manuais de Bubble Sort e Merge Sort
│   ├── experimento.py            # Baterias de 100, 1.000 e 5.000 (3 medições e mediana)
│   ├── main.py                   # Script de execução dos experimentos e exibição da tabela
│   ├── resultados_experimento.json # Dados brutos dos experimentos em formato estruturado
│   └── README.md                 # Documentação e guia do Desafio 2
│
├── relatorio/                    # RELATÓRIO TÉCNICO E ARTEFATOS VISUAIS
│   ├── Relatorio_Estruturas_Dados.pdf # Relatório final completo em PDF (5 páginas diagramadas)
│   ├── gerar_relatorio_pdf.py    # Script que compila o PDF com ReportLab
│   ├── gerar_graficos.py         # Script que gera os gráficos comparativos
│   ├── gerar_terminal_screenshots.py # Script que gera as evidências visuais de execução
│   └── graficos/                 # Gráficos de tempo, comparações, ABB e prints de terminal
│
├── entrega_projeto.zip           # Arquivo ZIP completo pronto para envio
└── README.md                     # Visão geral do projeto e instruções
```

---

## 🚀 Como Executar

### 1. Desafio 1 — Árvore Binária de Busca

Para iniciar o menu interativo com opções de cadastro, busca, percursos e testes:
```bash
python desafio1_arvore/main.py
```

Para rodar a demonstração automática com todos os dados da tabela oficial em 1 segundo:
```bash
python desafio1_arvore/main.py --demo
```

### 2. Desafio 2 — Algoritmos de Ordenação

Para rodar o benchmark completo dos algoritmos Bubble Sort e Merge Sort (100, 1.000 e 5.000 registros com seed 42):
```bash
python desafio2_ordenacao/main.py
```

### 3. Regenerar Gráficos e Relatório em PDF

Para reproduzir os gráficos analíticos e regerar o relatório em PDF com ReportLab:
```bash
python relatorio/gerar_graficos.py
python relatorio/gerar_terminal_screenshots.py
python relatorio/gerar_relatorio_pdf.py
```

---

## 📊 Resumo dos Resultados Experimentais (Desafio 2)

| Registros | Algoritmo | Tempo mediano (ms) | Comparações de Notas |
|---|---|---|---|
| **100** | Bubble Sort | 0,619 ms | 4.884 |
| **100** | Merge Sort | 0,177 ms | 539 |
| **1.000** | Bubble Sort | 82,607 ms | 498.905 |
| **1.000** | Merge Sort | 2,294 ms | 8.720 |
| **5.000** | Bubble Sort | 2.158,379 ms | 12.493.314 |
| **5.000** | Merge Sort | 12,620 ms | 55.198 |

---

## 📝 Resumo das Questões de Análise

### Desafio 1 (Árvore Binária de Busca)
1. **Raiz da Árvore:** Notebook (código 50), pois foi o primeiro registro inserido na árvore vazia.
2. **Percurso em Ordem:** `20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80` (ordenação estritamente crescente decorrente da propriedade da ABB).
3. **Diferença dos Percursos:**
   - **Pré-ordem (R-E-D):** Processa o nó antes das subárvores (usado para clonar e reconstruir a topologia da árvore).
   - **Em ordem (E-R-D):** Processa esquerda, raiz e direita (usado para recuperar os dados ordenados).
   - **Pós-ordem (E-D-R):** Processa as subárvores antes da raiz (usado para desalocação de memória e cálculo cumulativo).
4. **Nós visitados na busca do código 60:** Exatamente **3 nós** (Caminho: `50 -> 70 -> 60`).
5. **Inserção em ordem crescente:** A árvore sofre **degeneração em lista encadeada** com altura $h = n$, degradando a complexidade de busca e inserção de $O(\log n)$ para **$O(n)$** no pior caso.

### Desafio 2 (Ordenação)
1. **Menor tempo:** O **Merge Sort** foi o mais rápido em todos os tamanhos (chegando a ser **171x mais rápido** para 5.000 registros).
2. **Impacto do crescimento de 100 para 5.000 (fator 50x):**
   - Bubble Sort aumentou comparações em **2.558x** e tempo em **3.486x** (comportamento quadrático $O(n^2)$).
   - Merge Sort aumentou comparações em apenas **102x** e tempo em **71x** (comportamento linearítmico $O(n \log n)$).
3. **Menos comparações:** Merge Sort realizou **99,56% menos comparações** para 5.000 registros (55.198 vs 12.493.314).
4. **Influência da Divisão e Conquista:** Divide a entrada em $\log_2 n$ níveis e intercala com custo linear $n$ por nível, garantindo teto $O(n \log n)$ constante.
5. **Mais apropriado para 100.000 registros:** O **Merge Sort** (tempo $< 0,3$ s contra 15 a 20 minutos estimados do Bubble Sort).
6. **Memória Auxiliar:** Merge Sort consome memória auxiliar $O(n)$. Em cenários com RAM extremamente restrita, algoritmos *in-place* como QuickSort ($O(\log n)$) ou HeapSort ($O(1)$) são preferíveis, mas em sistemas modernos o ganho de tempo do Merge Sort é plenamente justificado.
