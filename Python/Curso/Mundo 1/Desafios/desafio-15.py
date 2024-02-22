da = int(input('Quantos dias alugados? '))
kr = float(input('Quantos kms foram rodados? '))

pago = (da * 60) + (kr * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))
