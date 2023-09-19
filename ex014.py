# Programa que converta temperatura digitada em ºC para ºF

c = float(input('Informe qual a temperatura em ºC: '))

f = c * 1.8 + 32          # ou ---> f = 9*c/5 + 32

print('A temperatura de {0}ºC corresponde a {1}ºF!'.format(c, f))