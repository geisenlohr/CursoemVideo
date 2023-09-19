# Programa q leia um ângulo qq e mostre na tela o valor seno (eixo vertical), cosseno (eixo horizontal)
# e tangente desse ângulo. A dificuldade foi converter radianos

from math import radians, cos, sin, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))

print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))

print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))

''' Maneira alternativa (acima)
from math radians, sin, cos, tan
tirar todas as referências math

ou uma maneira mais tradicional
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))

print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))

print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))
'''