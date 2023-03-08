dias = int(input())
ano = dias / 365
mes = (dias % 365) / 30
dia = (dias % 365) % 30
print('%i ano (s)\n%i mes (es)\n%i dia (s)'%(ano,mes,dia))