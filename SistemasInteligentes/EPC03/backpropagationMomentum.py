from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.supervised.trainers import BackpropTrainer
from pybrain3.datasets.classification import ClassificationDataSet
from PreProcess import PreProcess
import Tabela
import time as t
import statistics as st
import matplotlib.pyplot as plt


def teste(i):
    print("Testando")
    acc = 0
    preProcess.parser(f"iris-10-fold/test/iris-10-{str(i)}tst.dat")
    dataset_test = preProcess.data
    for row_teste in dataset_test:
        if int(round(melhorNN.activate(row_teste[:4])[0], 0)) == row_teste[4]:
            acc += 1
    ACURACIA = acc / len(dataset)
    return ACURACIA


for topo, indexPlot in zip(range(3,8,2), range(1,4)):
    nameArchive = f"ESTATÍSTICAS-MOMENTUM-TOPO-INTER-{str(topo)}.xlsx"
    arquivo = Tabela.__CriarTabela__(nameArchive)
    #TabelaTeste.__CriarTabela__()
    acuracias = []
    EQMs = []
    Tempos = []
    Epocas = []
    acuraciasTest = []
    for i in range(1,11):
        for j in range(1,4):
            preProcess = PreProcess()
            preProcess.parser(f"iris-10-fold/train/iris-10-{str(i)}tra.dat")
            dataset = preProcess.data
            ds = ClassificationDataSet(4, 1) #4 inputs e 1 output
            for row in dataset:
                inputs = [float(val) for val in row[:4]]
                ds.addSample(inputs, row[4])
            # por padrão é sigmoide e os valores de w variam entre 0 e 1
            nn = buildNetwork(ds.indim, topo , ds.outdim, bias=True)
            treinador = BackpropTrainer(nn, ds, learningrate=0.1, momentum=0.9)
            print("Construiu a rede")
            melhorAcuracia = 0
            EQM = 100
            PlotEQM = []
            convergenciaEpocas = 0
            totalEpocas = 0
            t0 = t.time()
            print(len(dataset))
            while(convergenciaEpocas < 50):
                treinador.train()
                acc = 0
                somatorioErro = 0
                for linha in dataset:
                     somatorioErro += (linha[4] - nn.activate(linha[:4])[0]) ** 2
                     if int(round(nn.activate(linha[:4])[0],0)) == linha[4]:
                         acc +=1
                erro = somatorioErro/len(dataset)
                PlotEQM.append(erro)
                ACURACIA = acc / len(dataset)
                if (ACURACIA > melhorAcuracia):
                    melhorAcuracia = ACURACIA
                    convergenciaEpocas = 0
                    EQM = erro
                    melhorNN = nn.copy()
                    print(melhorAcuracia, EQM)
                else:
                    convergenciaEpocas +=1
                totalEpocas += 1
            tempo = t.time() - t0
            print("Total Epocas ", totalEpocas)
            print("Treinou")
            accTest = teste(i)
            acuraciasTest.append(accTest)
            Tabela.inserirValores(arquivo, nameArchive, topo, melhorAcuracia, EQM, totalEpocas, tempo, accTest)
            acuracias.append(melhorAcuracia)
            EQMs.append(EQM)
            Tempos.append(tempo)
            Epocas.append(totalEpocas)
            plt.subplot(3, 1, indexPlot)
            plt.plot(PlotEQM, label="Treinamento " + str(i) + "-" +str(j))
            plt.legend()
            plt.xticks(range(0, len(PlotEQM), 50))  # alterar a escala
            plt.title('Erro quadrático médio (EQM) em função de cada época')
            plt.xlabel("Época")
            plt.ylabel("EQM")

    Tabela.inserirValores(arquivo, nameArchive, "-----------", "Média Acurácia Treinamento", "Média EQM", "Média Épocas", "Média Tempo", "Média Acurácia Teste")
    Tabela.inserirValores(arquivo, nameArchive, "-----------", st.mean(acuracias), st.mean(EQMs), st.mean(Epocas), st.mean(Tempos), st.mean(acuraciasTest))
    Tabela.inserirValores(arquivo, nameArchive, "-----------", "DP Acurácia Treinamento", "DP EQM", "DP Épocas", "DP Tempo", "DP Acurácia Teste")
    Tabela.inserirValores(arquivo, nameArchive, "-----------", st.pstdev(acuracias), st.pstdev(EQMs), st.pstdev(Epocas), st.pstdev(Tempos), st.pstdev(acuraciasTest))
plt.show()





#teste()






