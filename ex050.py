# Soma dos pares = ler 6 nº inteiros e mostre a soma apenas dos que forem pares. se o valor digitado for ímpar, desconsidere


soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num          # soma += num
        cont = cont + 1            # cont += 1
print('Você informou {} nº PARES e a soma foi {}'.format(cont, soma))

