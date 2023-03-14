valores = input()
a = float(valores.split()[0])
b = float(valores.split()[1])
c = float(valores.split()[2])
pi = 3.14159

print('TRIANGULO: %.3f'%((a*c)/2))
print('CIRCULO: %.3f'%(pi*c**2))
print('TRAPEZIO: %.3f'%(((a+b)*c)/2))
print('QUADRADO: %.3f'%(b*b))
print('RETANGULO: %.3f'%(a*b))
