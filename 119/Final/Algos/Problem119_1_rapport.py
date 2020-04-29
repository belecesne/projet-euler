from math import floor
import time

def sommeChiffreNombre(nombre):
    '''
    :param nombre: nombre à décomposer
    :return: somme des chiffres de nombre
    '''
    somme = 0
    while (nombre != 0):
        somme += nombre%10
        nombre=floor(nombre/10)
    return somme


def A(n):
    '''
    :param n: terme dont on cherche la valeur
    :return: n-ème terme répondant aux critères du problème
    '''
    index = 0
    nombreAct = 10
    valeurRetournee = 0
    while index != n:
        decomposition = sommeChiffreNombre(nombreAct)
        k = 2
        if decomposition != 1:
            while 1:
                puiss = decomposition**k
                if puiss == nombreAct:
                    index += 1
                    valeurRetournee = nombreAct
                    break
                if puiss > nombreAct:
                    break
                k += 1
        nombreAct += 1
    return valeurRetournee



nbTeste = int(input("Rentrez le n-ème terme recherché : "))
begin = time.time()
print("Résultat au problème 119 avec", nbTeste, "comme entrée :", A(nbTeste))
print(f"Duration = {time.time() - begin} seconds to complete.")