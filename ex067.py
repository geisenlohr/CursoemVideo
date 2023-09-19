# Faça um programa que mostre uma tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo
# ex009.py e ex049.py

num = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-='*30)
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num*cont}')
    print('-=' * 30)
print('Programa encerrado!')








