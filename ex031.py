# Programa Custo da Viagem (R$0,50 até 200Km / R$0,45 para outras viagens)

distância = float(input('Qual a distância da sua viagem? '))

preço1 = distância * 0.50
preço2 = distância * 0.45

if distância <= 200:
    print('Você está prestes a começar uma viagem de {}Km. \nE o preço da sua passagem é R${:.2f}'.format(distância, preço1))
else:
    print('Você está prestes a começar uma viagem de {}Km. \nE o preço da sua passagem é R${:.2f}'.format(distância, preço2))

'''
ou
preço = distância * 0.50 if distância <= 200 else distância * 0.45
'''







