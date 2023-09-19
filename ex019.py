# Sorteio de alunos ---> lista no python usar [] ---> nível fácil-médio

from random import choice
a1 = input('1º aluno: ')
a2 = input('2º aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')

lista = [a1, a2, a3, a4]
ordem = choice(lista)


print('O aluno escolhido foi {}'.format(ordem))

''' método 1
import random
a1 = input('1º aluno: ')
a2 = input('2º aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)


print('O aluno escolhido foi {}'.format(escolhido))


ou método 2
from random import choice
a1 = input('1º aluno: ')
a2 = input('2º aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')

lista = [a1, a2, a3, a4]
escolhido = choice(lista)


print('O aluno escolhido foi {}'.format(escolhido))

'''
