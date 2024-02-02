peso = float(input('Qual é seu peso? (Kg): '))
altura = float(input('Qual sua altura? (M): '))

imc = peso / (altura**2)

print('Seu imc é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso IDEAL!')
elif 25 <= imc < 30:
    print('Você está com SOBRE PESO!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!!')