# Programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar
# No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

print('Cadastre uma pessoa')
tot18 = tothomens = totmulher20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()[0].strip()
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomens += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    if resp == 'N':
        break
print(f'A) Total de pessoas com mais de 18 anos: {tot18}')
print(f'B) Quantos homens foram cadastrados: {tothomens}')
print(f'C) Quantas mulheres têm menos de 20 anos: {totmulher20}')
