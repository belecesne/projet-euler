def recursive2(n):
    if n == 0:
        return [0, 0, 0, 1]
    else:
        temp = recursive2(n-1)
        s3_next = temp[0] + temp[1] + temp[2] + temp[3]
        return [temp[1], temp[2], temp[3], s3_next]


nbTeste = int(input("Rentrez le nombre de case disponible : "))

result = recursive2(nbTeste)[3]
# car le résultat final se trouve dans la 4 "case" de la liste

print("Résultat au problème 117 avec", nbTeste, "comme entrée :", result)