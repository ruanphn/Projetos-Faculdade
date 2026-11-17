"""
Módulo de implementação da Árvore Binária de Busca (ABB) para gestão de produtos.
"""
from typing import Optional, List, Tuple
from produto import Produto
from no import No

class ArvoreBinariaBusca:
    """
    Implementação da Árvore Binária de Busca (ABB) orientada pelo código do produto.
    
    Regras da ABB:
    - O código do produto funciona como a chave de ordenação.
    - Nós à esquerda possuem chave estritamente menor que o nó pai.
    - Nós à direita possuem chave estritamente maior que o nó pai.
    - Chaves duplicadas são rejeitadas.
    """
    def __init__(self):
        self.raiz: Optional[No] = None
        self._total_nos: int = 0

    @property
    def total_nos(self) -> int:
        return self._total_nos

    def esta_vazia(self) -> bool:
        return self.raiz is None

    # -------------------------------------------------------------------------
    # Inserção na ABB
    # -------------------------------------------------------------------------
    def inserir(self, produto: Produto) -> Tuple[bool, str]:
        """
        Insere um novo produto na árvore.
        
        Retorna:
            Tuple[bool, str]: (Sucesso, Mensagem explicativa)
        """
        if not isinstance(produto, Produto):
            raise TypeError("O elemento a ser inserido deve ser uma instância de Produto.")

        if self.raiz is None:
            self.raiz = No(produto)
            self._total_nos += 1
            return True, f"Produto '{produto.nome}' (Cód: {produto.codigo}) inserido como raiz da árvore."

        return self._inserir_recursivo(self.raiz, produto)

    def _inserir_recursivo(self, no_atual: No, produto: Produto) -> Tuple[bool, str]:
        if produto.codigo == no_atual.produto.codigo:
            # Rejeita códigos duplicados conforme especificação
            return False, f"Erro: Código {produto.codigo} já existe na árvore (Produto: '{no_atual.produto.nome}'). Inserção rejeitada."

        if produto.codigo < no_atual.produto.codigo:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(produto)
                self._total_nos += 1
                return True, f"Produto '{produto.nome}' (Cód: {produto.codigo}) inserido à esquerda de '{no_atual.produto.nome}' (Cód: {no_atual.produto.codigo})."
            return self._inserir_recursivo(no_atual.esquerda, produto)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(produto)
                self._total_nos += 1
                return True, f"Produto '{produto.nome}' (Cód: {produto.codigo}) inserido à direita de '{no_atual.produto.nome}' (Cód: {no_atual.produto.codigo})."
            return self._inserir_recursivo(no_atual.direita, produto)

    # -------------------------------------------------------------------------
    # Busca por Código
    # -------------------------------------------------------------------------
    def buscar(self, codigo: int) -> Tuple[Optional[Produto], int, List[int]]:
        """
        Busca um produto na árvore pelo código.
        
        Retorna:
            Tuple[Optional[Produto], int, List[int]]:
                - Produto encontrado (ou None se não existir)
                - Quantidade total de nós visitados
                - Lista com a sequência de códigos dos nós visitados
        """
        caminho: List[int] = []
        no_encontrado = self._buscar_recursivo(self.raiz, codigo, caminho)
        produto = no_encontrado.produto if no_encontrado else None
        return produto, len(caminho), caminho

    def _buscar_recursivo(self, no_atual: Optional[No], codigo: int, caminho: List[int]) -> Optional[No]:
        if no_atual is None:
            return None

        caminho.append(no_atual.produto.codigo)

        if codigo == no_atual.produto.codigo:
            return no_atual
        elif codigo < no_atual.produto.codigo:
            return self._buscar_recursivo(no_atual.esquerda, codigo, caminho)
        else:
            return self._buscar_recursivo(no_atual.direita, codigo, caminho)

    # -------------------------------------------------------------------------
    # Percursos da Árvore
    # -------------------------------------------------------------------------
    def percurso_pre_ordem(self) -> List[Produto]:
        """
        Percurso Pré-ordem (Raiz -> Esquerda -> Direita).
        """
        resultado: List[Produto] = []
        self._pre_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _pre_ordem_recursivo(self, no_atual: Optional[No], resultado: List[Produto]):
        if no_atual is not None:
            resultado.append(no_atual.produto)
            self._pre_ordem_recursivo(no_atual.esquerda, resultado)
            self._pre_ordem_recursivo(no_atual.direita, resultado)

    def percurso_em_ordem(self) -> List[Produto]:
        """
        Percurso Em Ordem (Esquerda -> Raiz -> Direita).
        Gera os elementos em ordem crescente de chave em uma ABB.
        """
        resultado: List[Produto] = []
        self._em_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _em_ordem_recursivo(self, no_atual: Optional[No], resultado: List[Produto]):
        if no_atual is not None:
            self._em_ordem_recursivo(no_atual.esquerda, resultado)
            resultado.append(no_atual.produto)
            self._em_ordem_recursivo(no_atual.direita, resultado)

    def percurso_pos_ordem(self) -> List[Produto]:
        """
        Percurso Pós-ordem (Esquerda -> Direita -> Raiz).
        """
        resultado: List[Produto] = []
        self._pos_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _pos_ordem_recursivo(self, no_atual: Optional[No], resultado: List[Produto]):
        if no_atual is not None:
            self._pos_ordem_recursivo(no_atual.esquerda, resultado)
            self._pos_ordem_recursivo(no_atual.direita, resultado)
            resultado.append(no_atual.produto)

    # -------------------------------------------------------------------------
    # Representação Visual ASCII
    # -------------------------------------------------------------------------
    def obter_estrutura_visual(self) -> str:
        """
        Gera uma representação textual e hierárquica da árvore binária.
        """
        if self.raiz is None:
            return "(Árvore vazia)"
        
        linhas: List[str] = []
        self._montar_visual(self.raiz, "", True, linhas)
        return "\n".join(linhas)

    def _montar_visual(self, no: Optional[No], prefixo: str, eh_ultimo: bool, linhas: List[str]):
        if no is not None:
            conector = "└── " if eh_ultimo else "├── "
            linhas.append(f"{prefixo}{conector}[{no.produto.codigo}] {no.produto.nome} (R$ {no.produto.preco:.2f})")
            
            novos_filhos = []
            if no.esquerda or no.direita:
                novos_filhos.append((no.esquerda, "ESQ: "))
                novos_filhos.append((no.direita, "DIR: "))

            novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
            for idx, (filho, lado) in enumerate(novos_filhos):
                ultimo_filho = (idx == len(novos_filhos) - 1)
                if filho is not None:
                    self._montar_visual(filho, novo_prefixo, ultimo_filho, linhas)
                else:
                    conector_vazio = "└── " if ultimo_filho else "├── "
                    linhas.append(f"{novo_prefixo}{conector_vazio}({lado.strip()} vazio)")
