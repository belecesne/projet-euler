def recursive(n):
    '''
    :param n: nombre de cases à remplir
    :return: nombre de possibilités pour remplir n-cases
    '''
    if n == 5:
        return 15
    elif n == 4:
        return 8
    elif n == 3:
        return 4
    elif n == 2:
        return 2
    return recursive(n - 1) + recursive(n - 2) + recursive(n - 3) + recursive(n - 4)

nbTeste = int(input("Rentrez le nombre de case disponible : "))
print("Résultat au problème 117 avec", nbTeste, "comme entrée :", recursive(nbTeste))