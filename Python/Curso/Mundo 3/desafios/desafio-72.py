numeros = ('zero', 'um', 'dois', 'treis', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'deiz', 'onze',
           'doze', 'treze', 'quatorze ou catorze', 'Quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um nùmero entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('Tente novamente! ', end='')

    print(f'Você digitou o número {numeros[num]}')
