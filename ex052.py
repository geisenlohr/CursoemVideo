# Números primos (quando ele é divisível por 1 e por ele mesmo = até duas vezes é primo)

n = int(input('\nDigite um número: '))

tot = 0

for c in range(1, n+1):
    if n % c == 0:
        tot += 1
        print('\033[33m', end=' ')                                               # não primo

    else:
        print('\033[31m', end=' ')                                               # primo
    print('{}'.format(c), end=' ')

print('\n\n\033[mO número {} foi dividido {} vez(es).'.format(n, tot))
if tot == 2:                                                                     # até duas vezes é primo
    print('\nE por isso o número {} é \033[33mPRIMO\033[m!'.format(n))
else:
    print('\nE por isso o número {} \033[31mNÃO É PRIMO\033[m!'.format(n))
