import numpy as np

def distanciaEuclidiana(v1, v2):
  return np.linalg.norm(v1 - v2)

def constructUMatrix(linhas, colunas, mapa):
    u_matrix = np.zeros(shape=(linhas,colunas), dtype=np.float64)
    for i in range(linhas):
        for j in range(colunas):
            v = mapa[i][j] #retorna os 4 atributos do mapa
            sum_dists = 0.0; ct = 0
            #calcula a distancia eucliciana com os nós que estão acima, abaixo e dos lados
            if i - 1 >= 0:  # above
                sum_dists += distanciaEuclidiana(v, mapa[i - 1][j])
                ct += 1
            if i + 1 <= linhas - 1:  # below
                sum_dists += distanciaEuclidiana(v, mapa[i + 1][j])
                ct += 1
            if j - 1 >= 0:  # left
                sum_dists += distanciaEuclidiana(v, mapa[i][j - 1])
                ct += 1
            if j + 1 <= colunas - 1:  # right
                sum_dists += distanciaEuclidiana(v, mapa[i][j + 1])
                ct += 1
            u_matrix[i][j] = sum_dists / ct
    return u_matrix