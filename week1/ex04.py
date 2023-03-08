valores = input()

a = int(valores.split()[0])
b = int(valores.split()[1])
c = int(valores.split()[2])

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c


maiorAB = (a + b + abs(a-b))/2
maiorABC = (maiorAB + c + abs(maiorAB-c)) /2

print('%i eh o maior' %(maiorABC))