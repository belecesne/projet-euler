from math import floor
import time

def sommeChiffreNombre(nombre):
    '''
    :param nombre: nombre à décomposer
    :return: somme des chiffres de nombre
    '''
    somme = 0
    while (nombre != 0):            # tant qu'il reste des chiffres à ajouter à la somme
        somme += nombre%10          # on ajoute le dernier chiffre
        nombre=floor(nombre/10)     # puis on l'enlève du nombre
    return somme


def A(max):
    '''
    :param max: terme dont on cherche la valeur
    :return: max-ème terme répondant aux critères du problème
    '''
    index = 0
    nombreAct = 10
    valeurRetournee = 0
    while index != max:                                 # tant qu'on a pas trouvé le nombre que l'on recherche
        decomposition = sommeChiffreNombre(nombreAct)   # on effectue la somme de ses chiffres
        k = 2
        if decomposition != 1:                          # si "decomposition" est égale à 1 (que le nombre de départ était 10, 100, 1000, ...) c'est
            while 1:                                    # certain que ce nombre ne fonctionne pas
                puiss = decomposition**k                # on élève "decomposition" à la puissance "k"
                if puiss == nombreAct:                  # si le nombre obtenu est égal au nombre de départ alors on a trouvé un nombre de plus répondant
                    index += 1                          # aux critères
                    valeurRetournee = nombreAct         # on stocke ce nombre ci
                    break
                if puiss > nombreAct:                   # si "decomposition ** k" est supérieur au nombre de départ, alors ce nombre ne pourra jamais
                    break                               # répondre aux critères du problèmes
                k += 1
        nombreAct += 1
    return valeurRetournee


nbTeste = int(input("Rentrez le n-ème terme que vous souhaitez obtenir : "))
begin = time.time()
print("Résultat au problème 119 avec", nbTeste, "comme entrée :", A(nbTeste))
print(f"Duration = {time.time() - begin} seconds to complete.")