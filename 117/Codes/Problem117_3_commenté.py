import time

def finale(n):
    '''
    :param n: nombre de cases à remplir
    :return: nombre de possibilités pour remplir n-cases
    '''
    a, b, c, d = 0, 0, 0, 1 # déclaration et initialisation de 4 variables dont les 3 premières sont égales à 0 et la dernière correspond à tetranacci(0)
    for i in range(n):
        a, b, c, d = b, c, d, (a+b+c+d) # a, b et c sont des valeurs intermédiares, d correspond à tetranacci(i)
    return d

nbTeste = int(input("Rentrez le nombre de case disponible : "))
begin = time.time()
print("Résultat au problème 117 avec", nbTeste, "comme entrée :", finale(nbTeste))
print(f"Duration = {time.time() - begin} seconds to complete.")