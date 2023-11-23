from tools import *

def laberinto(M, i, j, i1, j1, paso):
    global c
    if not posValida(M, i, j):
        return
    M[i][j]=paso
    if i ==i1 and j ==j1:
        mostrar(M)
        c+=1
    laberinto(M, i, j-1, i1, j1, paso+1)
    laberinto(M, i-1, j, i1, j1, paso+1)
    laberinto(M, i, j+1, i1, j1, paso+1)
    laberinto(M, i+1, j, i1, j1, paso+1)
    M[i][j]=0

def laberintoDiagonal(M, i, j, i1, j1, paso):
    global c
    if not posValida(M, i, j):
        return
    M[i][j]=paso
    if i ==i1 and j ==j1:
        mostrar(M)
        c+=1
    laberintoDiagonal(M, i, j-1, i1, j1, paso+1)
    laberintoDiagonal(M, i-1, j-1, i1, j1, paso+1)
    
    laberintoDiagonal(M, i-1, j, i1, j1, paso+1)
    laberintoDiagonal(M, i-1, j+1, i1, j1, paso+1)
    
    laberintoDiagonal(M, i, j+1, i1, j1, paso+1)
    laberintoDiagonal(M, i+1, j+1, i1, j1, paso+1)
    
    laberintoDiagonal(M, i+1, j, i1, j1, paso+1)
    laberintoDiagonal(M, i+1, j-1, i1, j1, paso+1)
    M[i][j]=0

def laberintoCaballo(M, i, j, i1, j1, paso):
    global c
    if not posValida(M, i, j):
        return
    M[i][j]=paso
    if i ==i1 and j ==j1:
        mostrar(M)
        c+=1
    laberintoCaballo(M, i-1, j-2, i1, j1, paso+1)
    laberintoCaballo(M, i-2, j-1, i1, j1, paso+1)
    
    laberintoCaballo(M, i-2, j+1, i1, j1, paso+1)
    laberintoCaballo(M, i-1, j+2, i1, j1, paso+1)
    
    laberintoCaballo(M, i+1, j+2, i1, j1, paso+1)
    laberintoCaballo(M, i+2, j+1, i1, j1, paso+1)
    
    laberintoCaballo(M, i+2, j-1, i1, j1, paso+1)
    laberintoCaballo(M, i+1, j-2, i1, j1, paso+1)
    M[i][j]=0

def laberintoTorre(M, i, j, i1, j1, paso):
    global c
    if not posValida(M, i, j):
        return
    M[i][j]=paso
    if i ==i1 and j ==j1:
        mostrar(M)
        c+=1
    laberintoTorre(M, i, j-(len(M[i])-1), i1, j1, paso+1)
    laberintoTorre(M, i-(len(M)-1), j, i1, j1, paso+1)
    laberintoTorre(M, i, j+(len(M[i])-1), i1, j1, paso+1)
    laberintoTorre(M, i+(len(M)-1), j, i1, j1, paso+1)
    M[i][j]=0


if __name__ == '__main__':
    a = 3
    b = 3
    c = 0
    M = [[0]*a for _ in range(b)]
    laberintoTorre(M,1,1,a-1,b-1,1)
    print('Soluciones: ',c)