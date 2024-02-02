pessoa = {}
pessoas = []
soma = media = 0
while True:
    print('-'*30)
    pessoa['nome'] = str(input('Nome: '))

    while True:

        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().split()[0]

        if pessoa['sexo'] in 'MF':
            break

        else:
            print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())

    resp = ''
    while True:

        resp = str(input('Quer continuar ? [S/N] \n >> ')).upper().split()[0]

        if resp in 'SN':
            break

        else:
            print('ERRO! Responda apenas S ou N')

    if resp == 'N':
        break

print('-'*30)
print(f'O grupo tem {len(pessoas)} pessoas')

media = soma / len(pessoas)
print(f'a média de idade das pessoas é {media:5.2f}')

print(f'As mulheres cadastradas foram:', end=' ')

for p in (pessoas):

    if p['sexo'] == 'F':
        print(p['nome'], end=' ')

print()
print('-' * 30)
print('Lista de pessoas que estão acima da média:')
for p in (pessoas):

    if p['idade'] > media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<< ENCERRADO >>')
