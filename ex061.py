# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while

print('Gerador de P.A.')
print('=' *40)
t = int(input('Termo: '))
r = int(input('Razão: '))
termo = t
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')

