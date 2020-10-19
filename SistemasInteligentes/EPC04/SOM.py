import numpy as np
import matplotlib.pyplot as plt
import Mapa as m

def distanciaEuclidiana(v1, v2):
  return np.linalg.norm(v1 - v2)

def distanciaManhattan(r1, c1, r2, c2):
  return np.abs(r1-r2) + np.abs(c1-c2)

def noMaisProximo(Xs, indexAleatoriaInstancia, mapa, linhas, colunas):
  result = (0,0) #bidimensional
  raio = 1.0e20
  for i in range(linhas):
    for j in range(colunas):
      ed = distanciaEuclidiana(mapa[i][j], Xs[indexAleatoriaInstancia])
      if ed < raio:
        raio = ed
        result = (i, j)
  return result

def constructSOM(linhas, colunas, dim, StepsMax, AlcanceMaximo, taxaAprendizagem, Xs, topologia):
    #np.random.seed(1)
    #mapa = np.random.random_sample(size=(linhas, colunas, dim))
    mapa = m.mapa(topologia)
    for s in range(StepsMax):
        if s % (StepsMax/10) == 0: print("Geração = ", str(s))
        pct_left = 1.0 - ((s * 1.0) / StepsMax) #varia de 0 até 100%
        alcanceAtual = (int)(pct_left * AlcanceMaximo) # varia de 0 a 60 pontos
        taxaAtual = pct_left * taxaAprendizagem
        indexAleatoriaInstancia = np.random.randint(len(Xs))
        #posição i j no mapa mais próxima
        (bmu_row, bmu_col) = noMaisProximo(Xs, indexAleatoriaInstancia, mapa, linhas, colunas)
        #reajustes dos nós
        for i in range(linhas):
            for j in range(colunas):
                if distanciaManhattan(bmu_row, bmu_col, i, j) < alcanceAtual:
                    mapa[i][j] = mapa[i][j] + taxaAtual * (Xs[indexAleatoriaInstancia] - mapa[i][j])
    return mapa