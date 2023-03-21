entrada = ''
while entrada != '0 0 0 0':
    entrada = input()
    if entrada == '0 0 0 0':
        break

    x1 = int(entrada.split()[0])
    y1 = int(entrada.split()[1])
    x2 = int(entrada.split()[2])
    y2 = int(entrada.split()[3])

    casas = 0
    if x1 == x2 and y1 == y2:
        casas = 0
    else:
        if (x1 - x2) == 0 or (y1 - y2) == 0:
            casas = 1
        elif abs(x1 - x2) == abs(y1 - y2):
            casas = 1 
        elif x1 != x2 and y1 != y2:
            casas = 2

    print(casas)