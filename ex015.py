# Programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por Km rodado.

d = int(input('Quantos dias alugados? '))

k = float(input('Quantos Km rodados? '))

t = (d * 60) + (k * 0.15)

print('O total a pagar é de R${:.2f}'.format(t))

# vd = d * 60
# vk = k * 0.15