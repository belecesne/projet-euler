def finale(n):
    '''
    :param n: nombre de cases à remplir
    :return: nombre de possibilités pour remplir n-cases
    '''
    a, b, c, d = 0, 0, 0, 1
    for _ in range(n):
        a, b, c, d = b, c, d, (a+b+c+d)
    return d

print(finale(50))