from matplotlib import pylab
import generational_genetic_algorithm_binary as geracional
import steady_state_genetic_algorithm as state
import matplotlib.pyplot as plt
import numpy as np
import math

populacao_tam = 100
geracao_qtd = 200
taxas_cruzamento = [0.7, 0.8, 0.9]
mutacao = 0.01
taxaElitismo = 0.1
#Geracional
Xv = np.arange(-1,2.01, 0.01)
Yv=[]
for x in Xv:
    Yv.append(x*math.sin(10*math.pi*x) + 1)
evol = [1,4,7]

def exibicao(geracoes, xs, ys, index):
    plt.subplot(3, 3, index)
    if index == 1:
        plt.title('Evolução do melhor indivíduo X - Y')
    plt.plot(xs, ys, "-")  # - oadrão x

    plt.subplot(3, 3, index + 1)
    if index == 1:
        plt.title('Gráfico da f(x) com evolução')
    plt.plot(Xv, Yv, xs, ys, "o")

    plt.subplot(3, 3, index + 2)
    if index == 1:
        plt.title('Evolução do melhor indivíduo Geracao - Y')
    print(geracoes)
    plt.plot(geracoes, ys)
    #plt.xticks(range(0, len(ys), int(len(ys) / 10)))  # alterar a escala


fig = pylab.gcf()
for index, cruzamento in zip(evol, taxas_cruzamento):
    (geracoes, xs, ys) = geracional.generational_binary(populacao_tam, geracao_qtd, cruzamento, mutacao, taxaElitismo)
    fig.canvas.set_window_title('1 - Geracional Variando Cruzamento')
    exibicao(geracoes, xs, ys, index)
plt.show()

fig = pylab.gcf()
for index, cruzamento in zip(evol, taxas_cruzamento):
    (geracoes, xs, ys) = state.state_binary(populacao_tam, geracao_qtd, cruzamento, mutacao, taxaElitismo)
    fig.canvas.set_window_title('2 - state Variando Cruzamento')
    exibicao(geracoes, xs, ys, index)
plt.show()

populacao_tam = 100
geracao_qtd = 200
cruzamento = 0.9
taxas_mutacao = [0.01, 0.05, 0.1]
taxaElitismo = 0.1

fig = pylab.gcf()
for index, mutacao in zip(evol, taxas_mutacao):
    (geracoes, xs, ys) = geracional.generational_binary(populacao_tam, geracao_qtd, cruzamento, mutacao, taxaElitismo)
    fig.canvas.set_window_title('3 - Geracional Variando Mutação')
    exibicao(geracoes, xs, ys, index)
plt.show()

fig = pylab.gcf()
for index, mutacao in zip(evol, taxas_mutacao):
    (geracoes, xs, ys) = state.state_binary(populacao_tam, geracao_qtd, cruzamento, mutacao, taxaElitismo)
    fig.canvas.set_window_title('4 - State Variando Mutação')
    exibicao(geracoes, xs, ys, index)
plt.show()