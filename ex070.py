# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
# vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

print('Loja Super Baratão')

total = totproduto = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))

    cont += 1

    total += preço

    if preço > 1000:
        totproduto += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break


print(f'A) Qual é o total gasto na compra? R${total:.2f}')
print(f'B) Quantos produtos custam mais de R$1000? {totproduto} produto(s)')
print(f'C) O produto mais barato custa R${menor:.2f} e ele é o {barato}')




