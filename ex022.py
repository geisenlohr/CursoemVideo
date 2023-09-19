#Programa para ler nome completo, com letras maiúsculas, minúsculas e quantas letras têm o primeiro nome
# - nome.count(' ') --> Elimina contagem de espaços entre palavras
# .strip() --> em uma cadeia de caracteres para eliminar contagem de espaços antes e depois

nome = str(input('Digite seu nome completo: ')).strip()

dividido = nome.split()

print('Analisando seu nome...')

print('Seu nome com maiúsculas é {}'.format(nome.upper()))
print('Seu nome com minúsculas é {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0],len(dividido[0])))

# print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.find(' ')))

# João da Silva Moura
# Guilherme Frederico de Carvalho Eisenlohr
# Ana Maria



