real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real/5.12
euro = real/5.55
print('Com R${} você pode comprar U${:.2f} \n ou pode comprar eur {:.2f}'.format(real, dolar, euro))