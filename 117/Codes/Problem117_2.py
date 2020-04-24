def tetranacci(n):
    l = [0,0,0,1]      # déclaration et initialisation d'une liste dont les 3 premières valeurs sont à 0 et la dernière correspond à tetranacci(0)
    for i in range(4,n + 4):
        l.append(l[i - 4] + l[i - 3] + l[i - 2] + l[i - 1]) # ajout de la somme des 4 termes précédents
    return l[n + 3]

print(tetranacci(50))