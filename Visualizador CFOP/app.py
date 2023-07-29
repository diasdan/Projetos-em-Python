#Tabela CFOP
#Esse script tem por objetivo auxiliar o operador fiscal na consulta e pesquisa de CFOPs
from os import system
from time import sleep

def validateInput(value):  
    
    try:
        numVal = convertStringToNum(value)   
        if numVal not in range(1000, 7549):
            print("\n   Valor inválido.\n")
            return False
        else:
            return True
    except ValueError:
        print("   Erro: Valor inválido.\n")
    except TypeError:
        print("   Erro: Valor inválido.\n")


# Módulo simples de conversão de número para string no formato x.xxx 
def convertNumToString(num):
    try:
        numChar =  str(num)
        listNumChar = []
        # a cada iteração o caractere convertido será adcionado à lista
        for l in numChar:
            listNumChar.append(l)
        #caractere "." é adicionado 
        listNumChar.insert(1, ".")
        string = ''.join(listNumChar)
        return string # retorna a string 
    except ValueError:
        print("   Erro: Valor inválido.\n")
    except TypeError:
        print("   Erro: Valor inválido.\n")
        
# Módulo simples de conversão de string no formato x.xxx para número 
def convertStringToNum(string):
    try:
        stringList = []
        #será adicionada à lista vazia os caracteres diferentes do "."
        for j in string:
            if j != ".":
                stringList.append(j)
        string2 = "".join(stringList)
        #string é formatada para numérico
        num = int(string2)
        return num #retorno do valor numérico
    except ValueError:
        print("   Erro: Tipo de valor inválido.")
        
#Função de introdução do script
# Apenas imprime a primeira mensagem na tela e retorna a opção desejada
def scriptIntro():
    while True:
        print("    Você deseja")
        try:
            op = int(input("""
        | 1 - Consultar uma CFOP
        | 2 - Pesquisar uma CFP
        | 0 - Sair do Programa

    Selecionar [0/1/2]: """))
            return op
        except ValueError:
            print("\n   Por favor, informe uma categoria válida.")

#Função de consulta de CFOP
def consultCfop(value): 
    sum = 0
    # a função recebe o valor da CFOP a ser consultada
    # o arquivo de texto é aberto e permutado em busca do valor 
    tabelaCfop = open("tabelaCfop.txt", "r", encoding="utf-8") 
    for num_line, line in enumerate(tabelaCfop, start=1):
        if value in line:       
            sum += 1
            print(f'\n    {line}')
            # o valor é impresso na tela
    if sum < 1:
        print("\n   Categoria não existente.")
    tabelaCfop.close() # arquivo fechado
    
# Função de apresentação das categorias
# essa função imprime na tela as categorias da opção desejada informada na
# função searchCfop()
def showCategories(value): 
        try:
            listCat = []  # lista vazia  
            c = 1 # contador, o valor deve ser 1 pois 0 imprime o título da categoria
            aux = convertStringToNum(value) # serve de indicador numérico na condicional, pois, após a iteração, o valor usado é convertido para string e não pode ser comparado 
            print("\nCategorias:\n ")

            for c in range(1000):
                tabelaCfop = open("tabelaCfop.txt", "r", encoding="utf-8") 
                for num_line, line in enumerate(tabelaCfop, start=1):
                    if value in line:  # o valor existir na linha, a linha será impressa   
                        print(f'    {line}')
                        listCat.append(value) # o valor é adicionado à lista que será preenchida com as subcategorias e retornada pela função para ser utilizada como parâmetro pela próxima função showSubCategories
                valNum = convertStringToNum(value) # o valor é convertido para numérico 
                valNum += 50 # o valor 50 é somado à variável numérica, o valor 50 representa o intervalo mínimo de valor das categorias 
                value = convertNumToString(valNum) # o valor é convertido a string novamente
                if valNum >= aux+1000: # se o valor for maior que o valor inicial + 1000 o loop deve parar pois 1000 é o intervalo que cobre todas as subcategorias da categoria 
                    break
            tabelaCfop.close()
            return listCat # lista de categorias é retornada
        except ValueError or TypeError:
            print("   Categoria inválida.\n")
        except TypeError:
            print("   Categoria inválida.\n")

# Função que irá apresentar as subcategorias da categoria indicada anteriormente
def showSubCategories(value, list):  

    numVal = convertStringToNum(value)
    numList = [] # lista numérica

    # esse loop converterá todos os itens da lista para numérico
    for item in list:
       
        numItem = convertStringToNum(item)
        numList.append(numItem)
    try:
        valIndex = numList.index(numVal) #coleta o índice do valor de entrada na lista
    except ValueError or IndexError:
        if numVal > max(numList):
           c = numVal
           c -= 1 

    c = numVal # valor da entrada é atribuída ao contador para que loop começe a contar a partir dele 
    valAux = c   
     
    while True:
        callBreak = False # chamada para o break do loop
        c += 1 #valor começa sendo incrementado com 1 para que não seja impressa o valor da Categoria
        target = convertNumToString(c) # o valor é convertido para string
        tabelaCfop = open("tabelaCfop.txt", "r", encoding="utf-8") 
        for num_line, line in enumerate(tabelaCfop, start=1):
                if target in line:       
                    print(f'    {line}') # o valor é buscado no arquivo e impresso 
                if numVal < max(numList):
                    if numList[valIndex + 1] >= valAux + 99:
                        if c >= (valAux+99) or c > 7949: # essa condicional irá parar o loop quando a variável atingir o valor do próximo número da lista, pois esse valor indica a próxima categoria 
                            callBreak = True 
                            break
                    elif numList[valIndex + 1] == valAux + 49:
                        if c >= (valAux+49) or c > 7949: # essa condicional irá parar o loop quando a variável atingir o valor do próximo número da lista, pois esse valor indica a próxima categoria 
                            callBreak = True 
                            break
                else:
                    if c > numVal+99:  # essa condicional irá parar o loop quando a variável atingir o valor do próximo número da lista, pois esse valor indica a próxima categoria 
                        callBreak = True 
                        break
                    
        if callBreak:
            print(50*'-')
            break # para o loop
    tabelaCfop.close()
    return True 
    
# Função que irá mostrar os tipos de CFOP de entrada e saída  
def showTypes(value):
    type = ["1.000", "2.000", "3.000", "5.000", "6.000", "7.000"] #lista contendo os valores

    if value == 1:
        print("\nCFOPs de Entrada:\n")

        for c in range(3): # imprime os valores de entrada
            with open("tabelaCfop.txt", "r", encoding="utf-8") as tabelaCfop:
                for num_line, line in enumerate(tabelaCfop, start=1):
                    if type[c] in line:       
                        print(line)
        tabelaCfop.close()
                
    elif value == 2:
        print("\nCFOPs de Saída:\n")

        for c in range(3, 6): # imprime os valores de saída
            with open("tabelaCfop.txt", "r", encoding="utf-8") as tabelaCfop:
                for num_line, line in enumerate(tabelaCfop, start=1):
                    if type[c] in line:       
                        print(f'    {line}')
            tabelaCfop.close()

# Função de busca do CFOP, irá retornar o valor da opção para fazer a busca pelo CFOP desejado
def searchCfop():
    while True:
        print("\n   Qual tipo de CFOP deseja pesquisar?: ")
        try:
            option = int(input("""
    | 1 - CFOP de Entrada
    | 2 - CFOP de Saída
    | 0 - Sair do Programa

    Selecionar [0/1/2]: """))
            return option
        except ValueError:
            print('\n   Por favor, informe um valor válido.')

def showBanner():
        print(83*'-')
        print("""
████████╗░█████╗░██████╗░███████╗██╗░░░░░░█████╗░  ░█████╗░███████╗░█████╗░██████╗░
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║░░░░░██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║██████╦╝█████╗░░██║░░░░░███████║  ██║░░╚═╝█████╗░░██║░░██║██████╔╝
░░░██║░░░██╔══██║██╔══██╗██╔══╝░░██║░░░░░██╔══██║  ██║░░██╗██╔══╝░░██║░░██║██╔═══╝░
░░░██║░░░██║░░██║██████╦╝███████╗███████╗██║░░██║  ╚█████╔╝██║░░░░░╚█████╔╝██║░░░░░
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░░░░░""")
        print('----------------------------------- Danilo Dias -----------------------------------')
        print('\n')

def main():

    timer = 1
    showBanner()
    scriptOff = False

    while True:
        if scriptOff:
            break
        try:
            op = scriptIntro()
            if op == 0:
                scriptOff = True
                print("\n   Saindo do programa...", end='')
                for timer in range(2):
                    sleep(1)
                system('cls')
                timer = 0
                break
            if op == 1:
                system('cls')
                showBanner()  
                cfop = str(input("\n    Qual CFOP deseja consultar?: "))
                if validateInput(cfop):
                    consultCfop(cfop)
            if op == 2:
                while True:
                    system('cls')
                    showBanner()  
                    option = searchCfop()
                    if option == 0:
                        print("\n   Saindo do programa...\n")
                        scriptOff = True
                        break
                    elif option == 1 or option == 2:
                        system('cls')
                        showBanner() 
                        showTypes(option)
                        
                        while True:
                            optionCat = str(input("   Selecione a opção desejada: ")) 
                            if validateInput(optionCat):  
                                listCat = showCategories(optionCat)
                                break
                            else:
                                continue
                        while True:
                            optionSubCat = input("    Selecione a categoria desejada: ")
                            if validateInput(optionSubCat):
                                print(15*'-')
                                print('    Esses são os CFOPs para essa categoria:\n')
                                endSector = showSubCategories(optionSubCat, listCat)
                                if endSector:
                                    break
                            else:
                                continue
                        break
                    else:
                        print("\n   Por favor, digite um valor válido.\n")
                        continue
        except KeyboardInterrupt:
            print("\n\n    Cancelando operação...")
            for timer in range(3):
                sleep(2)
                system('cls')
            timer = 0
            break
        

main()
