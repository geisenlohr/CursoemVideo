# Programa que lê 3 números e mostra qual é o maior e qual o menor

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3 

print('O menor valor digitado foi {}'.format(menor))

maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

print('O maior valor digitado foi {}'.format(maior))

'''
v = [v1, v2, v3]
print('O menor valor digitado foi {}'.format(min(v)))
print('O maior valor digitado foi {}'.format(max(v)))
'''


