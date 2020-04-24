from math import floor
import time

def sommeChiffreNombre(nombre):
    """
    Renvoie la somme des chiffres du nombre passé en paramètres
    """
    somme = 0
    while (nombre != 0):            # tant qu'il reste des chiffres à ajouter à la somme
        somme += nombre%10          # on ajoute le dernier chiffre
        nombre=floor(nombre/10)     # puis on l'enlève du nombre
    return somme


def A(max):
    """
    Retourne le n-ème terme répondant aux critères du problème
    """
    index = 0
    nombreAct = 10
    valeurRetournee = 0
    while index != max:       # tant qu'on a pas trouvé le nombre que l'on recherche
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


nbTeste = int(input("Rentrez le n-ème terme que vous souhaitez obtenir : "))
begin = time.time()
print("Résultat au problème 119 avec", nbTeste, "comme entrée :", A(nbTeste))
print(f"Duration = {time.time() - begin} seconds to complete.")