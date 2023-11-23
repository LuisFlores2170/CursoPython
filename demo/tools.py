#A) CON CICLOS

def posValida(M, i, j):
    return i>=0 and i<len(M) and j>=0 and j<len(M[i]) and M[i][j]==0

def mostrar(M):
    print('-'*100)
    for F in M:
        print(F)

def distancia(x1, y1, x2, y2):
    import math
    return int(math.sqrt( pow(x1-y1, 2)+ pow(x2-y2,2) ))