import numpy as np
import matplotlib.pyplot as plt
import File as file
import SOM as som
import MatrixU as matrixU
import Associacao as associacao
from sklearn.cluster import KMeans

def main():
  dimensao = 4
  linhas = 30
  colunas = 30
  AlcanceMaximo = linhas + colunas
  taxaAprendizagem = 0.5 # taxa de aprendizagem
  StepsMax = 5000 # variáveis de manipulação

  (Xs,Ys) = file.openFile()

  for topologia in range(1,4):
    mapa = som.constructSOM(linhas, colunas, dimensao, StepsMax, AlcanceMaximo, taxaAprendizagem, Xs, topologia)
    u_matrix = matrixU.constructUMatrix(linhas, colunas, mapa)
    plt.subplot(2, 3, topologia)
    plt.imshow(u_matrix, cmap='gray')  # black = close = clusters # U-Matrix

    #porque os dados possuem rótulos, outra visualização é possível:
    #associar cada rótulo de dados a um nó do mapa
    label_map = associacao.Associating(linhas, colunas, mapa, Xs, Ys)
    plt.subplot(2, 3, topologia+3)
    plt.imshow(label_map, cmap=plt.cm.get_cmap('terrain_r', 4))
    plt.colorbar()
  plt.show()

  kmeans = KMeans(n_clusters=3, random_state=0).fit(Xs)
  #print(Ys)
  #print(kmeans.labels_)
  acerto = 0
  for i in range(len(Ys)):
    if(Ys[i] == 0 and kmeans.labels_[i] == 1):
      acerto += 1
    elif (Ys[i] == 1 and kmeans.labels_[i] == 2):
      acerto += 1
    elif (Ys[i] == 2 and kmeans.labels_[i] == 0):
      acerto += 1

  print("Acurácia = ", acerto*100/len(Ys), "%")



if __name__=="__main__":
  main()
