# Pedra, Papel e Tesoura

from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
pc = randint(0, 2)

print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual a sua jogada? '))
print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura...')
sleep(1)

print('-'*20)

print('O PC jogou {}'.format(itens[pc]))
print('O jogador jogou {}'.format(itens[jogador]))

print('-'*20)

if pc == 0: # PC jogou PEDRA
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador ganhou!')
    elif jogador == 2:
        print('PC ganhou')
    else:
        print('Jogada inválida!')
elif pc == 1: # PC jogou PAPEL
    if jogador == 0:
        print('PC ganhou')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador ganhou')
    else:
        print('Jogada inválida!')
elif pc == 2: # PC jogou TESOURA
    if jogador == 0:
        print('Jogador ganhou')
    elif jogador == 1:
        print('PC ganhou')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')