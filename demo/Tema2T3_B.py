from reglas import *
from tools import *


def laberinto(M, i, j, i1, j1, paso):
    global c
    M[i][j]=paso
    if i ==i1 and j ==j1:
        mostrar(M)
        c+=1
    L = reglasAplicablesC(M, i, j)
    while L:
        R = mejorReglaA(L, i, j)
        M[R.fil][R.col] = paso
        laberinto(M, R.fil, R.col, i1, j1, paso+1)
        M[R.fil][R.col] = 0

if __name__ == '__main__':
    a = 3
    b = 3
    c = 0
    M = [[0]*a for _ in range(b)]
    M[0][2] = -1
    laberinto(M,0,0,a-1,b-1,1)
    print('Soluciones: ',c)