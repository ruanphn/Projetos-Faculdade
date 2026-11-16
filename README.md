# AV2: Ciência de Dados e Inteligência Artificial
**Faculdade INBEC** | **Professor:** Jorge Barata  
**Grupo 07:** Ruan Pereira, Daniel Matos, Pedro Moraes  

---

## 📌 Sumário Executivo

Este repositório reúne os dois trabalhos avaliativos que compõem a nota da **AV2** da disciplina de **Ciência de Dados e Inteligência Artificial**, bem como os materiais de apoio e roteiro para a **Defesa Oral**.

A composição da nota é dada por:
$$\text{Nota Final AV2} = \text{Trabalho 1 (4,0 escr. + 1,0 oral)} + \text{Trabalho 2 (4,0 escr. + 1,0 oral)} = 10,0$$

---

## 👥 Identificação da Equipe e Contribuições

| Integrante | Atribuições Principais |
| :--- | :--- |
| **Ruan Pereira** | Configuração dos parâmetros do Grupo 07, implementação das rotinas em Python, execução e verificação do notebook `T1_Grupo07.ipynb` e análise dos metadados/dados estruturados do Trabalho 2. |
| **Daniel Matos** | Cálculos manuais e dedução analítica do Teorema de Bayes, condução do teste $t$ de Welch e intervalos de confiança; mapeamento das métricas preditivas, validação cruzada e análise dos erros Tipo I/II do artigo. |
| **Pedro Moraes** | Redação técnica das justificativas conceituais (itens 1.1 a 5.3) e reflexões finais (R1 a R3); elaboração da análise crítica metodológica (Q9) e revisão geral da fundamentação teórica. |

---

## 📂 Estrutura do Repositório

```text
├── T1_Grupo07.ipynb                                   # Trabalho 1: Notebook final executado com saídas e gráficos
├── T2_Grupo07.pdf                                     # Trabalho 2: Ficha analítica crítica de 2 páginas em PDF
├── Santos_Goya_2020_Evasao_Sistemas_Informacao.pdf     # Artigo científico oficial do Grupo 07 (SBSI 2020)
├── 20261027_19131_Trabalhos da AV2 Ciência de Dados...pdf # Enunciado e critérios de avaliação da disciplina
├── 20261027_191410_Trabalhos_AV2_Ciencia_de_Dados.pdf # Apresentação de suporte do professor
├── PLANO_DE_EXECUCAO_AV2.md                           # Planejamento estratégico e cronograma fase a fase
├── RELATORIO_FINAL_AV2.md                             # Relatório técnico completo de todo o progresso
└── README.md                                          # Visão geral e documentação do repositório
```

---

## 🍷 Trabalho 1: Do Dado à Decisão (`T1_Grupo07.ipynb`)

* **Conjunto de Dados:** `Wine` (*scikit-learn*)
* **Variável Alvo ($y$):** `cultivar` (`cultivar_0`, `cultivar_1`, `cultivar_2`)
* **Variáveis Preditivas ($X$):** `['alcohol', 'malic_acid', 'magnesium', 'color_intensity', 'proline']`
* **Divisão de Amostras:** `test_size=0.25`, `random_state=77`, estratificado por $y$

### Principais Conclusões e Resultados Numéricos

1. **Entendimento dos Dados (Etapa 1):**
   * $n = 178$ observações tabulares e $p = 13$ atributos contínuos originais ($p = 5$ selecionados para modelagem).
   * Valores ausentes removidos: **0 linhas** (base íntegra). A alternativa teórica para dados faltantes discutida foi a imputação por mediana ou modelos multivariados (KNN).

2. **Inferência Estatística (Etapa 2 - Teste $t$ de Welch):**
   * Comparação do teor de `magnesium` entre `cultivar_0` ($\bar{x}_0 = 106,339$) e `cultivar_1` ($\bar{x}_1 = 94,549$).
   * $H_0: \mu_0 = \mu_1$ vs. $H_1: \mu_0 \neq \mu_1$.
   * Estatística $t = 4,886$, **valor-p** $= 3,22 \times 10^{-6} < \alpha = 0,05$.
   * **Decisão:** Rejeição de $H_0$. O IC de 95% da diferença entre as médias $[7,012; 16,567]$ é estritamente positivo e não contém o zero, provando que vinhos da cultivar 0 têm teor de magnésio significativamente maior.

3. **Teorema de Bayes (Etapa 3 - Cálculo à Mão):**
   * Classe $C$: `cultivar_0` (59 vinhos) | Evidência $E$: `alcohol_faixa = alto` (85 vinhos no total, sendo 53 da classe C).
   * **Priori:** $P(C) = \frac{59}{178} \approx 33,15\%$
   * **Verossimilhança:** $P(E \mid C) = \frac{53}{59} \approx 89,83\%$
   * **Evidência:** $P(E) = \frac{85}{178} \approx 47,75\%$
   * **Posterior:** $P(C \mid E) = \frac{P(E \mid C) \cdot P(C)}{P(E)} = \frac{53}{85} \approx 62,35\%$
   * **Com nova priori $q = 0,10$:**  
     $P(E \mid \text{não } C) = \frac{32}{119} \approx 26,89\%$  
     $P(C \mid E) = \frac{0,10 \times 0,8983}{0,10 \times 0,8983 + 0,90 \times 0,2689} \approx 27,07\%$

4. **Aprendizado Supervisionado (Etapa 4 - Naive Bayes Gaussiano):**
   * Acurácia Treino: **96,24%** | Acurácia Teste: **88,89%**.
   * Não há indício de sobreajuste crítico. Apesar da correlação de 0,644 entre `alcohol` e `proline` violar a hipótese estrita de independência condicional, o modelo classifica com alta eficácia porque as fronteiras de decisão dependem prioritariamente da ordenação relativa das probabilidades.

5. **Aprendizado Não Supervisionado e PCA (Etapa 5):**
   * Pureza **sem normalização**: **70,22%** (distorcida pela escala da variável `proline`, cujos valores chegam a 1680).
   * Pureza **com normalização (`StandardScaler`)**: **92,13%** (alta concordância com as cultivares reais).
   * **PCA:** Redução para 2 componentes principais preservando **69,11%** da variância total, viabilizando projeção cartesiana clara dos agrupamentos.

---

## 📄 Trabalho 2: Leitura Crítica de Artigo (`T2_Grupo07.pdf`)

* **Artigo Analisado:** *Aprendizado de Máquina Aplicado à Análise de Evasão em Cursos de Sistemas de Informação*
* **Autores:** Patricia D. Santos, Denise H. Goya (UFABC)
* **Publicação:** SBSI 2020, p. 210–213 · DOI: `10.5753/sbsi.2020.13145`
* **Formato Entregue:** PDF estrito de 2 páginas, sem resumos desnecessários, com evidências apontadas por página, seção e tabela.

### Síntese das Respostas da Ficha Técnica

* **Q1 (Tipo de dados):** Dados estruturados (tabelas) do Censo da Educação Superior (Inep) 2014–2018 (Metodologia, p. 210–211).
* **Q2 (Matriz $X$ e vetor $y$):** $n = 223.687$ (Persp. 1) e $94.692$ (Persp. 2); $p = 14$ variáveis; $y$ = Situação de evasão. **$n$ muito maior que $p$** ($n \gg p$).
* **Q3 (Tipo de tarefa):** Reconhecimento ou classificação (categorização supervisionada binária).
* **Q4 (Aprendizagem):** Supervisionada de Classificação (Random Forest, AdaBoost, KNN, Regressão Logística e Voting Classifier).
* **Q5 (Pré-processamento):** Limpeza/tratamento de valores ausentes (eliminação de ruído na Persp. 2) e Seleção de características (Tabela 3: 12-14 atributos mais informativos via impureza de Gini).
* **Q6 (Validação contra sobreajuste):** Split treino/teste (75/25) + Validação cruzada (5-fold CV no treino com SMOTE). Métrica prioritária: **Cobertura (*Recall*) = 85,61%** (Tabela 2, p. 212).
* **Q7 (Inferência estatística):** Nenhum (não foram calculados valores-p nem intervalos de confiança).
* **Q8 (Erros e priori):**
  * Erro Tipo I (Falso Positivo): Classificar como evadido um aluno que iria se formar.
  * Erro Tipo II (Falso Negativo): Classificar como persistente um aluno que vai evadir.
  * **Mais grave:** Tipo II (perda da oportunidade de intervenção pedagógica preventiva).
  * **Classes balanceadas?** Não (34,77% na Persp. 1 e 81,90% na Persp. 2; exigiu SMOTE no treino).
* **Q9 (Análise crítica metodológica):** Aponta a ausência de divisão temporal (*time-based split*) em dados longitudinais (2014 a 2018), gerando risco de *data leakage* e sobreajuste; e a ausência de calibração bayesiana para lidar com a drástica alteração da priori entre as perspectivas.

---

## 🎯 Guia Rápido para a Defesa Oral (Banca / Prof. Jorge Barata)

1. **Pergunta Provável 1:** *"Por que a pureza do K-Means saltou de 70% para 92% após a normalização no Trabalho 1?"*  
   * **Resposta:** A variável `proline` varia de centenas até ~1600, enquanto `malic_acid` fica abaixo de 5. Sem padronização, a distância euclidiana é inteiramente dominada pelo `proline`. Ao normalizar com `StandardScaler` (média 0, desvio padrão 1), todas as 5 variáveis competem com o mesmo peso.

2. **Pergunta Provável 2:** *"No artigo de evasão, por que a métrica prioritária foi a Cobertura (Recall) e não a Acurácia?"*  
   * **Resposta:** Devido ao custo assimétrico do erro. Um falso negativo (deixar de identificar um aluno que vai evadir) faz a universidade perder a chance de agir preventivamente. Como a acurácia é inflada pelo desbalanceamento, a cobertura foca em capturar o máximo de evadidos reais.

3. **Pergunta Provável 3:** *"O Naive Bayes assume independência condicional. Isso é verdadeiro no dataset do grupo?"*  
   * **Resposta:** Não, pois observamos correlação de até 0,644 entre `alcohol` e `proline`. No entanto, o algoritmo classifica com 88,89% de acurácia no teste porque necessita apenas que a probabilidade da classe correta supere as demais para acertar o rótulo, mesmo com probabilidades absolutas distorcidas.
