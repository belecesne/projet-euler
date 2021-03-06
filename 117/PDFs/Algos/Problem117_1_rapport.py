import time

def recursive(n):
    '''
    :param n: nombre de cases à remplir
    :return: nombre de possibilités pour remplir n-cases
    '''
    if n == 5:
        return 15
    if n == 4:
        return 8
    if n == 3:
        return 4
    if n == 2:
        return 2
    return recursive(n - 1) + recursive(n - 2) + recursive(n - 3) + recursive(n - 4)

nbTeste = int(input("Rentrez le nombre de case disponible : "))
begin = time.time()
print("Résultat au problème 117 avec", nbTeste, "comme entrée :", recursive(nbTeste))
print(f"Duration = {time.time() - begin} seconds to complete.")