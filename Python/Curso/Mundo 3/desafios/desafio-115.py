from uteis.numeros import *
from uteis.utilidades.ex115 import *

while True:
    res = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    print(linha())    
    if res == 1:
        print(f'{"Opção 1":^40}')

    elif res == 2:

        print(f'{"Opção 2":^40}')

    elif res == 3:

        print(f'{"Opção 3":^40}')
        print('Saindo do sistema... Até logo!')
        break

    else:
        print('Erro! Digite uma opção válida!')