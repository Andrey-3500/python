from datetime import date
ano = date.today().year
qnt = 0
for c in range (0, 7):
        nasc = int(input('Digite o ano de nascimento: '))
        if ano - nasc >= 21:
                qnt += 1
print('{} pessoas já atingiram a maior idade e \n'
      '{} ainda não atigiram'.format(qnt, 7 - qnt))