# Aprovando Empréstimo para compra de casa. Prestação mensal não pode exceder 30% do salário do comprador.

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print('Para pagar uma casa de R${:.2f} em {:.2f} anos a prestação será de R$ {:.2f}'.format(casa, anos, prestação))

if prestação <= mínimo:
    print('Empréstimo APROVADO!')

else:
    print('Empréstimo NEGADO!')

