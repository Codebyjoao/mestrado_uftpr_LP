'''
N = numero de regioes
m = salto
1 = Auckland 
13 = wellington
'''
entrada  = 1
while entrada != 0:
    entrada  = int(input())
    if entrada == 0:
        break
    def josephus(n, k):
        regioes = list(range(1, n+1))
        index = 0
        while len(regioes) > 1:
            index = (index + k - 1) % len(regioes)
            regioes.pop(index)
        return regioes[0]

    print(josephus(entrada, 7))

