# Programa que leia as duas notas de um aluno e calcule a média aritmética

n1 = float(input('Qual a 1ª nota: '))
n2 = float(input('Qual a 2ª nota: '))

print('A 1ª nota é {} e a 2ª nota é {}. A média do aluno é {:.1f}'. format(n1, n2, (n1+n2)/2))
