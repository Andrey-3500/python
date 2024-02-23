print('-'*30)
print('BANCO DO CEV')
print('-'*30)

valor = int(input('Que valor vocÊ quer sacar? R$'))
ced50 = int(valor/50)
resto = valor % 50
print(f'Total de {ced50} cédulas de R$50')
ced20 = int(resto/20)
resto = resto % 20
print(f'Total de {ced20} cédulas de R$20')
ced10 = int(resto/10)
resto = resto % 10
print(f'Total de {ced10} cédulas de R$10')
ced1 = int(resto/1)
print(f'Total de {ced1} cédulas de R$1')
print('-'*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')