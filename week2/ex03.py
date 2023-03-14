casos = int(input())

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

for x in range(casos):
    valores = input()
    f1 = int(valores.split()[0])
    f2 = int(valores.split()[1])
    print(mdc(f1,f2))