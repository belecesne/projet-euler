from math import floor, log, exp, ceil
import time, sys

#Renvoie la somme des chiffres qui composent un nombre
def sommeChiffreNombre(nombre):
    return sum([ int(c) for c in str(nombre) ])


def A(n, vMax):
    vMaxOrigine = vMax
    listeNombre = []
    arret = 2
    aMax = 2
    listeArret = {}
    while len(listeNombre) < n:
        a = 2
        aAv = aMax
        aMax = exp(log(vMax)/2)
        while a < aMax:
            if a >= aAv:
                debut = 2
            else:
                debut = listeArret[a]
            value = a
            arret = floor(log(vMax) / log(a))+1
            listeArret[a] = arret
            for b in range(debut, arret):
                value = a**b
                if sommeChiffreNombre(value) == a:   # Si b est la somme des chiffres de value alors value est un des nombres qui nous intéresse
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


'''
for nbTeste in range(1, 31):
    begin = time.time()
    print("Résultat au problème 119 avec", nbTeste, "comme entrée :", A(nbTeste, vTeste))
    print(f"Duration = {time.time() - begin} seconds to complete.")
    print("#"*30)
'''