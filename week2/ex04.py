'''
N = numero de regioes
m = salto
1 = Auckland 
13 = wellington
'''

regioes = int(input())

def salto(n): 
    m = [1]
    nsaltos = 0

    while nsaltos != 13:
        for j in range(n):
            j+= 1
            for i in range(n):
                i+= j
                print(i)
                m.append(i)
        nsaltos = m[-1]

    return nsaltos


print(salto(regioes))