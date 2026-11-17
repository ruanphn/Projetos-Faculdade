"""
Script que executa os desafios e gera capturas visuais realistas do terminal
para inclusão no relatório técnico em PDF (evidências representativas de execução).
"""
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

def criar_imagem_terminal(titulo_janela: str, linhas_texto: list, caminho_saida: str, largura: int = 1000):
    # Fonte padrão ou truetype
    try:
        fonte = ImageFont.truetype("consola.ttf", 15)
        fonte_titulo = ImageFont.truetype("arialbd.ttf", 13)
    except IOError:
        try:
            fonte = ImageFont.truetype("DejaVuSansMono.ttf", 15)
            fonte_titulo = ImageFont.truetype("DejaVuSans-Bold.ttf", 13)
        except IOError:
            fonte = ImageFont.load_default()
            fonte_titulo = ImageFont.load_default()

    altura_linha = 20
    barra_topo = 35
    padding = 20
    altura_total = barra_topo + padding * 2 + len(linhas_texto) * altura_linha

    img = Image.new("RGB", (largura, altura_total), color="#1e1e1e")
    draw = ImageDraw.Draw(img)

    # Barra de título estilo Windows / Terminal Moderno
    draw.rectangle([0, 0, largura, barra_topo], fill="#2d2d2d")
    
    # Botões da janela (vermelho, amarelo, verde)
    raio = 5
    draw.ellipse([15 - raio, 18 - raio, 15 + raio, 18 + raio], fill="#ff5f56")
    draw.ellipse([32 - raio, 18 - raio, 32 + raio, 18 + raio], fill="#ffbd2e")
    draw.ellipse([49 - raio, 18 - raio, 49 + raio, 18 + raio], fill="#27c93f")

    # Título da janela centralizado
    draw.text((largura // 2 - 120, 10), titulo_janela, fill="#cccccc", font=fonte_titulo)

    # Linhas de texto
    y = barra_topo + padding
    for linha in linhas_texto:
        cor = "#d4d4d4" # padrão
        if "DEMONSTRAÇÃO" in linha or "INICIANDO" in linha or "EXPERIMENTO" in linha:
            cor = "#569cd6" # azul
        elif "SUCESSO" in linha or "inserido" in linha or "validados" in linha:
            cor = "#4ec9b0" # verde água
        elif "Erro" in linha or "rejeitada" in linha or "ATENÇÃO" in linha:
            cor = "#f44747" # vermelho
        elif "Cód:" in linha or "Nota:" in linha or "Bubble" in linha or "Merge" in linha:
            cor = "#ce9178" # laranja claro
        elif "=" in linha or "-" in linha:
            cor = "#6a9955" # verde comentário

        draw.text((padding, y), linha, fill=cor, font=fonte)
        y += altura_linha

    img.save(caminho_saida)
    print(f"[Terminal Screenshot] Imagem gerada: {caminho_saida}")

def capturar_execucoes():
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    dir_raiz = os.path.join(dir_atual, "..")
    dir_graficos = os.path.join(dir_atual, "graficos")
    os.makedirs(dir_graficos, exist_ok=True)

    # Executa Desafio 1
    proc1 = subprocess.run(
        ["python", "desafio1_arvore/main.py", "--demo"],
        cwd=dir_raiz,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    linhas1 = [linha for linha in proc1.stdout.splitlines() if linha.strip()]
    # Filtrar trechos mais expressivos
    linhas1_resumidas = [
        "PS C:\\Users\\RuanPereiraIGSA\\Downloads\\BARATA> python desafio1_arvore/main.py --demo",
        ""
    ] + linhas1[:45] # Primeiras 45 linhas expressivas
    
    criar_imagem_terminal(
        "PowerShell - Desafio 1 (Árvore Binária de Busca)",
        linhas1_resumidas,
        os.path.join(dir_graficos, "terminal_desafio1.png"),
        largura=950
    )

    # Executa Desafio 2
    proc2 = subprocess.run(
        ["python", "desafio2_ordenacao/main.py"],
        cwd=dir_raiz,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    linhas2 = [linha for linha in proc2.stdout.splitlines() if linha.strip()]
    linhas2_resumidas = [
        "PS C:\\Users\\RuanPereiraIGSA\\Downloads\\BARATA> python desafio2_ordenacao/main.py",
        ""
    ] + linhas2

    criar_imagem_terminal(
        "PowerShell - Desafio 2 (Comparativo Bubble Sort vs Merge Sort)",
        linhas2_resumidas,
        os.path.join(dir_graficos, "terminal_desafio2.png"),
        largura=950
    )

if __name__ == "__main__":
    capturar_execucoes()
