import time

def finale(n):
    '''
    :param n: nombre de cases à remplir
    :return: nombre de possibilités pour remplir n-cases
    '''
    a, b, c, d = 0, 0, 0, 1
    for i in range(n):
        a, b, c, d = b, c, d, (a+b+c+d)
    return d

nbTeste = int(input("Rentrez le nombre de case disponible : "))
begin = time.time()
print("Résultat au problème 117 avec", nbTeste, "comme entrée :", finale(nbTeste))
print(f"Duration = {time.time() - begin} seconds to complete.")
