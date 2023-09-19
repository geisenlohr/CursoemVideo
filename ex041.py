#Classificando Atletas:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima: Master

from datetime import date

an = int(input('AN: '))

hj = date.today().year

idade = hj - an

if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: Mirim')

elif idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: Infantil')

elif idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: Junior')

elif idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: Sênior')

else:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: Master')


