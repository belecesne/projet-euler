def gcd(a, b):
    while b > 1:
        temp = b
        b = a % b
        a = temp
    if b == 1:
        return 1
    return a

def G(a,b):
    max = 0
    n = 0
    while n < 1000000:
        temp = gcd(n**3 + b, (n+a)**3 + b)
        if temp > max:
            max = temp
            nMax = n
        n += 1
    return max

def H(m,n):
    sum = 0
    compt = 0
    for a in range(1,m+1):
        for b in range(1,m+1):
            compt += 1
            print(compt)
            sum += G(a,b)
    return sum


print(H(10,10))