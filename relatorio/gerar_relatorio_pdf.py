"""
Script gerador do Relatório Técnico em PDF da Atividade Prática de Estruturas de Dados.
Estruturado em 5 páginas balanceadas:
- Página 1: Capa/Cabeçalho + Desafio 1 (Contexto, Diagrama da ABB e Questões 1 e 2)
- Página 2: Desafio 1 (Questões 3, 4 e 5 + Evidência do Terminal)
- Página 3: Desafio 2 (Contexto, Tabela Oficial, Gráficos Comparativos e Questões 1 e 2)
- Página 4: Desafio 2 (Questões 3, 4, 5 e 6 + Evidência do Terminal)
- Página 5: Conclusão Geral da Atividade, Considerações Finais e Instruções de Execução
"""
import os
import json
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Cabeçalho decorativo superior (páginas > 1)
        if self._pageNumber > 1:
            self.drawString(45, A4[1] - 32, "Atividade Prática — Árvores Binárias e Algoritmos de Ordenação")
            self.drawRightString(A4[0] - 45, A4[1] - 32, "Ruan Pereira do Nascimento")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.6)
            self.line(45, A4[1] - 38, A4[0] - 45, A4[1] - 38)

        # Rodapé inferior
        texto_rodape = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(A4[0] - 45, 30, texto_rodape)
        self.drawString(45, 30, "Estruturas de Dados • Python 3 • Análise e Desenvolvimento de Sistemas")
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.6)
        self.line(45, 42, A4[0] - 45, 42)
        self.restoreState()

def gerar_pdf():
    dir_relatorio = os.path.dirname(os.path.abspath(__file__))
    caminho_pdf = os.path.join(dir_relatorio, "Relatorio_Estruturas_Dados.pdf")
    caminho_json = os.path.join(dir_relatorio, "..", "desafio2_ordenacao", "resultados_experimento.json")

    with open(caminho_json, "r", encoding="utf-8") as f:
        resultados = json.load(f)

    doc = SimpleDocTemplate(
        caminho_pdf,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=48,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor("#1A365D")   # Azul Marinho
    secondary_color = colors.HexColor("#0D9488") # Teal / Esmeralda
    dark_text = colors.HexColor("#2D3748")       # Cinza Chumbo

    estilo_titulo = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=primary_color,
        alignment=1,
        spaceAfter=4
    )

    estilo_subtitulo = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11.5,
        leading=14.5,
        textColor=secondary_color,
        alignment=1,
        spaceAfter=8
    )

    estilo_autor = ParagraphStyle(
        'DocAuthor',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=dark_text,
        alignment=1,
        spaceAfter=10
    )

    estilo_h1 = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=primary_color,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    estilo_h2 = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13.5,
        textColor=secondary_color,
        spaceBefore=6,
        spaceAfter=3,
        keepWithNext=True
    )

    estilo_pergunta = ParagraphStyle(
        'QuestionStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=primary_color,
        spaceBefore=5,
        spaceAfter=2,
        keepWithNext=True
    )

    estilo_resposta = ParagraphStyle(
        'AnswerStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.8,
        textColor=dark_text,
        spaceAfter=4
    )

    elementos = []

    # =========================================================================
    # PÁGINA 1 — CAPA / DESAFIO 1 (Contexto, Topologia e Q1-Q2)
    # =========================================================================
    elementos.append(Paragraph("ATIVIDADE PRÁTICA — ESTRUTURAS DE DADOS", estilo_titulo))
    elementos.append(Paragraph("Árvores Binárias de Busca e Algoritmos de Ordenação", estilo_subtitulo))
    elementos.append(Paragraph(
        "<b>Estudante:</b> Ruan Pereira do Nascimento &nbsp;|&nbsp; <b>Curso:</b> Análise e Desenvolvimento de Sistemas<br/>"
        "<b>Linguagem:</b> Python 3 &nbsp;|&nbsp; <b>Modalidade:</b> Individual / Dupla (Pontuação: 3,0 pontos)",
        estilo_autor
    ))
    elementos.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceAfter=8))

    elementos.append(Paragraph("1. DESAFIO 1 — Árvore Binária de Busca (ABB)", estilo_h1))
    elementos.append(Paragraph(
        "O Desafio 1 demandou o desenvolvimento do sistema de gerenciamento de produtos de uma loja de informática organizado em uma "
        "<b>Árvore Binária de Busca (ABB)</b> orientada pelo código do produto. A implementação foi rigorosamente modularizada em classes "
        "independentes (<code>Produto</code>, <code>No</code> e <code>ArvoreBinariaBusca</code>), respeitando a ordenação por chave, "
        "a rejeição explícita de duplicatas, percursos Pré-ordem, Em ordem e Pós-ordem e busca com instrumentalização.",
        estilo_resposta
    ))

    caminho_graf_arvore = os.path.join(dir_relatorio, "graficos", "grafico_arvore.png")
    if os.path.exists(caminho_graf_arvore):
        elementos.append(Image(caminho_graf_arvore, width=6.9*inch, height=2.9*inch))
        elementos.append(Spacer(1, 4))

    elementos.append(Paragraph("Questões de Análise Técnica (Parte 1)", estilo_h2))

    elementos.append(Paragraph("Q1: Qual produto ocupa a raiz da árvore?", estilo_pergunta))
    elementos.append(Paragraph(
        "<b>Resposta:</b> O produto que ocupa a raiz é o <b>Notebook (Código: 50, Preço: R$ 3.500,00)</b>. "
        "Em uma ABB, a raiz corresponde obrigatoriamente ao primeiro registro inserido na árvore vazia. "
        "Como a inserção seguiu rigorosamente a ordem da tabela do enunciado, o código 50 tornou-se o elemento pivô inicial para todas as subsequentes inserções e buscas.",
        estilo_resposta
    ))

    elementos.append(Paragraph("Q2: Qual sequência de códigos é apresentada no percurso em ordem?", estilo_pergunta))
    elementos.append(Paragraph(
        "<b>Resposta:</b> A sequência obtida é exatamente: <b>20 &rarr; 30 &rarr; 40 &rarr; 50 &rarr; 60 &rarr; 70 &rarr; 80</b>.<br/>"
        "<i>Fundamentação:</i> A propriedade invariante da ABB estipula que nós à esquerda possuem chaves menores que o nó atual e nós à direita possuem chaves maiores. "
        "Como o percurso em ordem visita recursivamente na ordem <i>(Esquerda &rarr; Raiz &rarr; Direita)</i>, a travessia resulta invariavelmente nas chaves ordenadas de forma estritamente crescente.",
        estilo_resposta
    ))

    elementos.append(PageBreak())

    # =========================================================================
    # PÁGINA 2 — DESAFIO 1 (Q3, Q4, Q5 + Evidência de Terminal)
    # =========================================================================
    elementos.append(Paragraph("Questões de Análise Técnica (Parte 2 — Continuação)", estilo_h2))

    elementos.append(Paragraph("Q3: Explique a diferença entre pré-ordem, em ordem e pós-ordem.", estilo_pergunta))
    elementos.append(Paragraph(
        "<b>Resposta:</b> A diferença reside no momento em que o nó raiz de cada subárvore é visitado em relação aos seus filhos:<br/>"
        "• <b>Pré-ordem (Raiz &rarr; Esquerda &rarr; Direita):</b> Processa o nó antes de seus descendentes. É ideal para clonagem e serialização, pois recria a topologia exata original (Sequência: <code>50 &rarr; 30 &rarr; 20 &rarr; 40 &rarr; 70 &rarr; 60 &rarr; 80</code>).<br/>"
        "• <b>Em ordem (Esquerda &rarr; Raiz &rarr; Direita):</b> Processa toda a subárvore esquerda, depois a raiz e em seguida a direita. Em uma ABB, gera os dados perfeitamente ordenados (Sequência: <code>20 &rarr; 30 &rarr; 40 &rarr; 50 &rarr; 60 &rarr; 70 &rarr; 80</code>).<br/>"
        "• <b>Pós-ordem (Esquerda &rarr; Direita &rarr; Raiz):</b> Processa ambos os ramos antes de visitar o nó pai. É o padrão clássico para liberação de memória e cálculo cumulativo de diretórios (Sequência: <code>20 &rarr; 40 &rarr; 30 &rarr; 60 &rarr; 80 &rarr; 70 &rarr; 50</code>).",
        estilo_resposta
    ))

    elementos.append(Paragraph("Q4: Quantos nós são visitados na busca pelo código 60, incluindo o nó encontrado?", estilo_pergunta))
    elementos.append(Paragraph(
        "<b>Resposta:</b> São visitados exatamente <b>3 nós</b> (Caminho percorrido: <b>50 &rarr; 70 &rarr; 60</b>):<br/>"
        "&nbsp;&nbsp;1. <b>Nó 50 (Raiz):</b> Como $60 > 50$, o algoritmo descende para a subárvore direita.<br/>"
        "&nbsp;&nbsp;2. <b>Nó 70:</b> Como $60 < 70$, o algoritmo descende para a subárvore esquerda.<br/>"
        "&nbsp;&nbsp;3. <b>Nó 60:</b> Como $60 == 60$, a chave coincide e o registro do SSD é retornado com sucesso.",
        estilo_resposta
    ))

    elementos.append(Paragraph("Q5: O que pode acontecer com a forma da ABB e com o desempenho das buscas quando os códigos são inseridos em ordem crescente?", estilo_pergunta))
    elementos.append(Paragraph(
        "<b>Resposta:</b> Quando as chaves são inseridas de forma previamente ordenada (crescente), cada novo elemento inserido será sempre maior que o anterior, sendo posicionado como filho direito. "
        "A árvore sofre <b>degeneração estrutural em lista encadeada</b> com altura $h = n$. "
        "Consequentemente, as operações de busca, inserção e remoção perdem a eficiência logarítmica média de $O(\\log n)$ e degradam para o pior caso linear <b>$O(n)$</b>.",
        estilo_resposta
    ))

    caminho_term1 = os.path.join(dir_relatorio, "graficos", "terminal_desafio1.png")
    if os.path.exists(caminho_term1):
        elementos.append(Spacer(1, 4))
        elementos.append(Paragraph("<b>Evidência Visual de Execução — Desafio 1 (Árvore Binária de Busca)</b>", estilo_h2))
        elementos.append(Image(caminho_term1, width=6.9*inch, height=3.7*inch))

    elementos.append(PageBreak())

    # =========================================================================
    # PÁGINA 3 — DESAFIO 2 (Contexto, Tabela, Gráficos e Q1-Q2)
    # =========================================================================
    elementos.append(Paragraph("2. DESAFIO 2 — Comparação de Algoritmos de Ordenação", estilo_h1))
    elementos.append(Paragraph(
        "Neste experimento comparativo, foram avaliados o <b>Bubble Sort</b> (quadrático) e o <b>Merge Sort</b> (divisão e conquista) "
        "aplicados a conjuntos com 100, 1.000 e 5.000 objetos <code>Aluno</code> ordenados pela nota acadêmica (0,00 a 10,00). "
        "A instrumentação mediu a mediana do tempo de 3 repetições (com <code>time.perf_counter()</code>) e contabilizou "
        "estritamente as comparações reais entre as notas dos estudantes, utilizando semente pseudoaleatória fixa (<code>seed = 42</code>).",
        estilo_resposta
    ))

    elementos.append(Paragraph("Tabela Oficial de Resultados Experimentais", estilo_h2))
    
    tabela_dados = [
        ["Registros", "Algoritmo", "Tempo mediano (ms)", "Comparações de Notas"]
    ]
    for r in resultados:
        tamanho_fmt = f"{r['tamanho']:,}".replace(",", ".")
        comps_fmt = f"{r['comparacoes']:,}".replace(",", ".")
        tempo_fmt = f"{r['tempo_mediano_ms']:,.3f} ms".replace(",", "X").replace(".", ",").replace("X", ".")
        tabela_dados.append([tamanho_fmt, r['algoritmo'], tempo_fmt, comps_fmt])

    t = Table(tabela_dados, colWidths=[2.2*cm, 3.8*cm, 4.3*cm, 4.8*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('BOTTOMPADDING', (0,0), (-1,0), 4),
        ('TOPPADDING', (0,0), (-1,0), 4),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#F8FAFC")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#EDF2F7")]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 8.5),
        ('BOTTOMPADDING', (0,1), (-1,-1), 3.5),
        ('TOPPADDING', (0,1), (-1,-1), 3.5),
    ]))
    elementos.append(t)
    elementos.append(Spacer(1, 4))

    caminho_graf_tempo = os.path.join(dir_relatorio, "graficos", "grafico_tempo.png")
    caminho_graf_comp = os.path.join(dir_relatorio, "graficos", "grafico_comparacoes.png")
    if os.path.exists(caminho_graf_tempo) and os.path.exists(caminho_graf_comp):
        tabela_graficos = Table([
            [Image(caminho_graf_tempo, width=3.4*inch, height=2.0*inch),
             Image(caminho_graf_comp, width=3.4*inch, height=2.0*inch)]
        ], colWidths=[3.5*inch, 3.5*inch])
        tabela_graficos.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
        ]))
        elementos.append(tabela_graficos)
        elementos.append(Spacer(1, 4))

    elementos.append(Paragraph("Questões de Análise Técnica (Parte 1)", estilo_h2))

    elementos.append(Paragraph("Q1: Qual algoritmo apresentou menor tempo de execução em cada tamanho de entrada?", estilo_pergunta))
    elementos.append(Paragraph(
        "<b>Resposta:</b> O <b>Merge Sort</b> apresentou menor tempo de execução absoluto em todos os cenários. "
        "Para 100 registros, foi <b>3,5&times; mais rápido</b> (0,177 ms vs 0,619 ms); para 1.000 registros, foi <b>36&times; mais rápido</b> (2,294 ms vs 82,607 ms); "
        "e para 5.000 registros, o Merge Sort foi <b>171&times; mais rápido</b> (12,620 ms contra 2.158,379 ms do Bubble Sort).",
        estilo_resposta
    ))

    elementos.append(Paragraph("Q2: Como o crescimento de 100 para 5.000 registros afetou o tempo e o número de comparações?", estilo_pergunta))
    elementos.append(Paragraph(
        "<b>Resposta:</b> A entrada aumentou por um fator de 50&times; (de 100 para 5.000 registros):<br/>"
        "• <b>Bubble Sort:</b> As comparações cresceram de 4.884 para 12.493.314 (salto de <b>2.558&times;</b>, alinhado ao fator quadrático $50^2 = 2.500$). O tempo saltou de 0,619 ms para 2.158,379 ms (crescimento de <b>3.486&times;</b>).<br/>"
        "• <b>Merge Sort:</b> As comparações variaram de 539 para 55.198 (crescimento de apenas <b>102&times;</b>). O tempo cresceu de 0,177 ms para 12,620 ms (apenas <b>71&times;</b>). A disparidade evidencia o contraste assintótico entre $O(n^2)$ e $O(n \\log n)$.",
        estilo_resposta
    ))

    elementos.append(PageBreak())

    # =========================================================================
    # PÁGINA 4 — DESAFIO 2 (Q3-Q6 + Evidência de Terminal)
    # =========================================================================
    elementos.append(Paragraph("Questões de Análise Técnica (Parte 2 — Continuação)", estilo_h2))

    elementos.append(Paragraph("Q3: Qual algoritmo efetuou menos comparações? Os resultados foram consistentes?", estilo_pergunta))
    elementos.append(Paragraph(
        "<b>Resposta:</b> O <b>Merge Sort</b> efetuou drasticamente menos comparações em todos os casos. Para 5.000 itens, foram necessárias apenas <b>55.198 comparações</b> contra <b>12.493.314 do Bubble Sort</b> (redução de 99,56% das comparações). "
        "Os resultados foram 100% determinísticos e consistentes entre as repetições devido ao isolamento das cópias dos dados.",
        estilo_resposta
    ))

    elementos.append(Paragraph("Q4: Como a estratégia de divisão e conquista do Merge Sort influencia seu desempenho?", estilo_pergunta))
    elementos.append(Paragraph(
        "<b>Resposta:</b> A divisão recursiva pela metade cria uma árvore de recursão com altura $\\lceil \\log_2 n \\rceil$. "
        "Na fase de intercalação (merge), a mesclagem de listas ordenadas ocorre em tempo estritamente linear $O(n)$ por nível. "
        "Dessa forma, a complexidade total mantém-se estritamente delimitada em $O(n \\log n)$ em todos os casos (melhor, médio e pior), eliminando comparações redundantes.",
        estilo_resposta
    ))

    elementos.append(Paragraph("Q5: Considerando as complexidades de tempo, qual algoritmo seria mais apropriado para 100.000 registros? Justifique.", estilo_pergunta))
    elementos.append(Paragraph(
        "<b>Resposta:</b> O <b>Merge Sort</b> é a única opção aceitável em engenharia de software.<br/>"
        "<i>Justificativa Analítica:</i> Para $N = 100.000$, o Bubble Sort exigiria aproximadamente $n^2/2 \\approx 5 \\times 10^9$ comparações (5 bilhões de operações), "
        "levando estimadamente <b>entre 15 a 20 minutos</b> de processamento contínuo. "
        "Em contrapartida, o Merge Sort exigiria aproximadamente $n \\log_2 n \\approx 100.000 \\times 16,6 \\approx 1,66 \\times 10^6$ comparações (apenas 1,66 milhão), "
        "completando a ordenação em <b>menos de 0,3 segundo</b>.",
        estilo_resposta
    ))

    elementos.append(Paragraph("Q6: Como o uso de memória auxiliar pelo Merge Sort pode influenciar a escolha de um algoritmo?", estilo_pergunta))
    elementos.append(Paragraph(
        "<b>Resposta:</b> O Merge Sort clássico requer memória auxiliar $O(n)$ para manter os vetores temporários durante a intercalação. "
        "Em cenários de <i>hardware</i> severamente restrito (microcontroladores, sensores IoT) ou quando os dados superam a RAM física, "
        "o consumo de memória pode provocar falhas de alocação. Nesses nichos específicos, algoritmos <i>in-place</i> como QuickSort ou HeapSort são preferíveis. "
        "Contudo, em servidores corporativos convencionais, o custo de $O(n)$ de RAM é amplamente compensado pelo ganho de velocidade e estabilidade.",
        estilo_resposta
    ))

    caminho_term2 = os.path.join(dir_relatorio, "graficos", "terminal_desafio2.png")
    if os.path.exists(caminho_term2):
        elementos.append(Spacer(1, 4))
        elementos.append(Paragraph("<b>Evidência Visual de Execução — Desafio 2 (Comparativo de Algoritmos)</b>", estilo_h2))
        elementos.append(Image(caminho_term2, width=6.9*inch, height=3.6*inch))

    elementos.append(PageBreak())

    # =========================================================================
    # PÁGINA 5 — CONCLUSÃO GERAL E INSTRUÇÕES
    # =========================================================================
    elementos.append(Paragraph("3. Conclusão Geral e Considerações Finais", estilo_h1))
    elementos.append(Paragraph(
        "A presente atividade prática consolidou de forma empírica e analítica a relevância crucial das estruturas de dados e do cálculo "
        "de complexidade assintótica no projeto de sistemas computacionais de alto desempenho.<br/><br/>"
        "• <b>Desafio 1 (Árvore Binária de Busca):</b> Comprovou a eficácia da organização hierárquica para consultas rápidas com tempo médio $O(\\log n)$ "
        "ao permitir a localização do produto SSD (cód. 60) com apenas 3 comparações. Evidenciou também a vulnerabilidade da ABB à inserção de dados "
        "previamente ordenados, fenômeno que justifica a utilização de estruturas auto-balanceáveis (como árvores AVL e Rubro-Negras) em ambientes de produção.<br/><br/>"
        "• <b>Desafio 2 (Algoritmos de Ordenação):</b> Revelou experimentalmente o abismo de eficiência entre algoritmos quadráticos $O(n^2)$ e linearítmicos $O(n \\log n)$. "
        "A redução de 99,56% no número de comparações e o ganho de 171&times; em velocidade de execução no conjunto de 5.000 alunos ratificam por que o Merge Sort "
        "e algoritmos derivados por divisão e conquista (como Timsort) são adotados como padrão pelas linguagens de programação modernas.",
        estilo_resposta
    ))
    elementos.append(Spacer(1, 10))

    elementos.append(Paragraph("4. Resumo Sintético das Contribuições", estilo_h1))
    
    tabela_sintese = [
        ["Critério Avaliado", "Desafio 1 (Árvore ABB)", "Desafio 2 (Ordenação)"],
        ["Estruturas Centrais", "Classes Produto, No e ArvoreBinariaBusca", "Classe Aluno, Bubble Sort e Merge Sort"],
        ["Princípio Teórico", "Estrutura Hierárquica e Busca Binária", "Divisão e Conquista vs Força Bruta Quadrática"],
        ["Complexidade Melhor/Média", "O(log n) para buscas e inserções", "Merge Sort: O(n log n) | Bubble: O(n²)"],
        ["Pior Caso Identificado", "O(n) com dados pré-ordenados (árvore degenerada)", "Bubble Sort com 12,49 milhões de comparações"],
        ["Validações Executadas", "Rejeição de duplicatas, 3 percursos e buscas", "3 repetições, mediana de tempo e checagem de ordenação"]
    ]
    t_sintese = Table(tabela_sintese, colWidths=[3.8*cm, 5.6*cm, 5.6*cm])
    t_sintese.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('BOTTOMPADDING', (0,0), (-1,0), 4),
        ('TOPPADDING', (0,0), (-1,0), 4),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#F8FAFC")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#EDF2F7")]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 8),
        ('BOTTOMPADDING', (0,1), (-1,-1), 3),
        ('TOPPADDING', (0,1), (-1,-1), 3),
    ]))
    elementos.append(t_sintese)
    elementos.append(Spacer(1, 10))

    elementos.append(Paragraph("5. Instruções Sucintas de Execução", estilo_h1))
    elementos.append(Paragraph(
        "Os códigos-fonte foram organizados de forma independente e podem ser reproduzidos com os comandos abaixo:<br/>"
        "• <b>Desafio 1 (Modo Interativo com Menu):</b> <code>python desafio1_arvore/main.py</code><br/>"
        "• <b>Desafio 1 (Modo Demonstração Rápida):</b> <code>python desafio1_arvore/main.py --demo</code><br/>"
        "• <b>Desafio 2 (Experimento de Ordenação):</b> <code>python desafio2_ordenacao/main.py</code><br/>"
        "• <b>Regeneração Automática deste Relatório PDF:</b> <code>python relatorio/gerar_relatorio_pdf.py</code>",
        estilo_resposta
    ))

    doc.build(elementos, canvasmaker=NumberedCanvas)
    print(f"[PDF] Relatório equilibrado de 5 páginas gerado com sucesso: {caminho_pdf}")

if __name__ == "__main__":
    gerar_pdf()
