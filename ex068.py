# Faça um programa que jogue par ou ímpar com o PC. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0

print('Vamos jogar par ou ímpar')

while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o PC jogou {pc}. Total de {total}.', end=' ')
    print('Deu PAR!!!' if total % 2 == 0 else 'Deu ÍMPAR!!!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você ganhou {v} vez(es).')









