u0 = 1
u1 = 2
nextU = 0
sum = 0
while u1 < 4000000 :
    if u1 % 2 == 0:
        sum += u1
    nextU = u0 + u1
    u0 = u1
    u1 = nextU
print(sum)