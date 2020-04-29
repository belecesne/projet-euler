from math import floor, log, exp, ceil
import time

def sommeChiffreNombre(nombre):
    '''
    :param nombre: nombre à décomposer
    :return: somme des chiffres de nombre
    '''
    return sum([ int(c) for c in str(nombre) ])


def A(n, vMax):
    '''
    :param n: terme dont on cherche la valeur
    :param vMax: variable permettant de borner a et b
    :return: n-ème terme répondant aux critères du problème
    '''
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