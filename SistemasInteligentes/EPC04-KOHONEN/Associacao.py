import numpy as np

def distanciaEuclidiana(v1, v2):
  return np.linalg.norm(v1 - v2)

def noMaisProximo(Xs, t, mapa, linhas, colunas):
  result = (0,0) #bidimensional
  raio = 1.0e20
  for i in range(linhas):
    for j in range(colunas):
      ed = distanciaEuclidiana(mapa[i][j], Xs[t])
      if ed < raio:
        raio = ed
        result = (i, j)
  return result

def maisComum(lst, n):
  # lst is a list of values 0 . . n
  if len(lst) == 0: return -1
  counts = np.zeros(shape=n, dtype=np.int) #[vetor com 3 posições, numero da classe]
  for i in range(len(lst)):
    counts[lst[i]] += 1
  return np.argmax(counts)

def Associating(linhas, colunas, mapa, Xs, Ys):
    mapping = np.empty(shape=(linhas, colunas), dtype=object)
    for i in range(linhas):
        for j in range(colunas):
            mapping[i][j] = []
    for t in range(len(Xs)):
        (m_row, m_col) = noMaisProximo(Xs, t, mapa, linhas, colunas)
        mapping[m_row][m_col].append(Ys[t])
        #print(mapping[m_row][m_col], Ys[t]) #pegando o proximo e acrescentando a classe

    label_map = np.zeros(shape=(linhas, colunas), dtype=np.int)
    for i in range(linhas):
        for j in range(colunas):
            #print(maisComum(mapping[i][j], 3))
            label_map[i][j] = maisComum(mapping[i][j], 3)
    return label_map