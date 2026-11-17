# Desafio 1 — Árvore Binária de Busca (ABB)

Este módulo implementa o sistema de cadastro, consulta e percursos de produtos em uma **Árvore Binária de Busca (ABB)** para uma loja de informática.

## 📁 Estrutura dos Arquivos

- `produto.py`: Definição da classe `Produto` (código, nome, preço).
- `no.py`: Definição da classe `No` (nó com ponteiros para filhos esquerdo e direito).
- `arvore_binaria.py`: Implementação da estrutura de dados `ArvoreBinariaBusca` (inserção com rejeição de duplicatas, busca com rastreamento de nós visitados e percursos pré-ordem, em ordem e pós-ordem).
- `main.py`: Interface de menu interativo no terminal e rotina de demonstração automatizada dos requisitos.

## 🚀 Como Executar

### Modo Interativo (Menu com opções manuais e demonstração):
```bash
python main.py
```

### Modo Demonstração Rápida (Executa todos os requisitos de teste e análise):
```bash
python main.py --demo
```

## 🧪 Dados de Teste Padrão
Inserção na ordem exata:
1. `[50] Notebook (R$ 3.500,00)`
2. `[30] Mouse (R$ 80,00)`
3. `[70] Monitor (R$ 900,00)`
4. `[20] Teclado (R$ 150,00)`
5. `[40] Webcam (R$ 250,00)`
6. `[60] SSD (R$ 420,00)`
7. `[80] Impressora (R$ 1.200,00)`
