# Programa que leia nome de uma cidade e que diga se ela começa com 'Santo' (True / False)

c = str(input('Em que cidade você nasceu?')).strip()

print(c[:5].upper() == 'SANTO')


'''
c = str(input('Em que cidade você nasceu?')).strip()

print(c[:5] == 'Santo') ---> mas tem prolemas, pois qq diferença ele dá como false
print(('Santo' in c)) ---> dá false se digitar maiúscula

print(c[:5].upper() == 'SANTO') ---> aqui o programdor joga tudo para maiúscula, fazendo o programa ler assim
automaticamente

# in é operador do Python, não é método

'''

