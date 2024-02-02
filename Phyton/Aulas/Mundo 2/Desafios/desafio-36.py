casa = float(input('Valor da casa: R$'))

sal = float(input('Salário do comprador: R$'))

anos = int(input('Quantos anos de financiamento? '))

prest = casa/(anos * 12)

par = (sal * 30/100)

print('para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prest))

if prest <= par:
    print('Seu emprestimo foi CONCEDIDO!')
else:
    print('Seu emprestimo foi NEGADO!')