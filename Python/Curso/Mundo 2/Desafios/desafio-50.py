soma = 0
cont = 0
for c in range (0, 6):
    c = int(input('Digite o {}ª valor: '.format(c+1)))
    if c % 2 == 0:
        soma = soma + c
        cont += 1
print('Você informou {} numeros pares e a soma desses valores foi {}'.format(cont, soma))