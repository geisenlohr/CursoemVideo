# Sorteando uma ordem da lista

from random import shuffle
a1 = str(input('1º aluno: '))
a2 = str(input('2º aluno: '))
a3 = str(input('3º aluno: '))
a4 = str(input('4º aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)


print('A ordem é {}: '.format(lista))

'''
from random import shuffle
e depois tirar menções a random

ou

import random
a1 = str(input('1º aluno: '))
a2 = str(input('2º aluno: '))
a3 = str(input('3º aluno: '))
a4 = str(input('4º aluno: '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)


print('A ordem é {}: '.format(lista))
'''
