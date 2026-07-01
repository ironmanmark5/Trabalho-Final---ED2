# Projeto – Árvore Binária de Busca (BST)

**Disciplina:** GCT153 – Estruturas de Dados II  
**Professor:** Prof. Dr. Alysson Naves  
**Data de entrega:** 30/06/2026

---

## Descrição do Projeto

Implementação manual de uma **Árvore Binária de Busca (BST)** em Python, sem o uso de bibliotecas prontas.

O projeto contempla:

- Inserção de elementos;
- Busca de valores;
- Remoção de nós;
- Percursos em pré-ordem, em-ordem e pós-ordem;
- Cálculo da altura da árvore;
- Contagem de nós e folhas;
- Análise do impacto da altura no desempenho;
- Testes utilizando diferentes sequências de entrada.

---

## Estrutura do Projeto

```text
Trabalho Final - ED2/
├── no.py                          # Classe Nó
├── arvoreBinaria.py               # Classe ArvoreBinaria (BST)
├── main.py                        # Script principal de testes
├── questoes.txt                   # Respostas das questões conceituais
├── execucoes_trabalho_final.txt   # Saída completa dos testes
└── README.md                      # Este arquivo
```

---

## Como Executar

### Pré-requisitos

- Python 3.6 ou superior.

### Passos

1. Coloque todos os arquivos na mesma pasta.
2. Abra um terminal dentro dessa pasta.
3. Execute:

```bash
python main.py
```

Todos os sete casos de teste serão executados automaticamente e seus resultados serão exibidos no terminal.

---

## Casos de Teste

| Teste | Descrição | Resultado Esperado | 
|:------:|-----------|:-------------------:|
| 1 | Inserção básica | Em-ordem: 2, 5, 7, 10, 12, 15, 20; Altura = 2; Nós = 7; Folhas = 4
| 2 | Busca | 7 e 12 encontrados; 99 e 1 não encontrados
| 3 | Menor e maior | Menor = 2; Maior = 20
| 4 | Remoção de folha (2) | Em-ordem: 5, 7, 10, 12, 15, 20
| 5 | Remoção com um filho (7) | Em-ordem: 2, 5, 6, 10, 15 
| 6 | Remoção com dois filhos (10) | Em-ordem: 2, 5, 7, 12, 15, 20 
| 7 | Árvore degenerada (1..5) | Altura = 4; Nós = 5; Folhas = 1 

A saída completa está disponível no arquivo **execucoes_trabalho_final.txt**.

---

## Questões Conceituais

As respostas completas encontram-se em **questoes.txt**.

### Resumo

### Por que o percurso em-ordem gera valores crescentes?

Porque visita primeiro a subárvore esquerda, depois o nó atual e, por fim, a subárvore direita. Em uma BST, essa ordem produz os elementos em ordem crescente.

### Qual a diferença entre uma árvore binária comum e uma BST?

Uma árvore binária comum não possui regra de ordenação entre seus nós. Já uma BST mantém os valores menores na subárvore esquerda e os maiores na subárvore direita.

### Por que a altura influencia o desempenho?

A altura determina o número máximo de comparações necessárias para localizar, inserir ou remover um elemento.

### O que acontece quando os valores são inseridos em ordem crescente?

A árvore torna-se degenerada, assumindo formato semelhante ao de uma lista encadeada, fazendo com que as operações passem a ter custo **O(n)**.

### Qual é o custo médio em uma BST balanceada?

As principais operações possuem complexidade **O(log n)**.

### Qual é o pior caso?

Quando a árvore está degenerada, as operações passam a ter complexidade **O(n)**.

### Casos de remoção

- **Nó folha:** removido diretamente.
- **Nó com um filho:** o filho assume a posição do nó removido.
- **Nó com dois filhos:** o nó é substituído pelo sucessor em-ordem (menor elemento da subárvore direita), que é removido posteriormente.

---

## Dependências

Nenhuma biblioteca externa é necessária.

---

## Data

Junho de 2026.