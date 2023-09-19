# Crie um algoritmo que leia um número e mostre o seu Dobro, Triplo, Raiz Quadrada

n = int(input('O número é: '))

print('O dobro do número {} é {}. \nO triplo é {} e sua raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))

# d = n * 2
# t = n * 3
# r = n ** (1/2) --> vai calcular primeiro o valor entre parênteses e depois a potência (ver ordem de precedência)
# pow(n, (1/2))


