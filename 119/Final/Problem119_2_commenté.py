from math import floor, log, exp, ceil
import time

def sommeChiffreNombre(nombre):
    '''
    :param nombre: nombre à décomposer
    :return: somme des chiffres de nombre
    '''
    return sum([ int(c) for c in str(nombre) ])        # transforme le nombre en chaîne de caractères pour en faire la somme
                                                       # de ses caractères


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
    while len(listeNombre) < n:                        # tant qu'on a pas trouvé le nombre que l'on recherche
        '''
        aPrevious, aMaximum, bMinimum, bMaximum et listebMaximum sont des outils nous permettant d'incrémenter vMax sans avoir à tout re-tester. En effet lorsque vMax est changé il faut retester sur les anciens a, les nouvelles puissances. Cependant sur les nouveaux a il faut tester toutes les puissances possibles. C'est pourquoi nous avons besoin de ces outils. Il n'est donc pas nécessaire ici d'expliquer en détail comment ils sont manipulés. Ainsi, nous ne détaillerons pas les opérations impliquant ces variables.
        '''
        a = 2
        aPrevious = aMaximum
        aMaximum = exp(log(vMax)/2)                    # on borne "a" grâce à la valeur minimum que "b" peut prendre (2) et grâce à "vMax"
        while a < aMaximum:                            # et on teste ainsi tous les "a" possibles
            if a >= aPrevious:
                bMinimum = 2
            else:
                bMinimum = listebMaximum[a]
            bMaximum = floor(log(vMax) / log(a))+1     # on borne "b" (les puissances) en fonction de "a"
            listebMaximum[a] = bMaximum
            for b in range(bMinimum, bMaximum):        # ainsi pour chaque "a" on fait varier les puissances
                value = a**b                           # et on stocke dans "value"
                if sommeChiffreNombre(value) == a:     # Si "a" est la somme des chiffres de "value" alors "value" est un des nombres qui nous intéresse
                    listeNombre.append(value)          # on l'ajoute donc à notre liste
            a += 1
        vMax *= 5**ceil((n - len(listeNombre))/2)      # on augmente "vMax" en fonction de la taille de la liste
    listeNombre.sort()                                 # on trie la liste afin d'obtenir le bon terme recherché
    return listeNombre[n-1]


nbTeste = int(input("Rentrez le n-ème terme que vous souhaitez obtenir : "))
vTeste = int(input("Rentrez votre 'vMax' : "))
begin = time.time()
print("Résultat au problème 119 avec", nbTeste, "comme entrée :", A(nbTeste, vTeste))
print(f"Duration = {time.time() - begin} seconds to complete.")