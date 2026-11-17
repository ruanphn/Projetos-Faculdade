"""
Programa Principal - Desafio 1: Árvore Binária de Busca (ABB)
Loja de Informática - Cadastro, Consulta e Percursos
"""
import sys
from produto import Produto
from arvore_binaria import ArvoreBinariaBusca

DADOS_TESTE_OFICIAIS = [
    (50, "Notebook", 3500.00),
    (30, "Mouse", 80.00),
    (70, "Monitor", 900.00),
    (20, "Teclado", 150.00),
    (40, "Webcam", 250.00),
    (60, "SSD", 420.00),
    (80, "Impressora", 1200.00),
]

def carregar_dados_iniciais(arvore: ArvoreBinariaBusca, exibir_logs: bool = True):
    """Insere os 7 registros da tabela de testes exatamente na ordem estipulada."""
    if exibir_logs:
        print("\n" + "="*65)
        print("  CARREGANDO DADOS OFICIAIS DE TESTE NA ABB")
        print("="*65)
    for codigo, nome, preco in DADOS_TESTE_OFICIAIS:
        prod = Produto(codigo, nome, preco)
        sucesso, msg = arvore.inserir(prod)
        if exibir_logs:
            print(f" -> {msg}")

def exibir_lista_produtos(titulo: str, lista_produtos):
    print("\n" + "-"*65)
    print(f"  {titulo} (Total: {len(lista_produtos)} produtos)")
    print("-" * 65)
    if not lista_produtos:
        print("  (Nenhum produto cadastrado)")
        return
    codigos = [str(p.codigo) for p in lista_produtos]
    print(f"  Sequência de Códigos: {' -> '.join(codigos)}")
    print("." * 65)
    for p in lista_produtos:
        print(f"  {p}")
    print("-" * 65)

def executar_demonstracao_completa(arvore: ArvoreBinariaBusca):
    """Executa todas as operações e requisitos de análise do enunciado em sequência."""
    print("\n" + "#"*70)
    print("      DEMONSTRAÇÃO COMPLETA DOS REQUISITOS DO DESAFIO 1")
    print("#"*70)
    
    # 1. Carga dos dados iniciais na ordem exata
    carregar_dados_iniciais(arvore, exibir_logs=True)
    
    # 2. Exibição da estrutura visual
    print("\n" + "="*65)
    print("  ESTRUTURA HIERÁRQUICA DA ÁRVORE APÓS AS INSERÇÕES:")
    print("="*65)
    print(arvore.obter_estrutura_visual())

    # 3. Teste de rejeição de duplicata
    print("\n" + "="*65)
    print("  TESTE DE REJEIÇÃO DE CÓDIGO DUPLICADO (CÓDIGO 30):")
    print("="*65)
    prod_duplicado = Produto(30, "Mouse Gamer", 120.00)
    sucesso, msg = arvore.inserir(prod_duplicado)
    print(f"  Resultado da tentativa: {msg}")

    # 4. Três percursos
    exibir_lista_produtos("PERCURSO PRÉ-ORDEM (Raiz -> Esquerda -> Direita)", arvore.percurso_pre_ordem())
    exibir_lista_produtos("PERCURSO EM ORDEM (Esquerda -> Raiz -> Direita - Crescente)", arvore.percurso_em_ordem())
    exibir_lista_produtos("PERCURSO PÓS-ORDEM (Esquerda -> Direita -> Raiz)", arvore.percurso_pos_ordem())

    # 5. Buscas requeridas
    print("\n" + "="*65)
    print("  TESTE DE BUSCA BEM-SUCEDIDA 1: Código 60 (Item da Análise)")
    print("="*65)
    prod, visitados, caminho = arvore.buscar(60)
    if prod:
        print(f"  [SUCESSO] Produto encontrado: {prod}")
        print(f"  Nós visitados ({visitados}): {' -> '.join(map(str, caminho))}")
    else:
        print("  [FALHA] Produto não encontrado.")

    print("\n" + "="*65)
    print("  TESTE DE BUSCA BEM-SUCEDIDA 2: Código 50 (Raiz)")
    print("="*65)
    prod, visitados, caminho = arvore.buscar(50)
    if prod:
        print(f"  [SUCESSO] Produto encontrado: {prod}")
        print(f"  Nós visitados ({visitados}): {' -> '.join(map(str, caminho))}")

    print("\n" + "="*65)
    print("  TESTE DE BUSCA POR CÓDIGO INEXISTENTE: Código 99")
    print("="*65)
    prod, visitados, caminho = arvore.buscar(99)
    if prod:
        print(f"  Produto encontrado: {prod}")
    else:
        print(f"  [ATENÇÃO] Produto com código 99 NÃO encontrado na árvore.")
        print(f"  Nós percorridos até folha nula ({visitados}): {' -> '.join(map(str, caminho))}")
    print("="*65 + "\n")

def menu_interativo():
    arvore = ArvoreBinariaBusca()
    
    while True:
        print("\n" + "="*50)
        print("     SISTEMA DE PRODUTOS - ÁRVORE BINÁRIA (ABB)")
        print("="*50)
        print("  1. Cadastrar produto")
        print("  2. Buscar produto por código")
        print("  3. Exibir produtos em Pré-ordem")
        print("  4. Exibir produtos Em ordem (crescente)")
        print("  5. Exibir produtos em Pós-ordem")
        print("  6. Visualizar desenho hierárquico da árvore")
        print("  7. Carregar dados de teste e executar demonstração")
        print("  0. Sair")
        print("="*50)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                codigo = int(input("Informe o código único (inteiro): ").strip())
                nome = input("Informe o nome do produto: ").strip()
                preco = float(input("Informe o preço (R$): ").strip().replace(",", "."))
                prod = Produto(codigo, nome, preco)
                sucesso, msg = arvore.inserir(prod)
                print(f"\n-> {msg}")
            except ValueError as ve:
                print(f"\n[Erro de entrada]: {ve}")

        elif opcao == "2":
            try:
                codigo = int(input("Informe o código a buscar: ").strip())
                prod, visitados, caminho = arvore.buscar(codigo)
                if prod:
                    print(f"\n[SUCESSO] Produto Encontrado:\n  {prod}")
                    print(f"  Quantidade de nós visitados: {visitados}")
                    print(f"  Caminho percorrido: {' -> '.join(map(str, caminho))}")
                else:
                    print(f"\n[NÃO ENCONTRADO] O produto com código {codigo} não existe na árvore.")
                    print(f"  Nós inspecionados antes de constatar ausência ({visitados}): {' -> '.join(map(str, caminho)) if caminho else 'Nenhum'}")
            except ValueError:
                print("\n[Erro]: O código deve ser um número inteiro.")

        elif opcao == "3":
            exibir_lista_produtos("PERCURSO PRÉ-ORDEM", arvore.percurso_pre_ordem())

        elif opcao == "4":
            exibir_lista_produtos("PERCURSO EM ORDEM", arvore.percurso_em_ordem())

        elif opcao == "5":
            exibir_lista_produtos("PERCURSO PÓS-ORDEM", arvore.percurso_pos_ordem())

        elif opcao == "6":
            print("\nESTRUTURA HIERÁRQUICA DA ÁRVORE:")
            print(arvore.obter_estrutura_visual())

        elif opcao == "7":
            executar_demonstracao_completa(arvore)

        elif opcao == "0":
            print("\nEncerrando sistema da ABB. Até logo!\n")
            break
        else:
            print("\nOpção inválida! Escolha um número entre 0 e 7.")

if __name__ == "__main__":
    if "--demo" in sys.argv or "--auto" in sys.argv:
        arvore = ArvoreBinariaBusca()
        executar_demonstracao_completa(arvore)
    else:
        menu_interativo()
