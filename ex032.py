# Programa que leia um ano e mostre se é bissexto ou não

from datetime import date
a = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year # comando para pegar ano atual confirgurado na máquina
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):   # o sinal != significa "diferente"
    print('O ano {} é Bissexto'.format(a))

else:
    print('O ano {} não é bissexto'.format(a))




