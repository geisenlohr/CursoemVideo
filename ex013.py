# Programa que mostra salário do funcionário e quanto recebe com 15% de aumento

s = float(input('Qual é o salário do funcionário? R$'))

n = s + (s * 15 / 100)

print('Um funcionário que ganhava R${} com 15% de aumento passa a receber R${}.'. format(s, n))



