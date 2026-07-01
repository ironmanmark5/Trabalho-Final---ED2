from arvoreBinaria import ArvoreBinaria
from no import No

if __name__ == "__main__":
    arvore_binaria = ArvoreBinaria()

    arvore_binaria.raiz = arvore_binaria.inserir(None, 10)
    raiz = arvore_binaria.raiz
    
    arvore_binaria.inserir(raiz, 5)
    arvore_binaria.inserir(raiz, 15)
    arvore_binaria.inserir(raiz, 2)
    arvore_binaria.inserir(raiz, 7)
    arvore_binaria.inserir(raiz, 12)
    arvore_binaria.inserir(raiz, 20)
    
    # Teste 1 - Inserções Básicas
    print("Teste 1\n")
    print("=== PERCURSOS ===")
    print("Pre-ordem: ", end="")
    arvore_binaria.pre_ordem(raiz)
    print("\nEm-ordem: ", end="")
    arvore_binaria.em_ordem(raiz)
    print("\nPos-ordem: ", end="")
    arvore_binaria.pos_ordem(raiz)

    print("\n\nALTURA:")
    print(arvore_binaria.altura(raiz))
    print("\n-------------------\n")
    print("NÚMERO DE NÓS:")
    print(arvore_binaria.contar_nos(raiz))
    print("\n-------------------\n")
    print("NÚMERO DE FOLHAS:")
    print(arvore_binaria.contar_folhas(raiz))
    print("\n-------------------\n")

    # Teste 2 - Busca 
    print("Teste 2\n")
    print(f"Buscar 7: {arvore_binaria.buscar(raiz, 7)}")
    print(f"Buscar 12: {arvore_binaria.buscar(raiz, 12)}")
    print(f"Buscar 99: {arvore_binaria.buscar(raiz, 99)}")
    print(f"Buscar 1: {arvore_binaria.buscar(raiz, 1)}")
    print("\n-------------------\n")

    # Teste 3 - Menor e maior
    print("Teste 3\n")
    print(f"MENOR VALOR: {arvore_binaria.minimo(raiz)}")
    print(f"MAIOR VALOR: {arvore_binaria.maximo(raiz)}")  
    print("\n-------------------\n")
    
    # Teste 4 - Remoção de nó folha
    print("Teste 4\n")
    raiz = arvore_binaria.remover(raiz, 2)
    arvore_binaria.em_ordem(raiz)
    print("\n\n-------------------\n")

    # Teste 5 - Remoção de nó com um filho
    print("Teste 5\n")
    arvore_binaria2 = ArvoreBinaria()
    arvore_binaria2.raiz = arvore_binaria2.inserir(None, 10)
    raiz2 = arvore_binaria2.raiz
    arvore_binaria2.inserir(raiz2, 5)
    arvore_binaria2.inserir(raiz2, 15)
    arvore_binaria2.inserir(raiz2, 2)
    arvore_binaria2.inserir(raiz2, 7)
    arvore_binaria2.inserir(raiz2, 6)
    

    print("\nÁrvore Binária antes da remoção(em ordem): \n")
    arvore_binaria2.em_ordem(raiz2)
    print()

    print("\nÁrvore Binária depois da remoção(em ordem): \n")
    raiz2 = arvore_binaria2.remover(raiz2, 7)
    arvore_binaria2.em_ordem(raiz2)
    print("\n\n-------------------\n")

    # Teste 6 - Remoção de Nó com dois filhos
    print("Teste 6\n")
    arvore_binaria3 = ArvoreBinaria()
    arvore_binaria3.raiz = arvore_binaria3.inserir(None, 10)
    raiz3 = arvore_binaria3.raiz
    arvore_binaria3.inserir(raiz3, 5)
    arvore_binaria3.inserir(raiz3, 15)
    arvore_binaria3.inserir(raiz3, 2)
    arvore_binaria3.inserir(raiz3, 7)
    arvore_binaria3.inserir(raiz3, 12)
    arvore_binaria3.inserir(raiz3, 20)

    print("\nÁrvore Binária antes da remoção(em ordem): \n")
    arvore_binaria3.em_ordem(raiz3)
    print()

    print("\nÁrvore Binária depois da remoção(em ordem): \n")
    raiz3 = arvore_binaria3.remover(raiz3, 10)
    arvore_binaria3.em_ordem(raiz3)
    print("\n\n-------------------\n")

    # Teste 7 - Árvore degenerada
    print("Teste 7\n")
    arvore_binaria4 = ArvoreBinaria()
    arvore_binaria4.raiz = arvore_binaria4.inserir(None, 1)
    raiz4 = arvore_binaria4.raiz

    for i in range(2, 6): 
        arvore_binaria4.inserir(raiz4, i)

    print("\nÁrvore Degenerada (em ordem): \n")
    arvore_binaria4.em_ordem(raiz4)
    print()

    print(f"\nAltura da árvore degenerada: {arvore_binaria4.altura(raiz4)} \n")
    print(f"Número de nós na árvore degenerada: {arvore_binaria4.contar_nos(raiz4)} \n")
    print(f"Número de folhas na árvore degenerada: {arvore_binaria4.contar_folhas(raiz4)} ")

    