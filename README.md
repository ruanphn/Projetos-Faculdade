# Atividade Prática — Estruturas de Dados
**Árvores Binárias de Busca e Algoritmos de Ordenação**

- **Estudante:** Ruan Pereira do Nascimento
- **Curso:** Análise e Desenvolvimento de Sistemas
- **Linguagem:** Python 3.13
- **Avaliação:** Prática (3,0 pontos)

---

## 📂 Estrutura do Projeto

```text
BARATA/
├── desafio1_arvore/              # DESAFIO 1: Árvore Binária de Busca (ABB)
│   ├── produto.py                # Classe Produto
│   ├── no.py                     # Classe No
│   ├── arvore_binaria.py         # Implementação da ABB (inserção, busca e percursos)
│   ├── main.py                   # Menu interativo CLI e modo demonstração (--demo)
│   └── README.md                 # Instruções de execução do Desafio 1
│
├── desafio2_ordenacao/           # DESAFIO 2: Comparação de Algoritmos de Ordenação
│   ├── aluno.py                  # Classe Aluno e gerador de dados
│   ├── ordenacao.py              # Implementações manuais de Bubble Sort e Merge Sort
│   ├── experimento.py            # Baterias de 100, 1.000 e 5.000 registros
│   ├── main.py                   # Script de execução do experimento
│   └── README.md                 # Instruções de execução do Desafio 2
│
├── Relatorio_Estruturas_Dados.pdf # Relatório técnico oficial em PDF
├── entrega_projeto.zip           # Arquivo ZIP final para submissão
└── README.md                     # Visão geral e instruções
```

---

## 🚀 Como Executar

### 1. Desafio 1 — Árvore Binária de Busca

Modo interativo (menu):
```bash
python desafio1_arvore/main.py
```

Modo demonstração automática (executa a tabela oficial e percursos):
```bash
python desafio1_arvore/main.py --demo
```

### 2. Desafio 2 — Algoritmos de Ordenação

Executar o experimento comparativo (100, 1.000 e 5.000 registros):
```bash
python desafio2_ordenacao/main.py
```

---

## 📊 Resultados Experimentais (Desafio 2)

| Registros | Algoritmo | Tempo mediano (ms) | Comparações de Notas |
|---|---|---|---|
| **100** | Bubble Sort | 0,619 ms | 4.884 |
| **100** | Merge Sort | 0,177 ms | 539 |
| **1.000** | Bubble Sort | 82,607 ms | 498.905 |
| **1.000** | Merge Sort | 2,294 ms | 8.720 |
| **5.000** | Bubble Sort | 2.158,379 ms | 12.493.314 |
| **5.000** | Merge Sort | 12,620 ms | 55.198 |

---

## 📝 Respostas às Questões de Análise

### Desafio 1 (Árvore Binária de Busca)
1. **Raiz da Árvore:** Notebook (código 50), primeiro elemento inserido na árvore vazia.
2. **Percurso em Ordem:** `20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80` (ordem crescente garantida pela propriedade da ABB).
3. **Diferença dos Percursos:**
   - **Pré-ordem (R-E-D):** Processa o nó antes das subárvores (utilizado para clonar ou serializar a estrutura original).
   - **Em ordem (E-R-D):** Processa esquerda, raiz e direita (recupera os elementos em ordem crescente).
   - **Pós-ordem (E-D-R):** Processa subárvores antes da raiz (utilizado para desalocação de memória e cálculo cumulativo).
4. **Nós visitados na busca do código 60:** Exatamente **3 nós** (Caminho: `50 -> 70 -> 60`).
5. **Inserção em ordem crescente:** A árvore degenera em **lista encadeada** com altura $h = n$, degradando a complexidade de busca e inserção de $O(\log n)$ para **$O(n)$** no pior caso.

### Desafio 2 (Ordenação)
1. **Menor tempo:** O **Merge Sort** apresentou menor tempo em todos os tamanhos (até 171x mais rápido para 5.000 registros).
2. **Impacto do crescimento de 100 para 5.000 (fator 50x):**
   - Bubble Sort aumentou comparações em 2.558x e tempo em 3.486x ($O(n^2)$).
   - Merge Sort aumentou comparações em 102x e tempo em 71x ($O(n \log n)$).
3. **Menos comparações:** Merge Sort efetuou 99,56% menos comparações para 5.000 registros (55.198 vs 12.493.314).
4. **Influência da Divisão e Conquista:** Divide a entrada em $\log_2 n$ níveis e intercala com custo linear $n$ por nível, mantendo complexidade $O(n \log n)$ invariante.
5. **Mais apropriado para 100.000 registros:** O **Merge Sort** (tempo estimado $< 0,3$ s contra 15 a 20 minutos do Bubble Sort).
6. **Memória Auxiliar:** Merge Sort requer memória adicional $O(n)$ para intercalação. Em sistemas com memória extremamente restrita, algoritmos *in-place* como QuickSort ($O(\log n)$) ou HeapSort ($O(1)$) são opções adequadas, embora o ganho de tempo do Merge Sort justifique seu uso na ampla maioria dos sistemas.
