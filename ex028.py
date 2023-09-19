# Programa Jogo da Adivinhação v.1.0

from random import randint
from time import sleep

computador = randint(0 ,5) # faz o computador 'pensar'

print('-=-' * 20)
print('Vou pensar num número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar

print('Processando...')
sleep(2)

if jogador == computador:
    print('Parabéns, você GANHOU!!!')
else:
    print('Eitcha! Você perdeu! Eu pensei no número {} e não no número {}'.format(computador, jogador))




