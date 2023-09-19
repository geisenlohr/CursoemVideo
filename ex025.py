# Programa que verifique se a palavra Silva aparece no nome de uma pessoa

n = str(input('Qual é o seu nome completo: ')).strip()

print('Seu nome tem Silva? {}'.format('SILVA' in n.upper()))


# in é operador do Python, não é método


