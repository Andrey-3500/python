salario = float(input('Qual o salario de um funcionario?'))

aumento = float(input('De quanto será o aumento do funcionario em %?'))

total = salario + (salario*aumento/100)

print('Um funcionário que ganhava R${}, com {}% de aumento, passa a ganhar R${:.2f}'.format(salario, aumento, total))