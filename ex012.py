# Programa para mostrar preço de produto e mostre seu preço com desconto de 5%

p = float(input('Qual é o preço do produto? R$ '))

d = p * 5/100 # aqui eu calculo quanto é o desconto

pd = p - d # aqui eu calculo o valor - desconto

# np = preço - (preço * 5/100) ---> fórmula mais simples passada pelo Guanabara

print('O produto que custava R${} vai custar R${:.2f} com um desconto de 5%, que é de R${:.2f}'.format(p, pd, d))
