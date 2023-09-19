# Jogo da Adivinhação v.2.0: Program que melhora o desafio 028 onde o PC vai "pensar" num nº entre 0 e 10.
# Só que agora vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer

from random import randint
from time import sleep

computador = randint(0, 10)

print('-=-' * 20)
print('Sou seu PC e vou pensar num número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente de novo! ')
        elif jogador > computador:
            print('Menos... solta mais uma vez... ')
print('Parabéns, você ganhou com tantas {} tentativas!'.format(palpites))


'''print('Foram necessários {} palpites até acertar'.format())'''





