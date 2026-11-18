import sys
from produto import Produto
from arvore_binaria import ArvoreBinariaBusca

DADOS_TESTE = [
    (50, "Notebook", 3500.00),
    (30, "Mouse", 80.00),
    (70, "Monitor", 900.00),
    (20, "Teclado", 150.00),
    (40, "Webcam", 250.00),
    (60, "SSD", 420.00),
    (80, "Impressora", 1200.00),
]

def carregar_dados_iniciais(arvore: ArvoreBinariaBusca, verbose: bool = True):
    for codigo, nome, preco in DADOS_TESTE:
        prod = Produto(codigo, nome, preco)
        sucesso, msg = arvore.inserir(prod)
        if verbose:
            print(f" -> {msg}")

def exibir_produtos(titulo: str, lista_produtos):
    print(f"\n{titulo} ({len(lista_produtos)} produtos):")
    if not lista_produtos:
        print("  (Árvore vazia)")
        return
    codigos = [str(p.codigo) for p in lista_produtos]
    print(f"  Códigos: {' -> '.join(codigos)}")
    for p in lista_produtos:
        print(f"  {p}")

def executar_demonstracao(arvore: ArvoreBinariaBusca):
    print("\n--- INSERÇÃO DOS DADOS DE TESTE ---")
    carregar_dados_iniciais(arvore, verbose=True)

    print("\n--- ESTRUTURA HIERÁRQUICA DA ÁRVORE ---")
    print(arvore.obter_estrutura_visual())

    print("\n--- TESTE DE CHAVE DUPLICADA (CÓDIGO 30) ---")
    sucesso, msg = arvore.inserir(Produto(30, "Mouse Gamer", 120.00))
    print(f"  Resultado: {msg}")

    exibir_produtos("PERCURSO PRÉ-ORDEM", arvore.percurso_pre_ordem())
    exibir_produtos("PERCURSO EM ORDEM", arvore.percurso_em_ordem())
    exibir_produtos("PERCURSO PÓS-ORDEM", arvore.percurso_pos_ordem())

    print("\n--- TESTES DE BUSCA ---")
    for cod in [60, 50, 99]:
        prod, visitados, caminho = arvore.buscar(cod)
        if prod:
            print(f"  Busca por {cod}: Encontrado ({prod}) | Nós visitados ({visitados}): {' -> '.join(map(str, caminho))}")
        else:
            print(f"  Busca por {cod}: Não encontrado | Nós visitados ({visitados}): {' -> '.join(map(str, caminho)) if caminho else 'Nenhum'}")

def menu_interativo():
    arvore = ArvoreBinariaBusca()

    while True:
        print("\n=== ÁRVORE BINÁRIA DE BUSCA (PRODUTOS) ===")
        print("1. Cadastrar produto")
        print("2. Buscar produto por código")
        print("3. Percurso Pré-ordem")
        print("4. Percurso Em ordem")
        print("5. Percurso Pós-ordem")
        print("6. Visualizar árvore")
        print("7. Carregar dados de teste e demonstrar")
        print("0. Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            try:
                codigo = int(input("Código: ").strip())
                nome = input("Nome: ").strip()
                preco = float(input("Preço (R$): ").strip().replace(",", "."))
                sucesso, msg = arvore.inserir(Produto(codigo, nome, preco))
                print(f"-> {msg}")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            try:
                codigo = int(input("Código para busca: ").strip())
                prod, visitados, caminho = arvore.buscar(codigo)
                if prod:
                    print(f"Encontrado: {prod}")
                    print(f"Nós visitados ({visitados}): {' -> '.join(map(str, caminho))}")
                else:
                    print(f"Produto {codigo} não encontrado. Nós visitados: {visitados}")
            except ValueError:
                print("Erro: O código deve ser numérico.")

        elif opcao == "3":
            exibir_produtos("PERCURSO PRÉ-ORDEM", arvore.percurso_pre_ordem())

        elif opcao == "4":
            exibir_produtos("PERCURSO EM ORDEM", arvore.percurso_em_ordem())

        elif opcao == "5":
            exibir_produtos("PERCURSO PÓS-ORDEM", arvore.percurso_pos_ordem())

        elif opcao == "6":
            print(arvore.obter_estrutura_visual())

        elif opcao == "7":
            executar_demonstracao(arvore)

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    if "--demo" in sys.argv:
        arvore = ArvoreBinariaBusca()
        executar_demonstracao(arvore)
    else:
        menu_interativo()
