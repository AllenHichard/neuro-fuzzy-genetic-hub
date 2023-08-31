import random

instancias = []
n = 0.01 # Inicializando a taxa de aprendizagem proposta

def getU(instancia, pesos):
    u = 0
    for indice in range(0, len(pesos)):
        u += pesos[indice]*float(instancia[indice]) # pesos[0] é o deslocamento
    return u

def sinal(u):
    if u >= 0: return 1
    else: return -1

def ajustePesos(dk, y, XK, pesos):
    for i in range(len(pesos)):
        pesos[i] = pesos[i] + n*(dk - y)*float(XK[i])

treinamento = open("dados.txt", "r")
for instancia in treinamento.readlines():
    instancias.append(instancia.split())

instanciasTeste = []
teste = open("teste.txt", "r")
for instancia in teste.readlines():
    instanciasTeste.append(instancia.split())

def redeNeuralPerceptron(pesos):
    acuracia = 0
    geracao = 0
    while(acuracia < 100):
        qtdAcerto = 0
        #print("Geração - ", geracao, " Taxa de Acurácia - " , acuracia, "%")
        for instancia in instancias:
            u = getU(instancia, pesos)
            Y = sinal(u)
            dx = float(instancia[4])
            if (dx != Y):
                ajustePesos(dx, Y, instancia, pesos)
            else:
                qtdAcerto+=1
        geracao+=1
        acuracia = qtdAcerto*100/len(instancias)
    return pesos, geracao
    #print("Geração - ", geracao, " Taxa de Acurácia - " , acuracia, "%")


def teste(pesos):
    classificacao = []
    for instancia in instanciasTeste:
        u = getU(instancia, pesos)
        Y = sinal(u)
        classificacao.append(Y)
    return classificacao

for i in range(1, 6):
    pesos = [random.random(), random.random(), random.random(),random.random()]  # ------- W0.....Wn Inicializando o vetor de pesos com valores aleatórios
    print("Execução --- ", i)
    #print(pesos)
    print("Peso Inicias", pesos)  # pesos
    resp = redeNeuralPerceptron(pesos)
    print("Peso Finais" , resp[0]) # pesos
    print("Classificação", teste(resp[0]))
    print("Gerações", resp[1]) # geracoes
    print()


