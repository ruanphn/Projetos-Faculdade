# Relatório Técnico Integrado e Registro de Progresso — AV2
**Disciplina:** Ciência de Dados e Inteligência Artificial  
**Instituição:** Faculdade INBEC | **Docente:** Prof. Jorge Barata  
**Equipe (Grupo 07):** Ruan Pereira, Daniel Matos, Pedro Moraes  
**Data:** Novembro de 2026  

---

## 1. Contextualização e Objetivo Geral

A avaliação da segunda etapa (AV2) tem como premissa consolidar a transição entre o entendimento teórico dos fundamentos estatísticos e a aplicação prática de algoritmos de aprendizado de máquina e reconhecimento de padrões.

A avaliação divide-se formalmente em duas entregas complementares:
1. **Trabalho 1: Do dado à decisão** — Um pipeline completo de ciência de dados desenvolvido e validado em ambiente interativo Jupyter/Colab, abordando desde a inferência estatística clássica e Teorema de Bayes até aprendizagem supervisionada (Naive Bayes) e não supervisionada (K-Means e PCA) sobre a base *Wine*.
2. **Trabalho 2: Leitura crítica de artigo científico** — Uma auditoria analítica e metodológica do estudo de Santos & Goya (SBSI 2020), que aborda a predição de evasão discente no ensino superior brasileiro via técnicas de aprendizado supervisionado e técnicas de balanceamento amostral (SMOTE).

---

## 2. Trabalho 1: Memorial de Execução e Resultados Detalhados

### 2.1 Identificação e Parâmetros Vinculados ao Grupo 07
* **Conjunto de Dados:** `wine` (178 amostras de vinhos originários de três cultivares distintas na Itália).
* **Vetor Alvo ($y$):** `cultivar` com três rótulos discretos: `cultivar_0` ($n=59$), `cultivar_1` ($n=71$) e `cultivar_2` ($n=48$).
* **Espaço de Características Reduzido ($X$):**
  * `alcohol` (teor alcoólico em volume %)
  * `malic_acid` (ácido málico em g/L)
  * `magnesium` (magnésio em mg/L)
  * `color_intensity` (intensidade da cor)
  * `proline` (concentração de prolina em mg/L)
* **Parâmetros Amostrais:** Split treino/teste com proporção 75%/25% (`test_size=0.25`), semente pseudoaleatória `random_state=77`, amostragem estratificada pela classe alvo.

---

### 2.2 Análise Passo a Passo das Etapas do Notebook

#### Etapa 1: Entendimento da Matriz de Dados e Qualidade
* **Dimensão da Matriz:** $n = 178$ linhas (observações) e $p = 13$ colunas de atributos físico-químicos originais.
* **Tipagem:** Todas as variáveis de atributos são numéricas contínuas (*float64*). A variável alvo `cultivar` e a variável derivada `alcohol_faixa` (categorizada via mediana) são qualitativas nominais.
* **Integridade:** Foram detectados 0 valores nulos na base. O procedimento de filtragem executado descartou 0 registros, preservando integralmente o poder estatístico do conjunto amostral.

#### Etapa 2: Inferência Estatística — Teste t de Welch
* **Variável Avaliada:** `magnesium` entre `cultivar_0` e `cultivar_1`.
* **Média Amostral Cultivar 0:** $106,339$ mg/L ($n_0 = 59$, desvio padrão $\approx 10,499$).
* **Média Amostral Cultivar 1:** $94,549$ mg/L ($n_1 = 71$, desvio padrão $\approx 16,753$).
* **Formulação das Hipóteses:**
  * Hipótese Nula ($H_0$): $\mu_0 = \mu_1 \implies \mu_0 - \mu_1 = 0$
  * Hipótese Alternativa ($H_1$): $\mu_0 \neq \mu_1 \implies \mu_0 - \mu_1 \neq 0$
* **Resultados Obtidos:**
  * Estatística $t = 4,886$
  * Graus de Liberdade Efetivos (Welch-Satterthwaite): $\approx 119,77$
  * **Valor-p:** $3,22 \times 10^{-6}$ ($0,00000322$)
  * **Intervalo de Confiança de 95% para a Diferença de Médias:** $[7,012; 16,567]$ mg/L
* **Conclusão Estatística:** Rejeita-se categoricamente a hipótese nula $H_0$ ao nível de significância $\alpha = 0,05$. O intervalo de confiança estritamente positivo confirma que vinhos da cultivar 0 apresentam concentração média de magnésio expressivamente superior aos vinhos da cultivar 1.

#### Etapa 3: Teorema de Bayes e Raciocínio Probabilístico
A partir da matriz de contingência bivariada entre `alcohol_faixa` e `cultivar`:

| Faixa de Álcool | Cultivar 0 | Cultivar 1 | Cultivar 2 | Total Geral |
| :--- | :---: | :---: | :---: | :---: |
| **Alto** (acima da mediana 13,05%) | 53 | 5 | 27 | **85** |
| **Baixo** (abaixo da mediana 13,05%)| 6 | 66 | 21 | **93** |
| **Total** | **59** | **71** | **48** | **178** |

* **Probabilidade a Priori:** $P(C) = P(\text{cultivar\_0}) = \frac{59}{178} \approx 0,3315$ (33,15%)
* **Verossimilhança:** $P(E \mid C) = P(\text{alto} \mid \text{cultivar\_0}) = \frac{53}{59} \approx 0,8983$ (89,83%)
* **Probabilidade Marginal da Evidência:** $P(E) = P(\text{alto}) = \frac{85}{178} \approx 0,4775$ (47,75%)
* **Probabilidade a Posterior:**
  $$P(C \mid E) = \frac{P(E \mid C) \cdot P(C)}{P(E)} = \frac{53}{85} \approx 0,6235 \quad (62,35\%)$$
* **Efeito da Alteração da Priori ($q = 0,10$):**
  * $P(E \mid \text{não } C) = \frac{5 + 27}{71 + 48} = \frac{32}{119} \approx 0,2689$
  * Nova posterior:
    $$P(C \mid E) = \frac{0,10 \times 0,8983}{(0,10 \times 0,8983) + (0,90 \times 0,2689)} = \frac{0,08983}{0,08983 + 0,24201} \approx 0,2707 \quad (27,07\%)$$
  * *Interpretação:* Demonstra empiricamente o princípio da indução bayesiana: mesmo mantendo a mesma evidência física observada, uma menor prevalência populacional basal (*priori*) ancora a probabilidade posterior em um patamar significativamente mais conservador.

#### Etapa 4: Aprendizado Supervisionado com GaussianNB
* **Treinamento e Validação:** Amostra particionada em 133 observações de treino e 45 de teste.
* **Acurácia no Treino:** $96,24\%$ (128 acertos em 133).
* **Acurácia no Teste:** $88,89\%$ (40 acertos em 45).
* **Matriz de Confusão no Teste:**
  $$\begin{bmatrix} 13 & 0 & 2 \\ 0 & 17 & 1 \\ 0 & 2 & 10 \end{bmatrix}$$
* **Discussão Teórica sobre a Suposição de Independência:** O par mais correlacionado no subespaço foi `alcohol` e `proline` ($r = 0,644$). Apesar de violar a premissa de independência condicional estatística exigida pelo Naive Bayes, o modelo mantém robustez preditiva porque a classificação depende da fronteira geométrica onde a probabilidade relativa de uma classe supera as demais, mantendo-se estável mesmo diante de distorções moderadas nas estimativas de densidade absoluta.

#### Etapa 5: Aprendizado Não Supervisionado, Espaço de Características e PCA
* **K-Means sem Normalização:** Pureza de **70,22%**. A variável `proline` (com valores absolutos na faixa de $10^3$) distorce a métrica euclidiana no espaço $\mathbb{R}^5$.
* **K-Means com Padronização (`StandardScaler`):** Pureza de **92,13%**. A transformação das variáveis para média 0 e variância 1 equilibra a contribuição geométrica de cada dimensão.
* **Análise de Componentes Principais (PCA):**
  * Projeção em 2 eixos principais ortogonais.
  * Variância explicada acumulada: **69,11%** (Componente 1: ~41,8%, Componente 2: ~27,3%).
  * A projeção em 2D comprova visualmente a separabilidade natural dos grupos formados pelo K-Means em correspondência quase perfeita com as cultivares reais.

---

## 3. Trabalho 2: Memorial da Análise do Artigo Científico

### 3.1 Ficha Técnica do Estudo
* **Título:** *Aprendizado de Máquina Aplicado à Análise de Evasão em Cursos de Sistemas de Informação*
* **Autoria:** Patricia D. Santos e Denise H. Goya (Universidade Federal do ABC - UFABC)
* **Veículo:** Simpósio Brasileiro de Sistemas de Informação (SBSI 2020), Trilha Estendida, pp. 210–213. DOI: `10.5753/sbsi.2020.13145`.

### 3.2 Resumo das Respostas com Referenciamento Direto
1. **Q1. Tipo de dados:** Estruturados (tabelas do Censo da Educação Superior / Inep, Seção 2, p. 210–211).
2. **Q2. Matriz e Dimensões:** $n_1 = 223.687$ e $n_2 = 94.692$; $p = 14$; $y$ = evasão. Configuração típica de $n \gg p$ (Seção 2, p. 211 e Abstract, p. 210).
3. **Q3. Tarefa:** Reconhecimento/classificação supervisionada binária.
4. **Q4. Aprendizagem:** Supervisionada de classificação tabular (Random Forest, AdaBoost, KNN, Logistic Regression, Voting Classifier).
5. **Q5. Pré-processamento:** Limpeza de registros inconsistentes/ruídos e Seleção de características (ranqueamento de importância via impureza de Gini na Floresta Aleatória, Tabela 3, p. 212).
6. **Q6. Validação:** Split 75/25 e 5-fold cross validation no treino com SMOTE. Métrica principal: Cobertura (*Recall*) = **85,61%** (Tabela 2, p. 212).
7. **Q7. Inferência:** Nenhum teste de hipótese ou intervalo de confiança formal conduzido.
8. **Q8. Custos de Erro e Balanceamento:**
   * Tipo I: Classificar discente persistente como evadido.
   * Tipo II: Não detectar o discente que vai evadir (mais grave devido à perda irreversível da intervenção de retenção institucional).
   * Desbalanceamento severo corrigido com SMOTE no treino.
9. **Q9. Análise Crítica do Trio:** Alerta para o risco de *data leakage* e superestimação de desempenho decorrentes da falta de particionamento temporal (*time-based split*) em dados longitudinais (2014-2018), propondo calibração bayesiana para controlar a influência das prioris desbalanceadas na prática.

---

## 4. Roteiro e Argumentação para a Defesa Oral

A defesa oral de 7 minutos exige clareza e domínio conceitual de qualquer membro do trio:

* **Ponto 1: Por que usar teste t de Welch em vez de Student tradicional?**  
  * *Argumento:* O teste de Welch não pressupõe homocedasticidade (variâncias populacionais iguais), sendo mais robusto para amostras reais onde os desvios padrões diferem (como observado: $\sim 10,5$ no cultivar 0 vs $\sim 16,8$ no cultivar 1).
* **Ponto 2: O que significa pureza de um cluster no aprendizado não supervisionado?**  
  * *Argumento:* A pureza é a proporção de elementos pertencentes à classe majoritária dentro de cada agrupamento gerado pelo K-Means. Uma pureza de 92,13% atesta que, mesmo sem receber qualquer rótulo durante o treino, a proximidade físico-química dos vinhos no espaço vetorial padronizado bastou para reconstruir as classes reais com alta precisão.
* **Ponto 3: Por que a Floresta Aleatória superou os demais modelos no artigo de evasão?**  
  * *Argumento:* Porque conjuntos (*ensembles*) de árvores de decisão lidam excepcionalmente bem com dados tabulares heterogêneos, capturando relações não lineares e interações complexas entre atributos socioeconômicos e acadêmicos sem sofrer severamente com escala de variáveis.
