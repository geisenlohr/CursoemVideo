# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de P.A.')
print('=' *40)
t = int(input('Termo: '))
r = int(input('Razão: '))

termo = t
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim!')
print('Progressão finalizada com {} termos mostrados'.format(total))

'''if termo != 0:
    print('{} -> '.format(termo), end=' ')
    termo += r
    cont += 1
else:
    print('Fim')
print('Fim')'''