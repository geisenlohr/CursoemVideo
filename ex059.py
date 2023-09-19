# Programa que leia dois valores e mostre menu na tela:

'''
[1]somar
[2]multiplicador
[3]maior
[4]novos números
[5]sair do programa

Seu programa deverá realizar a operação solicitada em cada caso
'''

from time import sleep

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))

opção = 0

while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('>>>>>>>> Qual a sua opção? '))
    if opção == 1:
        s = v1 + v2
        print('A soma de {} e {} é {} '.format(v1, v2, s))
    elif opção == 2:
        m = v1 * v2
        print('A multiplicação de {} e {} é {}'.format(v1, v2, m))
    elif opção == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O maior número entre {} e {} é {}'.format(v1, v2, maior))
    elif opção == 4:
        print('Informa os números novamente')
        v1 = int(input('Digite um NOVO valor '))
        v2 = int(input('Digite outro NOVO valor '))
    elif opção == 5:
        print('Você saiu do programa! Tchau!')
    else:
        print('Opção inválida! Tente novamente!')
    print('=-='*20)
    sleep(2)
print('Fim do programa!')

