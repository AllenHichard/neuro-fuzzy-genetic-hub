#plt.imshow(mapa, cmap='gray')  # black = close = clusters
#plt.show()
#https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-python-numpy
import numpy as np
import matplotlib.pyplot as plt

def mapa(topologia):
    np.random.seed(1)
    if topologia == 1:
        mapa = np.random.random_sample(size=(30, 30, 4))
        return mapa
    elif topologia == 2:
        index = 0
        mapa = np.random.random_sample(size=(30, 30, 4))
        for i in range(30):
            for j in range(30):
                mapa[i][j] = [index/900, index/900, index/900, index/900]
                index+=1
        return mapa
    elif topologia == 3:
        index = 0
        mapa = np.random.random_sample(size=(30, 30, 4))
        for i in range(30):
            for j in range(30):
                if i%2 == 0 and j%2 == 0:
                    mapa[i][j] = [index / 900, index / 900, index / 900, index / 900]
                else:
                    mapa[i][j] = 0
                index+=1
        return mapa

#print(mapa)
#plt.imshow(mapa, cmap='gray')  # black = close = clusters
#plt.show()