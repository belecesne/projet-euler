import xlrd
import time

from xlwt import Workbook, Formula



def recursive(n):    # 1ère méthode
    '''
    :param n: nombre de cases à remplir
    :return: nombre de possibilités pour remplir n-cases
    '''
    if n == 5:       # 4 cas d'arrêts : 5, 4, 3 et 2 dont on connait les résultats
        return 15
    if n == 4:
        return 8
    if n == 3:
        return 4
    if n == 2:
        return 2
    if n == 1 or n == 0:
        return 1
    return recursive(n - 1) + recursive(n - 2) + recursive(n - 3) + recursive(n - 4)    # récursion sur les 4 précédents


def tetranacci(n):
    '''
    :param n: nombre de cases à remplir
    :return: nombre de possibilités pour remplir n-cases
    '''
    l = [0,0,0,1]      # déclaration et initialisation d'une liste dont les 3 premières valeurs sont à 0 et la dernière correspond à tetranacci(0)
    for i in range(4,n + 4): # les 3 premiers éléments de la liste ne font partie de la suite de tetranacci, c'est pourquoi on commence à 4
        l.append(l[i - 4] + l[i - 3] + l[i - 2] + l[i - 1]) # ajout de la somme des 4 termes précédents
    return l[n + 3] # retourne le dernier élément de la liste


def finale(n):
    '''
    :param n: nombre de cases à remplir
    :return: nombre de possibilités pour remplir n-cases
    '''
    a, b, c, d = 0, 0, 0, 1 # déclaration et initialisation de 4 variables dont les 3 premières sont égales à 0 et la dernière correspond à tetranacci(0)
    for i in range(n):
        a, b, c, d = b, c, d, (a+b+c+d) # a, b et c sont des valeurs intermédiares, d correspond à tetranacci(i)
    return d



path = r"E:\Explorateur de fichier\Documents\fichier.xls"

# On créer un "classeur"
classeur = Workbook()
# On ajoute une feuille au classeur
feuille = classeur.add_sheet("OCB")


for i in range (0, 37):
    begin = time.time()
    result = recursive(i)
    temps = time.time() - begin
    print("Résultat au problème 117 avec", i, "comme entrée :", result)
    print(f"Duration = {temps} seconds to complete.")
    feuille.write(i, 1, result)
    feuille.write(i, 2, temps)


for i in range (0, 1001):
    begin = time.time()
    result = tetranacci(i)
    temps = time.time() - begin
    print("Résultat au problème 117 avec", i, "comme entrée :", result)
    print(f"Duration = {temps} seconds to complete.")
    feuille.write(i, 3, result)
    feuille.write(i, 4, temps)

for i in range (0, 1001):
    begin = time.time()
    result = finale(i)
    temps = time.time() - begin
    print("Résultat au problème 117 avec", i, "comme entrée :", result)
    print(f"Duration = {temps} seconds to complete.")
    feuille.write(i, 0, i)
    feuille.write(i, 5, result)
    feuille.write(i, 6, temps)











classeur.save(path)
print(u"Fichier créé: {}".format(path))