# Programa para ler quanto dinheiro tem na carteira e quantos dólares pode comprar

real = float(input('Quanto $$$ você tem na carteira? R$')) #
dólar = real / 4.87
# dólar = 4.87
# câmbio = real / dólar
print('Eu tenho R${} :D e posso comprar US${:.2f}'.format(real, dólar))
