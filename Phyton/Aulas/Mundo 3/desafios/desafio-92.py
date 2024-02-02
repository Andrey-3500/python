from datetime import date
pessoa = {}

pessoa['nome'] = str(input('Nome: '))
datadenasc = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - datadenasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não possui) :'))

if pessoa['ctps'] == 0:

    print('-'*30)
    for k, v in pessoa.items():
        print(k,'tem o valor', v)

else:

    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (date.today().year - pessoa['contratação']))
    print('-'*30)

    for k, v in pessoa.items():
        print(k, 'tem o valor', v)
