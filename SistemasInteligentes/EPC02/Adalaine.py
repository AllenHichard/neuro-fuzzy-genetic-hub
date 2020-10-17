import random
import matplotlib.pyplot as plt


n = 0.0025
e = 10**-6 #precisão
def getU(instancia, pesos):
    u = 0
    for indice in range(0, len(pesos)):
        u += pesos[indice]*float(instancia[indice]) # pesos[0] é o deslocamento
    return u

def sinal(u):
    if u >= 0: return 1 # B
    else: return -1 # A

def ajustePesos(dk, u, XK, pesos):
    for i in range(len(pesos)):
        pesos[i] = pesos[i] + n*(dk - u)*float(XK[i])

instancias = []
treinamento = open("dados.txt", "r")
for instancia in treinamento.readlines():
    instancias.append(instancia.split())

instanciasTeste = []
teste = open("teste.txt", "r")
for instancia in teste.readlines():
    instanciasTeste.append(instancia.split())

def redeNeuralAdalaine(pesos):
    EQM_ant = float("inf");
    EQM_atual = 1
    geracao = 0
    EQMs = []
    EQMs.append(EQM_atual)
    while(abs(EQM_atual - EQM_ant) > e):
        #print(abs(EQM_atual - EQM_ant))
        EQM_ant = EQM_atual
        #print("Geração - ", geracao, " Taxa de Acurácia - " , acuracia, "%")
        somatorioErro = 0
        for instancia in instancias:
            u = getU(instancia, pesos)
            dx = float(instancia[5])
            ajustePesos(dx, u, instancia, pesos)
            somatorioErro += (dx - u)**2
        geracao+=1
        EQM_atual = somatorioErro/len(instancias)
        EQMs.append(EQM_atual)
    return pesos, geracao, EQMs
    #print("Geração - ", geracao, " Taxa de Acurácia - " , acuracia, "%")

def teste(pesos):
    classificacao = []
    for instancia in instanciasTeste:
        u = getU(instancia, pesos)
        Y = sinal(u)
        if (Y == -1):
            # print(instancia)
            classificacao.append("A")
        else:
            classificacao.append("B")
    return classificacao

for i in range(1, 6):
    pesos = [random.random(), random.random(), random.random(),
             random.random(), random.random()]  # ------- W0.....Wn Inicializando o vetor de pesos com valores aleatórios
    print("Execução --- ", i)
    print("Peso Inicias", pesos)  # pesos
    resp = redeNeuralAdalaine(pesos)
    print("Peso Finais", resp[0])  # pesos
    print("Classificação", teste(resp[0]))
    print("Gerações", resp[1])  # geracoes
    print()
    plt.plot(resp[2], label="Treinamento " + str(i))
    plt.legend()
    #plt.legend("Treinamento " + str(i))
    plt.xticks(range(0, len(resp[2]), 50)) # alterar a escala

plt.title('Erro quadrático médio (EQM) em função de cada época')
plt.xlabel("Época")
plt.ylabel("EQM")
plt.show()



