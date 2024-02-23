print('='*8,'LOJAS GUANABARA','='*8)

valor = float(input('Preço da compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[1] á vista Dinheiro / Cheque')
print('[2] á vista cartão')
print('[3] 2x no cartão')
print('[4] 3x até 12x')
op = int(input('Qual seria a opção? '))

if op == 1:
    valor2 = valor - (valor*10/100)
    print('A sua compra de R${:.2f} vai custar R${:.2f}'.format(valor, valor2))

elif op == 2:
    valor2 = valor - (valor*5/100)
    print('A sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, valor2))

elif op == 3:
    print('Sua compra será parcelada 2x de R${:.2f} sem JUROS'.format(valor/2))
    print('A sua compra vai custar R${:.2f}'.format(valor))

elif op == 4:
    np = int(input('Quantas parcelas? '))

    valor2 = valor + (valor * 20/100)
    print('Sua compra será parcelada {}x de R${:.2f} COM JUROS'.format(np, (valor2/np)))
    print('A sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, valor2))
else:
    print('OPÇÃO INVALIDA! tente novamente!')
