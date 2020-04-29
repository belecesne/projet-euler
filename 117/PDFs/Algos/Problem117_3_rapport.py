import time
import math

def finale(n):
    '''
    :param n: nombre de cases à remplir
    :return: nombre de possibilités pour remplir n-cases
    '''
    a, b, c, d = 0, 0, 0, 1
    for i in range(n):
        a, b, c, d = b, c, d, (a+b+c+d)
    return d

def f(n):
    if n == 0: return [0, 0, 0, 1]
    else:
        s = f(n-1)
        return [s[1], s[2], s[3], s[0] + s[1] + s[2] + s[3]]

nbTeste = int(input("Rentrez le nombre de case disponible : "))
begin = time.time()
print("Résultat au problème 117 avec", nbTeste, "comme entrée :", finale(nbTeste))
print(f"Duration = {time.time() - begin} seconds to complete.")

print(108681103392592 - 52298426843184)