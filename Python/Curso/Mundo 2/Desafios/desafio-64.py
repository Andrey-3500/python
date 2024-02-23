num = 0
cont = 0
soma = 0
while num != '999':

    num = int(input('Digite um nùmero  [999 para parar] \n >> '))
    cont += 1
    if num == 999:
        break
    else:
        soma = soma + num

print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
