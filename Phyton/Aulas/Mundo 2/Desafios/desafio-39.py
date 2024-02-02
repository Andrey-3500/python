from datetime import date

nasc = int(input('ano de nascimento: '))

ano = date.today().year

idade = ano - nasc

print('Quem nasceu em {} completa {} em {}'.format(nasc, idade, ano))

alis = (idade - 18)

if idade == 18:
    print('Você terá que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Você irá se alistar em {}'.format(ano + saldo))

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano - saldo))
