def recursive(n):    # 1ère méthode
    if n == 5:       # 4 cas d'arrêts : 5, 4, 3 et 2 dont on connait les résultats
        return 15
    if n == 4:
        return 8
    if n == 3:
        return 4
    if n == 2:
        return 2
    return recursive(n - 1) + recursive(n - 2) + recursive(n - 3) + recursive(n - 4)    # récursion sur les 4 précédents

print(recursive(50))



