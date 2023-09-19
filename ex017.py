''' Programa q leia comprimento do cateto opsoto e do cateto adjacente de uma triângulo retângulo
(um dos ângulos internos de 90º) e que mostre o comprimento da Hipotenusa --> hi = (co ** 2 + ca ** 2) ** (1/2)
(o quadrado da hipotenusa é igual a soma dos quadrados do catetos) '''

''' Maneira meramente matemática de resolver
co = float(input('\nComprimento do cateto oposto: '))
ca = float(input('\nComprimento do cateto adjacente: '))

hi = (co ** 2 + ca ** 2) ** (1/2)

print('\nA hipotenusa vai medir {:.2f}'.format(hi)) '''

''' Maneira 1 Python MELHOR!!!
from math import hypot
co = float(input('\nComprimento do cateto oposto: '))
ca = float(input('\nComprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('\nA hipotenusa vai medir {:.2f}'.format(hi))'''

'''# Maneira 2 Python
import math
co = float(input('\nComprimento do cateto oposto: '))
ca = float(input('\nComprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('\nA hipotenusa vai medir {:.2f}'.format(hi))'''

from math import hypot
co = float(input('\nComprimento do cateto oposto: '))
ca = float(input('\nComprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('\nA hipotenusa vai medir {:.2f}'.format(hi))