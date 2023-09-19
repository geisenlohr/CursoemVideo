# Soma de ímpares múltiplos de três no intervalo de 1 a 500
# A soma de todos os 83 valores solicitados é 2067? SIM!

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1                # o nome disso é contador == soma 1 // cont += 1
        soma = soma + c                # o nome disso é acumulador == soma valor // soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
