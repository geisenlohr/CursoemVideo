# Alistamento Militar

from datetime import date

a = int(input('Ano de nascimento: '))

atual = date.today().year
idade = atual - a

if idade < 18:
    faltam = 18 - idade
    alistamento = a + 18
    print('Quem nasceu em {} e tem {} anos em {}.'.format(a, idade, atual))
    print('Ainda faltam {} anos para o alistamento.'.format(faltam))
    print('Seu alistamento será em {}'.format(alistamento))

elif idade == 18:
    print('CORRA! Você tem {} anos e deve se alistar IMEDIATAMENTE!'.format(idade))

else:
    deveria = idade - 18
    alistamento = a + 18
    print('Você já deveria ter se alistado há {} anos.'.format(deveria))
    print('Seu alistamento foi em {}.'.format(alistamento))



