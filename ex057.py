# Programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter uma valor correto

# .upper()[0] --> corta espaços no início

sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]
s1 = 'F'
s2 = 'M'
while sexo != s1 and sexo != s2:
    sexo = str(input('Dados inválidos. Digite o seu sexo novamente: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

'''
código do professor:

while sexo not in 'MmFf':
     sexo = str(input('Dados inválidos. Digite o seu sexo novamente: [M/F] ')).strip().upper()[0]
'''








