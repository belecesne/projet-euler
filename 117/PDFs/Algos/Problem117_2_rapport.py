import time

def tetranacci(n):
    '''
    :param n: nombre de cases à remplir
    :return: nombre de possibilités pour remplir n-cases
    '''
    l = [0,0,0,1]
    for i in range(4,n + 4):
        l.append(l[i - 4] + l[i - 3] + l[i - 2] + l[i - 1])
    return l[n + 3]

nbTeste = int(input("Rentrez le nombre de case disponible : "))
begin = time.time()
print("Résultat au problème 117 avec", nbTeste, "comme entrée :", tetranacci(nbTeste))
print(f"Duration = {time.time() - begin} seconds to complete.")