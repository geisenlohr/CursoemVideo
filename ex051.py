# Progressão Aritmética

print('=' *40)
print('10 TERMOS DE UMA P.A.')
print('=' *40)

t = int(input('Termo: '))
r = int(input('Razão: '))
d = t + (10 - 1) * r

for c in range(t, d + r, r):
    print('{}'.format(c), end=" --> ")
print('Fim!')


# const = t + 1