def survivor(n, k):

    tnk = 0

    for i in range(n):
        i+= 1
        tnk = (tnk + k) % i

    return tnk

while(1):
    n = int(input())
    k = 1
    while(survivor(n,k)+2 != 13):
        k+= 1
        print(k)
        
