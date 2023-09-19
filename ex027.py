# Programa q lê nome completo de pessoa e mostre em seguida o primeiro e último nome separadamente

n = str(input('Digite seu nome completo: ')).strip()

nome = n.split()

print('Seu 1º nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))


# Guilherme Frederico de Carvalho Eisenlohr