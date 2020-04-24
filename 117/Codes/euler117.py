def numberOfWays(n):
    if n == 5:
        return 15
    if n == 4:
        return 8
    if n == 3:
        return 3
    if n == 2:
        return 1
    return numberOfWays(n - 1) + numberOfWays(n - 2) + numberOfWays(n - 3) + numberOfWays(n - 4)

def number(n):
    dico = {}
    dico[5] = [15, 1, 2, 4, 8]
    dico[4] = [8, 1, 2, 4, 7]
    dico[3] = [3, 1, 2, 3, 6]
    dico[2] = [1, 1, 1, 2, 4]
    if n < 6:
        return dico[n][0]
    elif n < 10:
        return dico[2][n - 5] + dico[3][n - 5] * 3 + dico[4][n - 5] * 8 + dico[5][n - 5] * 15
    else:
        for i in range(10,n + 1):
            for j in range(2,6):
                dico[j].append(dico[j][i - 6] + dico[j][i - 7] + dico[j][i - 8] + dico[j][i - 9])
        print(dico[2])
        return dico[2][n - 5] + dico[3][n - 5] * 3 + dico[4][n - 5] * 8 + dico[5][n - 5] * 15



#print(numberOfWays(7))
print(number(12))



