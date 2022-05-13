'''
   MAC0122 Principios de Desenvolvimento de Algoritmos
 
   NÃO MODIFIQUE ESTE ARQUIVO

   Este arquivo contem o programa principal do projeto.
'''

# tk.tokeniza(), 
import tokeniza as tk

# categorias e dicionario "categoria: decrição" 
import operadores as op

# desenha o grafo da expressão g.create_grafo()
import grafo as g

PROMPT = "expressão >>> "
QUIT   = ''

#------------------------------------------------------------
def main():
    '''None -> None

    Programa que lê do teclado uma expressão aritmética 
    e imprime cada item léxico na expressão.

    Exemplos:

    
    '''
    print("Entre como uma expressão ou tecle apenas ENTER para encerrar.") 
    expressao = input(PROMPT)
    while expressao != QUIT:
        lista_tokens = tk.tokeniza(expressao)
        for token in lista_tokens:
            # pegue item e tipo
            item, tipo = token

            # cri string com a descriçao
            if tipo in [tk.OPERADOR, tk.PARENTESES]:
                descricao = "'%s' : %s" %(item,op.DESCRICAO[item])
            elif tipo == tk.VARIAVEL:
                descricao = "'%s' : nome de variável" %item
            elif tipo == tk.NUMERO:
                descricao = "%f : constante float" %item
            else:
                descricao = "'%s' : categoria desconhecida" %item

            # imprima a descriçao
            print(descricao)

        #cria o grafo da expressao
        g.create_grafo(lista_tokens)

        # leia próxima expressão    
        expressao = input(PROMPT)        

#-------------------------------------------
# início da execução do programa
main()
        