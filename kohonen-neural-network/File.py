import numpy as np
def openFile():
    file = "iris_data.txt"
    x = np.loadtxt(file, delimiter=",", usecols=range(0, 4),
                        dtype=np.float64)
    y = np.loadtxt(file, delimiter=",", usecols=[4],
                        dtype=np.int)
    return x, y