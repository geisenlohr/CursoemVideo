# Peso de 5 pessoas e qual o maior e menor peso lidos.

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg'.format(maior))
print('O menor peso foi de {}Kg'.format(menor))

