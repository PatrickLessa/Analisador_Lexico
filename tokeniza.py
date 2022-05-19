"""
AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
OU PLÁGIO.
DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
DIVULGADOS NA PÁGINA DA DISCIPLINA.
ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

Nome :
NUSP :
Turma:
Prof.:

Referências: Com exceção das rotinas fornecidas no enunciado
e em sala de aula, caso você tenha utilizado alguma refência,
liste-as abaixo para que o seu programa não seja considerado
plágio ou irregular.

Exemplo:
    - O algoritmo Quicksort foi baseado em http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html

"""

# Constantes
TESTE   = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

# categorias
OPERADOR   = 1 # para operadores aritméticos e atribuição
NUMERO     = 2 # para números: todos são considerados float
VARIAVEL   = 3 # para variáveis
PARENTESES = 4 # para '(' e ')

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS    = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"


#------------------------------------------------------------
def tokeniza(exp):
    """(str) -> list

    Recebe uma string exp representando uma expressão e cria 
    e retorna uma lista com os itens léxicos que formam a
    expressão.

    Cada item léxico (= token) é da forma
       
        [item, tipo]

    O componente item de um token é 

        - um float: no caso do item ser um número; ou 
        - um string no caso do item ser um operador ou 
             uma variável ou um abre/fecha parenteses.

    O componente tipo de um token indica a sua categoria
    (ver definição de constantes acima). 

        - OPERADOR;
        - NUMERO; 
        - VARIAVEL; ou 
        - PARENTESES

    A funçao ignora tuo que esta na exp apos o caractere
    COMENTARIO (= "#").
    """
    # escreva o seu código abaixo

    token_list = []
    
    def cleanWhiteSpace(string):
        for element in BRANCOS:
            string = string.replace(element, "")
        return string

    def findComment(string):
        comment = string.find(COMENTARIO)
        if(comment >= 0):
            return string[0:comment]
        else:
            return string

    def verifyEmptyVariable(variable, category):
        if(variable != ""):
            if(category == NUMERO):
                token_list.append([float(variable), category])
            else:
                token_list.append([variable, category])
        

    def separator(string):
        # variavel de indice
        index = 0

        # laço até acabar a expressao
        while(index < len(string)):

            # declaração de variáveis auxiliares para cada categoria
            variableStr = ""
            operator = ""
            numberStr = ""
            erroStr = ""

            # verificação se será um float/número
            while(index < len(string) and string[index] in DIGITOS):

                # verifica se a variavel auxiliar de string está vazia, 
                # para poder dizer se esse numero pertence a um nome de variavel ou nao
                if(variableStr == ""):
                    numberStr += string[index]
                    index += 1

                # verificia se o próximo caracter a ser lido será um ponto,
                # indicando se é um numero decimal
                if(index < len(string) and string[index] == PONTO):
                    numberStr += string[index]
                    index += 1

            # verifica se o caracter pertence a um nome de variável
            while(index < len(string) and string[index] not in OPERADORES and string[index] not in ABRE_FECHA_PARENTESES):
                variableStr += string[index]
                index += 1

            # verifica se o caracter pertence aos operadores
            while(index < len(string) and string[index] in OPERADORES):
                operator += string[index]
                index += 1

            # Verifica se todas as variáveis foram preenchidas,
            # e se sim, irá adicionar a variavel e sua categoria na lista de tokens
            verifyEmptyVariable(numberStr, NUMERO)
            verifyEmptyVariable(variableStr, VARIAVEL)
            verifyEmptyVariable(operator, OPERADOR)

            # verifica se o caracter pertence aos parenteses
            if(index < len(string) and string[index] in ABRE_FECHA_PARENTESES):
                token_list.append([string[index], PARENTESES])
                index += 1

            while(index < len(string) and string[index] not in OPERADORES and string[index] not in ABRE_FECHA_PARENTESES and string[index] not in DIGITOS and string[index] not in LETRAS and string[index] not in PONTO):
                erroStr += string[index]
                index += 1
            
            verifyEmptyVariable(erroStr, 5)


    # clona a string da exp, para não alterar a original
    expression = exp

    # limpa os espaços em branco
    expression = cleanWhiteSpace(expression)

    # retorna a exressão sem o comentario
    expression = findComment(expression)

    # analise léxica
    separator(expression)
    return token_list

def tokeniza_arquivo():
    list_token_file = []

    # constantes para o separador dos elementos e quebra de linha
    SEPARATOR = ";"
    BREAK_LINE = "\n"

    # le o arquivo e passa para uma variável
    with open("data.txt", "r") as file:
        dados = file.readlines()

    # Le linha a linha da string do txt
    for line in dados:
        # retira as quebras de linha
        line = line.replace(BREAK_LINE, "")

        # faz a separação pelo separador definido
        list_line = line.split(SEPARATOR)

        # adiciona os elementos e suas categorias na lista
        category = 0
        for element in list_line:
            list_token_file.append([element.lstrip(), category])
            category += 1
        
    return list_token_file
