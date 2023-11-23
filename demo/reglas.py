from tools import *
class Reglas():
    def __init__(self, fil, col):
        self.fil = fil
        self.col = col

def reglasAplicables(M, i, j):
    L = []
    if posValida(M, i, j-1): L.append(Reglas(i, j-1))
    if posValida(M, i-1, j): L.append(Reglas(i-1, j))
    if posValida(M, i, j+1): L.append(Reglas(i, j+1))
    if posValida(M, i+1, j): L.append(Reglas(i+1, j))
    return L

def reglasAplicablesB(M, i, j):
    L = []
    if posValida(M, i, j-1): L.append(Reglas(i, j-1))
    if posValida(M, i-1, j-1): L.append(Reglas(i-1, j-1))
    
    if posValida(M, i-1, j): L.append(Reglas(i-1, j))
    if posValida(M, i-1, j+1): L.append(Reglas(i-1, j+1))
    
    if posValida(M, i, j+1): L.append(Reglas(i, j+1))
    if posValida(M, i+1, j+1): L.append(Reglas(i+1, j+1))
    
    if posValida(M, i+1, j): L.append(Reglas(i+1, j))
    if posValida(M, i+1, j-1): L.append(Reglas(i+1, j-1))
    
    return L

# Mov. caballo
def reglasAplicablesC(M, i, j):
    L = []
    if posValida(M, i-1, j-2): L.append(Reglas(i-1, j-2))
    if posValida(M, i-2, j-1): L.append(Reglas(i-2, j-1))
    
    if posValida(M, i-2, j+1): L.append(Reglas(i-2, j+1))
    if posValida(M, i-1, j+2): L.append(Reglas(i-1, j+2))
    
    if posValida(M, i+1, j+2): L.append(Reglas(i+1, j+2))
    if posValida(M, i+2, j+1): L.append(Reglas(i+2, j+1))
    
    if posValida(M, i+2, j-1): L.append(Reglas(i+2, j-1))
    if posValida(M, i+1, j-2): L.append(Reglas(i+1, j-2))
    
    return L


def mejorReglaA(L, i, j) -> Reglas:
    return L.pop(0)

def mejorReglaB(L, i, j) -> Reglas:
    import sys
    men = sys.maxsize
    dist = 0
    posMen = 0
    i = 0
    while i < len(L):
        dist = distancia(L[i].fil, L[i].col, i, j)
        if dist < men:
            men = dist
            posMen = i
        i +=1
    return L.pop(posMen)

