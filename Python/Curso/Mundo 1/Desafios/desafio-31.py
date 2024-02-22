d = float(input('Digite a distancia da sua viagem: '))
print('Você está prestes a começar uma viagem de {}Km.'.format(d))
if d <= 200:
    print('O valor da sua passagen será R${:.2f}'.format(d*0.5))
else:
    print('O valor da sua passagen será R${:.2f}'.format(d*0.45))