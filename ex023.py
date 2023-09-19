# Programa para contar de 0 a 9999 unidade, dezena, centena, milhar:

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))


'''
Pra quem achou a explicação complicada:
Veja os exemplos abaixo.
Divisão: 1234 / 10 = 123,4
Divisão inteira: 1234 //10 = 123
Módulo: 1234 % 10 = 4
Pra ele descobrir a centena ele faz isso:
Faz a divisão inteira por 100: 1234 // 100 = 12
Depois pega o resultado e dividi por 10, mas pega só o resto dessa divisão (que é o módulo): 12 % 10 = 2
Ou seja, a centena é 2.
'''
'''
num = int(input('Informe um número: ')) #número inteiro
n = str(num) #string

print('Analisando o número {}'.format(num))

print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
'''




