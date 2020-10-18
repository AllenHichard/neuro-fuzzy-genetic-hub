import numpy as np
import matplotlib.pyplot as plt
import File as file
import SOM as som
import MatrixU as matrixU
import Associacao as associacao

def main():
  np.random.seed(1)
  dimensao = 4
  linhas = 30
  colunas = 30
  AlcanceMaximo = linhas + colunas
  taxaAprendizagem = 0.5
  StepsMax = 5000

  (Xs,Ys) = file.openFile()
  mapa = som.constructSOM(linhas, colunas, dimensao, StepsMax, AlcanceMaximo, taxaAprendizagem, Xs)
  u_matrix = matrixU.constructUMatrix(linhas, colunas, mapa)

  # U-Matrix
  #plt.imshow(u_matrix, cmap='gray')  # black = close = clusters
  #plt.show()

  #porque os dados possuem rótulos, outra visualização é possível:
  #associar cada rótulo de dados a um nó do mapa
  label_map = associacao.Associating(linhas, colunas, mapa, Xs, Ys)

  plt.imshow(label_map, cmap=plt.cm.get_cmap('terrain_r', 4))
  plt.colorbar()
  plt.show()




if __name__=="__main__":
  main()
