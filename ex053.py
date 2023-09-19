# Palíndromo
'''
Frases
A base do teto desaba.
A cara rajada da jararaca.
Acuda cadela da Leda caduca.
A dama admirou o rim da amada.
A Daniela ama a lei? Nada!
Adias a data da saída.
'''


frase = str(input('Digite uma frase: ')).strip().upper() # elimina espaços antes e depois

palavras = frase.split()     # divide a frase

junto = ''.join(palavras)    # elimina espaços internos, juntando tudo numa strig

inverso = junto[::-1]


if inverso == junto:
    print('Você digitou a frase {} que invertida é {}'.format(junto, inverso), end=' ')
    print('\nPalíndromo!')

else:
    print('Você digitou a frase {} que invertida é {}'.format(junto, inverso), end=' ')
    print('\nNão Palíndromo!')



'''
ou

inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''