# Desafio 2 — Comparação de Algoritmos de Ordenação (Bubble Sort vs Merge Sort)

Este módulo implementa a geração determinística de registros acadêmicos e a comparação empírica de desempenho entre os algoritmos **Bubble Sort** e **Merge Sort**.

## 📁 Estrutura dos Arquivos

- `aluno.py`: Definição da classe `Aluno` (matrícula, nome, nota) e gerador `gerar_alunos()`.
- `ordenacao.py`: Implementação manual dos algoritmos Bubble Sort e Merge Sort, com contagem estrita de comparações entre notas (sem uso de `sort()` ou `sorted()`).
- `experimento.py`: Rotina de instrumentação com `time.perf_counter()`, 3 repetições, cálculo da mediana (ms), contagem de comparações e validações de integridade.
- `main.py`: Script principal que executa os testes para 100, 1.000 e 5.000 registros e exibe a tabela comparativa.

## 🚀 Como Executar

```bash
python main.py
```

Você também pode fornecer uma semente alternativa via argumento:
```bash
python main.py 123
```
*(Por padrão, utiliza semente 42).*
