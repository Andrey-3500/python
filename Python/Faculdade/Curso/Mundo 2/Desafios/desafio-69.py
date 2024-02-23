
cont = mais18 = homens = mulhermenor = 0
sexo = ' '
while True:

    print('-' * 30,
          '\nCADASTRE UMA PESSOA')
    print('-' * 30)

    idade = int(input('Idade: '))

    if idade > 18:
        mais18 += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo [M/F]: ')).upper().strip()[0]

    cont += 1

    if sexo == 'M':
        homens += 1

    elif sexo == 'F' and idade < 20:
        mulhermenor += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]

    if resposta == 'N':
        break

print('-'*12,'Fim do programa','-'*12)
print(f'Total de pessoas com mais de 18 anos: {mais18}\n '
      f'Ao todo temos {homens} homens cadastrados\n'
      f' E temos {mulhermenor} mulheres com 20 anos ou menos')