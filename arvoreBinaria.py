from no import No

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None # Inicializa a raiz da árvore como None

    def esta_vazia(self) -> bool:
        return self.raiz == None

    def inserir(self, no: No, valor: int) -> No:
        if no == None:
            return No(valor) # Criar um novo nó com o valor e retornar
        
        if valor < no.valor:
            no.esquerda = self.inserir(no.esquerda, valor)
        
        elif valor > no.valor:
            no.direita = self.inserir(no.direita, valor)

        else:
            pass

        return no
    
    def buscar(self, no: No, valor: int) -> bool:
        if no == None:
            return False 
        
        if valor == no.valor:
            return True 
        
        if valor < no.valor:
            return self.buscar(no.esquerda, valor)
        
        elif valor > no.valor:
            return self.buscar(no.direita, valor)
        
    def minimo(self, no: No) -> int:
        if no == None:
            return None
        
        atual = no

        while atual.esquerda != None:
            atual = atual.esquerda

        return atual.valor
    
    def maximo(self, no: No) -> int:
        if no == None:
            return None
        
        atual = no

        while atual.direita != None:
            atual = atual.direita

        return atual.valor
    
    def menor_no(self, no: No) -> No:
        atual = no
        
        while atual.esquerda != None:
            atual = atual.esquerda

        return atual
    
    def remover(self, no: No, valor: int):
        if no == None:
            return None
        
        if valor < no.valor:
            no.esquerda = self.remover(no.esquerda, valor)

        elif valor > no.valor:
            no.direita = self.remover(no.direita, valor)

        else:
            if no.esquerda == None:
                return no.direita
            
            if no.direita == None:
                return no.esquerda
            
            sucessor = self.menor_no(no.direita)
            no.valor = sucessor.valor
            no.direita = self.remover(no.direita, sucessor.valor)

        return no
    
    def pre_ordem(self, no: No):
        if no != None:
            print(no.valor, end=" ")
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    def em_ordem(self, no: No):
        if no != None:
            self.em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self.em_ordem(no.direita)

    def pos_ordem(self, no: No):
        if no != None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor, end=" ")

    def altura(self, no: No) -> int:
        if no == None:
            return -1
        
        h_esq = self.altura(no.esquerda)
        h_dir = self.altura(no.direita)

        return 1 + max(h_esq, h_dir)
    
    def contar_nos(self, no: No) -> int:
        if no == None:
            return 0
        
        return 1 + self.contar_nos(no.esquerda) + self.contar_nos(no.direita)
    
    def contar_folhas(self, no: No) -> int:
        if no == None:
            return 0
        
        if no.esquerda == None and no.direita == None:
            return 1
        
        return self.contar_folhas(no.esquerda) + self.contar_folhas(no.direita)