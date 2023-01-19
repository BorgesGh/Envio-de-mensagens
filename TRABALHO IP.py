# VETORES PARA ARMAZENAMENTO DE DADOS
DISPOSTIVOS = [] 
IP = [] 
CAIXA_DE_MENSAGEM = []
ULTIMO_EMISSOR =[]

##### FUNÇÕES PARA PROPOSTIO GERAL #### 
#### LEITURA PADRÃO
def lerDados(): 
    x = input("Digite a opção: ")
    while x.isdigit() == False: 
        print("Valor invalido!")
        x = input("Digite a opção: ")

    return int(x)

#### PESQUISA PARA TODOS

def PESQUISAR(a,val):
    for i, e in enumerate(a): 
        if val == e: 
            return i 

    return -1
    
#### RELACIONADOS A DIGITAÇÃO IP
def DIGITAR_IP():
    x = input("Digite o IP: ")
    while len(x) < 8: 
        print("IP invalido!!")
        x = input("Digite o IP: ")

    return(x)

def GERAR_IP(b): 
   
    x = DIGITAR_IP()
    t = PESQUISAR(b,x)
    while t != -1: 
        print("\nIP inserido ja existente!! Insira um IP diferente")
        x = DIGITAR_IP()
        t = PESQUISAR(b,x)

    return(x)

def Octeto(b): 
    i = 0

    x = GERAR_IP(b) 
    temp = [] 
    temp = x.split(".")

    while i < len(temp): 
        if int(temp[i]) < 0 or int(temp[i]) > 255 or len(temp) != 4: 
            print("O IP nao respeita as regras de definicao!")
            print("Apenas valores entre 0 e 255. E 4 octetos xxx.xxx.xxx.xxx")
            temp.clear()
            x = GERAR_IP(b)  
            temp = x.split(".")
            i = 0

        i = i + 1

    print("\nO IP esta verificado!\n")

    return x


def RETORNAR_IP(b,val): 
    x = b[val] 
    return x

def COMPARAR_IP(vet1, b, indice):
    vet2 = []
    vet21 = []
    for i,e in enumerate(b): 
        vet2.clear()
        vet21.clear()
        
        vet2 = e.split(".")
        vet21.append(vet2[0])
        vet21.append(vet2[1])

        if vet1[0] == vet21[0] and vet1[1] == vet21[1] and i != indice: 
            return i 

    return int(-1)


### FERRAMENTAS PARA O SOFTWARE ####

def ADICIONAR_NO(a,b,c,d): 
    x = input ("Insira o nome do dispositivo: ") 
    x = x.upper()

    a.append(x) 
    u = Octeto(b) 
    b.append(u) 
    c.append("<Vazio>") 
    d.append("<Vazio>")

def IMPRIMIR_NOS(a,b,c,d): 
    for i, e in enumerate(a):
        print("\n\nDispositivo %s" %(i + 1))
        print("%s" %a[i])
        print("IP:%s " %b[i])
        print("Caixa de mensagem:%s" %c[i]) 
        print("Ip do ultimo emissor: %s" %d[i])
        print("---------------------------------------\n\n")

def LIMPAR_MENSAGENS(c): 
    for i, e in enumerate(c): 
        c[i] = "<Vazio>" 


def REMOVER_NO(a,b,c,d): 
    x = input("Insira o nome do nó a ser removido: ")
    x = x.upper()
    while x != 0: 
        z = PESQUISAR(a,x) 
        if z != -1: 
            del(a[z])
            del(b[z])
            del(c[z])
            del(d[z])
            x = 0
        else : 
            print("\nDispositivo nao encontrado!!\n")
            x = 0

#################################### SUBCATEGORIA// INFILTRACAO #####################

def SELECIONAR_NO(a):
    for i, e in enumerate(a): 
        print("%d - %s" %(i + 1, e))

    x = int(input("Escolha o dispostivo para utlizar (digite sua numeracao): ")) 
    return (x - 1)


######## ENVIAR MENSAGEM POR IP#################################
def ENVIAR_MENSAGEM(indice,ip,b,c,d): 
    temp = [] #Temp vai ser o local onde será guardados os dados da rede (192.168)
    temp.clear()

    temp = ip.split(".") 
    
    temp1 =[]
    temp1.clear()

    temp1.append(temp[0]) 
    temp1.append(temp[1])


    m = COMPARAR_IP(temp1,b,indice) #Retorna o indice do receptor, se existir(Ultimo emissor)

    if m > -1:#Comparação de existencia
        while m > -1: 
            x = input("\nDigite o IP do destinatário: ") 
            j = PESQUISAR(b,x)# Retorna indice do IP se existir na lista

            
            temp3 =[]
            temp3.clear()
            temp31 = []

            if j > -1: #Comparação de certificação
                y = b[j] 

                temp3 = y.split(".") #SEPARÇOES PARA COMPARAR OS 2 IP'S

                temp31.clear()

                temp31.append(temp3[0]) 
                temp31.append(temp3[1])

                if set(temp1) == set(temp31) and j != indice: 
                    x = input("Digite sua mensagem: ")
                    print("\n\nMensagem enviada com sucesso!!\n\n")

                    if c[j] == "<Vazio>":
                        c[j] = x 
                        d[j] = ip
                        return j
                    else:
                        c[j] = c[j] + "+"
                        c[j] = c[j] + x
                        d[j] = ip
                        return j

                else: 
                    print("--------------------------")
                    print("\nEste dispostivo nao compartilha da mesma rede!\n")
                    print("--------------------------")

            else: 
                print("--------------------------")
                print("\n\nIP nao existente no Banco de dados!!\n\n")
                print("--------------------------")

    else: 
        print("\n\n\nNão existe um dispositivo de mesma rede!!\n\n")
        return (0)

##################################################################
def BROADCAST(indice,ip, b, c, d):
    vet1 = []
    vet1.clear()

    k = ip.split(".") 

    vet11 =[] 
    vet11.clear()

    vet11.append(k[0])
    vet11.append(k[1])
    
    l = COMPARAR_IP(vet11,b,indice)
    if l > -1:
        s = input("Digite sua mensagem: ")
        vet2=[]
        vet21= []
        for i,e in enumerate(b): 
            vet21.clear()
            vet2.clear()
            
            vet2 = e.split(".")  

            vet21.append(vet2[0])
            vet21.append(vet2[1])

            if set(vet11) == set(vet21) and i != indice: 
                print("\n\nBroadcast realizado!!\n\n")
                if c[i] == "<Vazio>":
                    c[i] = s
                    d[i] = ip
                     
                else:
                    c[i] = c[i] + "+"
                    c[i] = c[i] + s
                    d[i] = ip
                    
    else: 
        print("--------------------------") 
        print("\n\n\nNão existe um dispositivo de mesma rede!!\n\n")
        return (0)

#################### PROGRAMA PRINCIPAL ######################### 

x = 1 
while x > 0: 
    print("-----------------------------------")
    print("1 - ADICIONAR UM NOVO DISPOSITIVO ")
    print("2 - REMOVER DISPOTIVO ")
    print("3 - LIMPAR CAIXA DE MENSAGENS")
    print("4 - IMPRIMIR")
    print("5 - POSSUIR DISPOSITVO") 
    print("0 - SAIR DO PROGRAMA\n")

    x = lerDados()
    while x < 0 or x > 9: 
        print("Valor invalido!") 
        x = lerDados()

    if x == 1: 
        #DIGITAR 192.168 POIS SE TRATA DE UMA REDE PRIVADA
        ADICIONAR_NO(DISPOSTIVOS,IP,CAIXA_DE_MENSAGEM, ULTIMO_EMISSOR) 
        print("\n\n\nNó adicionado com sucesso!\n\n\n")
        print("---------------------------") 
    elif x == 2: 
        REMOVER_NO(DISPOSTIVOS,IP,CAIXA_DE_MENSAGEM, ULTIMO_EMISSOR)
        print("\n\n\nDispotivo removido!!\n\n\n") 
        print("---------------------------")
    elif x == 3: 
        LIMPAR_MENSAGENS(CAIXA_DE_MENSAGEM) 
        print("\n\n\nMensagens apagadas!!\n\n\n")
        print("---------------------------") 
    elif x == 4:
        IMPRIMIR_NOS(DISPOSTIVOS,IP, CAIXA_DE_MENSAGEM,ULTIMO_EMISSOR) 
        print("\n\n\nTodos os dispositivos foram exibidos!!\n\n\n") 
        print("---------------------------")

    # INFILTRAÇAO DE APARELHO
    elif x == 5: 
        n = SELECIONAR_NO(DISPOSTIVOS)
        ip_mestre = RETORNAR_IP(IP,n) #RETORNA O IP DO DISPOSTIVO SELECIONADO
        indice = n

        h = 1
        while h > 0: 
            print("-----------------------------------")
            print("1 - Enviar mensagem por IP")
            print("2 - Fazer BROADCAST")
            print("0 - Sair do dispostivo\n")

            h = int(input("Digite a opção: ") )
            while h < 0 or h > 2: 
                print("Valor invalido!") 
                h = input("Digite a opção: ") 

            if h == 1: 
                l = ENVIAR_MENSAGEM(indice,ip_mestre,IP,CAIXA_DE_MENSAGEM,ULTIMO_EMISSOR)
            if h == 2: 
                BROADCAST(indice,ip_mestre, IP, CAIXA_DE_MENSAGEM, ULTIMO_EMISSOR)
                 
    x = 1        
    input("Pressione <enter> para continuar...")
            
