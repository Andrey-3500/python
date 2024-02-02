num = cont = soma = maior = menor = 0
resposta = 'S'

while resposta == 'S':

    num = int(input('Digite um nùmero\n>> '))
    soma += num

    cont += 1
    resposta = str(input('Quer continuar [S/N] \n >> ')).upper().strip()[0]

    if resposta == 'S':

        if cont == 1:
             maior = menor = num

        elif maior < num:
             maior = num

        elif menor > num:
             menor = num

print('Você digitou {} nùmeros e a média entre eles é {:.1f}'.format(cont, soma/cont))
print('O menor número digitado foi {} e o maior foi {}'.format(menor, maior))
