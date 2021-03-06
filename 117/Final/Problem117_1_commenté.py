import time

def recursive(n):    # 1ère méthode
    '''
    :param n: nombre de cases à remplir
    :return: nombre de possibilités pour remplir n-cases
    '''
    if n == 5:       # 4 cas d'arrêts : 5, 4, 3 et 2 dont on connait les résultats
        return 15
    elif n == 4:
        return 8
    elif n == 3:
        return 4
    elif n == 2:
        return 2
    return recursive(n - 1) + recursive(n - 2) + recursive(n - 3) + recursive(n - 4)    # récursion sur les 4 précédents

nbTeste = int(input("Rentrez le nombre de case disponible : "))
begin = time.time()
print("Résultat au problème 117 avec", nbTeste, "comme entrée :", recursive(nbTeste))
print(f"Duration = {time.time() - begin} seconds to complete.")