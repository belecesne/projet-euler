import random

def chase(n):
    pot = 0
    for i in range(n-2):
        s = 0
        j1 = random.randint(0,n-i-1)
        j2 = random.randint(0,n-i-1)
        while(j1 != j2):
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            if(d1 < 3):
                j1 = (j1 - 1) % (n - i - 1)
            elif(d1 > 4):
                j1 = (j1 + 1) % (n - i -1)
            if(d2 < 3):
                j2 = (j2 - 1) % (n - i - 1)
            elif(d2 > 4):
                j2 = (j2 + 1) % (n - i -1)
            s += 1
        pot += s * s
    return pot






