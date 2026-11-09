# Plano de Execução - AV2: Ciência de Dados e IA
**Faculdade INBEC** | **Professor:** Jorge Barata  
**Grupo 07:** Ruan Pereira, Daniel Matos, Pedro Moraes  

---

## 1. Visão Geral e Distribuição dos Trabalhos

A avaliação é dividida em dois trabalhos em trio (0 a 5 pontos cada), além de uma defesa oral única que cobre ambos.

```
AV2 (Nota Final) = Trabalho 1 (4,0 escr. + 1,0 oral) + Trabalho 2 (4,0 escr. + 1,0 oral) = 10,0
```

| Item | Trabalho 2: Leitura Crítica de Artigo | Trabalho 1: Do Dado à Decisão |
| :--- | :--- | :--- |
| **Tema / Alvo** | Evasão em Cursos de Sistemas de Informação | Classificação de Cultivares de Vinho (`wine`) |
| **Material Base** | Artigo de Santos & Goya (SBSI 2020) | Notebook `Trabalho1_Do_dado_a_decisao.ipynb` |
| **Exige Código?**| Não (Ficha analítica estruturada) | Sim (Python no Google Colab / Jupyter) |
| **Formato de Envio**| Arquivo PDF: `T2_Grupo07.pdf` (máx. 2 páginas) | Notebook com saídas: `T1_Grupo07.ipynb` |
| **Data Limite** | **10/11/2026 até 23h59** ⚠️ *(Vence primeiro)* | **16/11/2026 até 23h59** |
| **Defesa Oral** | 17/11/2026 e 24/11/2026 (Sorteio na aula, ~7 min por grupo, material aberto) |

---

## 2. Parâmetros Específicos do Grupo 07

### Trabalho 1 (Notebook):
* **Dataset:** `wine` (178 amostras, 3 classes: `cultivar_0`, `cultivar_1`, `cultivar_2`).
* **Variável Alvo ($y$):** `cultivar`.
* **Features Selecionadas ($X$):** `['alcohol', 'malic_acid', 'magnesium', 'color_intensity', 'proline']` (5 características).
* **Etapa 2 (Inferência):** Teste $t$ de Welch em `magnesium` comparando `cultivar_0` vs `cultivar_1`, com nível de significância $\alpha = 0,05$.
* **Etapa 3 (Teorema de Bayes à mão):** Cálculo de $P(\text{cultivar} = \text{cultivar\_0} \mid \text{alcohol} = \text{alto})$ a partir da tabela de contingência, e recálculo com a nova priori $q = 0,10$.
* **Etapa 4 (Supervisionado):** Classificador `GaussianNB`, divisão de treino/teste com `test_size=0.25` e `random_state=77`, estratificado por $y$.
* **Etapa 5 (Não Supervisionado):** Agrupamento `KMeans(n_clusters=3)` sem e com normalização (`StandardScaler`), cálculo de pureza e redução dimensional via `PCA(n_components=2)`.
* **Reflexão:** Respostas R1, R2 e R3 com foco conceitual sólido em até 5 linhas cada.

### Trabalho 2 (Ficha de Artigo):
* **Artigo:** Santos e Goya. *Aprendizado de Máquina Aplicado à Análise de Evasão em Cursos de Sistemas de Informação*, SBSI 2020, p. 210-213. DOI: `10.5753/sbsi.2020.13145`.
* **Foco da Avaliação:** Preenchimento estrito de Q1 a Q8 com evidências explícitas (seção, página, tabela/figura) sem introdução nem resumo, mais a questão discursiva crítica Q9 (até 10 linhas) e declaração de contribuição dos membros.

---

## 3. Cronograma de Execução Fase a Fase

```mermaid
flowchart TD
    subgraph Fase 1 [Fase 1: Trabalho 2 - Prazo 10/11]
        F1_1[Download e leitura do artigo de Santos & Goya] --> F1_2[Preenchimento minucioso das questões Q1 a Q8 com evidências]
        F1_2 --> F1_3[Elaboração da análise crítica técnica Q9]
        F1_3 --> F1_4[Geração do PDF T2_Grupo07.pdf em exatamente 2 páginas]
    end

    subgraph Fase 2 [Fase 2: Trabalho 1 - Prazo 16/11]
        F2_1[Configuração do cabeçalho e GRUPO = 7 no notebook] --> F2_2[Completar código das etapas 2, 4 e 5]
        F2_2 --> F2_3[Desenvolver cálculos manuais da Etapa 3]
        F2_3 --> F2_4[Redigir respostas teóricas objetivas em até 5 linhas]
        F2_4 --> F2_5[Executar notebook gerando T1_Grupo07.ipynb com saídas]
    end

    subgraph Fase 3 [Fase 3: Preparação para Defesa Oral - 17 e 24/11]
        F3_1[Guia de perguntas prováveis da banca / Prof. Jorge Barata]
        F3_2[Alinhamento dos três integrantes com o material aberto]
    end

    Fase 1 --> Fase 2 --> Fase 3
```

---

## 4. Divisão de Contribuição da Equipe
* **Ruan Pereira:** Implementação técnica e execução das rotinas de código do Trabalho 1; extração dos metadados e pré-processamento para a ficha do Trabalho 2.
* **Daniel Matos:** Formulação e verificação dos cálculos do Teorema de Bayes e teste $t$; mapeamento de métricas, matrizes de confusão e erros Tipo I e II do artigo.
* **Pedro Moraes:** Redação das respostas conceituais e reflexões finais (R1 a R3); elaboração da análise crítica da questão Q9 e revisão da coesão do projeto.

