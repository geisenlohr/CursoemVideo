# Clássico da Média

n1 = float(input('1ª Nota: '))
n2 = float(input('2ª Nota: '))

m = (n1 + n2) / 2

if m >= 7.0:
    print('APROVADO!')
    print('Sua média é {:.1f}'.format(m))
elif m >= 5.0 and m < 7:               # ou pode escrever assim -- if 7 > m >= 5
    print('RECUPERAÇÃO!')
    print('Sua média é {:.1f}'.format(m))
else:
    print('REPROVADO!')
    print('Sua média é {:.1f}'.format(m))
