# Gerenciador de Pagamentos:
# à vista dinheiro/cheque: 10% desconto
# à vista cartão: 5% desconto
# 2x no cartão: preço normal
# 3x no cartão: 20% de juros

print('\n{:=^40}'.format(' GuiStore '))

preço = float(input('Preço das compras: R$'))

print('''\nFormas de pagamento:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou + no cartão''')

opção = int(input('\nQual é a opção? '))
print("\nO valor do item é {}".format(preço))

if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('\nSua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    parcelas = int(input('\nQuantas parcelas? '))
    parcela = total / parcelas
    print('\nSua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, parcela))
else:
    preço = 0
    total = 0
    print('Opção inválida!')
print('\nSua compra de R${:.2f} vai custar R${} no final'.format(preço, total))


print('\n{:=^40}'.format(' GuiStore '))










