# Programa Radar eletrônico de até 80Km/h. Se passar, multa de R$7,00 por km acima do limite


velocidade = float(input('Qual a velocidade atual de um carro? '))
multa = 7 * (velocidade - 80)

if velocidade > 80:
    print('Excesso de velocidade! Multado! Você tem pagar R$ {:.2f} de multa!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
