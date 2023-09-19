# Índice de Massa Corporal
# Peso (em kg) / altura² (em metros).

'''
IMC	Classificação
Menor que 18,5	Magreza
18,5 a 24,9	Normal
25 a 29,9	Sobrepeso
30 a 34,9	Obesidade grau I
35 a 39,9	Obesidade grau II
Maior que 40	Obesidade grau III '''

p = float(input('Qual seu peso? (Kg) '))
a = float(input('Qual sua altura? (m) '))
imc = p / (a ** 2)

print('O IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO do peso! MAGREZA')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 35:
    print('Você está em OBESIDADE grau I!')
elif 35 <= imc < 40:
    print('Você está em OBESIDADE grau II!')
else:
    print('Você está em OBESIDADE MÓRBIDA! Cuidado!')










