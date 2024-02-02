from time import sleep
valor1 = float(input('Digite um primeiro valor \n >> '))
valor2 = float(input('Digite um segundo valor \n >> '))
opção = 0

while opção != 5:
    print('------ MENU ------')
    print('[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Trocar os números\n[5]Sair do programa')
    print('------------------')

    opção = int(input('Digite sua opção \n >> '))
    print('------------------')

    if opção == 1:
        print('{} + {} = {:.1f} '.format(valor1, valor2, valor1 + valor2))
        print('-' * 20)
    elif opção == 2:
        print('{} x {} = {:.1f} '.format(valor1, valor2, valor1 * valor2))
        print('-'*20)
    elif opção == 3:
        if valor1 > valor2:
            print('o maior valor é {}'.format(valor1))
            print('-' * 20)
        elif valor1 < valor2:
            print('o maior valor é {}'.format(valor2))
            print('-' * 20)
        else:
            print('Nenhum valor é maior, os dois são iguais')
            print('-' * 20)
    elif opção == 4:
        valor1 = float(input('Digite um primeiro valor \n >> '))
        valor2 = float(input('Digite um segundo valor \n >> '))

    elif opção == 5:
        break
    else:
        print('Opção inválida, Tente novamente !')
    sleep(2)
print('Fim do programa!')