# Programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

v = s = cont = 0

while True:
    v = int(input('Digite um valor [flag 999]: '))
    if v == 999:
        break
    s += v
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles é {s}')
