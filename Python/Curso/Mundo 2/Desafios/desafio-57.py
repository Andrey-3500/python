sexo = str(input('Informe seu sexo [M/F] \n >> ')).upper().strip()[0]

while sexo not in 'MmFf':

    sexo = str(input('Opção INVALIDA! \nTente novamente, Informe seu sexo [M/F] \n >> ')).upper().strip()[0]
print('Registrado com sucesso!')
