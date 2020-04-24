from math import floor, log, exp, ceil
import time

def sommeChiffreNombre(nombre):
    """
    Renvoie la somme des chiffres du nombre passé en paramètres
    """
    return sum([ int(c) for c in str(nombre) ])


def A(n, vMax):
    """
    Retourne le n-ème terme répondant aux critères du problème
    """
    listeNombre = []
    bMaximum = 2
    aMaximum = 2
    listebMaximum = {}
    while len(listeNombre) < n:
        a = 2
        aPrevious = aMaximum
        aMaximum = exp(log(vMax)/2)
        while a < aMaximum:
            if a >= aPrevious:
                bMinimum = 2
            else:
                bMinimum = listebMaximum[a]
            value = a
            bMaximum = floor(log(vMax) / log(a))+1
            listebMaximum[a] = bMaximum
            for b in range(bMinimum, bMaximum):
                value = a**b
                if sommeChiffreNombre(value) == a:
                    listeNombre.append(value)
            a += 1
        vMax *= 5**ceil((n - len(listeNombre))/2)
    listeNombre.sort()
    return listeNombre[n-1]


nbTeste = int(input("Rentrez le n-ème terme que vous souhaitez obtenir : "))
vTeste = int(input("Rentrez votre 'vMax' : "))
begin = time.time()
print("Résultat au problème 119 avec", nbTeste, "comme entrée :", A(nbTeste, vTeste))
print(f"Duration = {time.time() - begin} seconds to complete.")