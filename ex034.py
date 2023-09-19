# Programa pergunta o salário do funcionário a calcula o valor do aumento.
# Salário superior a R$1.250,00 (10% de aumento)
# Salários inferiores ou iguais (15% de aumento)

salário = float(input('Qual o salário do funcionário? R$'))

if salário <= 1250:
    novo = (salário * 15/100) + salário
else:
    novo = (salário * 10/100) + salário

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário, novo))


