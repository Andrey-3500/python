v = float(input('Qual a velocidade do carro?'))
if v > 80:
    print("MULTADO Você exedeu o limite permitido é de 80km/h")
    print('Sua multa é de R${:.2f}'.format((v-80)*7))
print('Tenha um bom dia! Dirija com cuidado!')