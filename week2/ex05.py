triangulo = input()
aux = triangulo.split()
valores = [float(val) for val in aux]
order = sorted(valores, reverse=True)

a = float(order[0])
b = float(order[1])
c = float(order[2])

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == (b**2 + c**2):
        print('TRIANGULO RETANGULO')
    if a**2 > (b**2 + c**2):
        print('TRIANGULO OBTUSANGULO')
    if a**2 < (b**2 + c**2):
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')

