# Análise completa de 4 pessoas/ média de idade / homem mais velho (idade e nome) / quantas mulheres com menos de 20 anos

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0

for p in range(1, 5):
    print('---- {}ª pessoa ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade/4
print('A média de idade do grupo é {}.'.format(médiaidade)) # somar tudo e dividir por 4
print('A idade do homem mais velho é {} e ele se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

