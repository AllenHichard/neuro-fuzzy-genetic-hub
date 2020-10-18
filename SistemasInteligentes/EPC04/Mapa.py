import numpy as np
import matplotlib.pyplot as plt
mapa = np.random.random_sample(size=(30, 30, 4))
#https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-python-numpy

#plt.imshow(mapa, cmap='gray')  # black = close = clusters
#plt.show()

lista = []
for i in range(30):
    lista.append(i)
xvalues = np.array(lista);
yvalues = np.array(lista);
xx, yy = np.meshgrid(xvalues, yvalues)
print(yy)
plt.plot(xx, yy, marker='.', color='k', linestyle='none')
plt.show()