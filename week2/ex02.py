dinheiro = int(input())

print(dinheiro)
print('%i nota(s) de R$ 100,00'%(dinheiro / 100) )
print('%i nota(s) de R$ 50,00'%((dinheiro % 100)/50))
print('%i nota(s) de R$ 20,00'%(((dinheiro % 100)% 50)/20))
print('%i nota(s) de R$ 10,00'%((((dinheiro % 100)% 50)%20)/10))
print('%i nota(s) de R$ 5,00'%(((((dinheiro % 100)% 50)%20)%10)/5))
print('%i nota(s) de R$ 2,00'%((((((dinheiro % 100)% 50)%20)%10)%5)/2))
print('%i nota(s) de R$ 1,00'%((((((dinheiro % 100)% 50)%20)%10)%5)%2))