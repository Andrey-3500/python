
print('{:-^51}'.format(' CARDAPIO '))
print('\033[34mCódigo\033[m  |       \033[33mDescrição\033[m         |\033[32m Valor(R$)\033[m \n',
'-'*50,'\n',
      '\033[34m 100   \033[m|\033[33m Cachorro-Quente         \033[m| \033[32m 9,00 \033[m\n',
      '\033[34m 101   \033[m|\033[33m Cachorro-Quente Duplo   \033[m| \033[32m 11,00 \033[m\n',
      '\033[34m 102   \033[m|\033[33m X-Egg                   \033[m| \033[32m 12,00 \033[m\n',
      '\033[34m 103   \033[m|\033[33m X-Salada                \033[m| \033[32m 13,00 \033[m\n',
      '\033[34m 104   \033[m|\033[33m X-Bacon                 \033[m| \033[32m 14,00 \033[m \n',
      '\033[34m 105   \033[m|\033[33m X-Tudo                  \033[m| \033[32m 17,00 \033[m \n',
      '\033[34m 200   \033[m|\033[33m Refrigerante Lata       \033[m| \033[32m 5,00 \033[m\n',
      '\033[34m 201   \033[m|\033[33m Chá Gelado              \033[m| \033[32m 4,00 \033[m\n',
'-'*50)


opção = 0
opção2 = ''
pedido = []
valor = []
total = 0
tentativa = ''
while True:

      opção = int(input('Qual é o seu pedido ?\n >> '))
      print('\033[30m-\033[m'*50)
      if opção == 100:
                  pedido.append('Cachorro-Quente')
                  total += 9
                  valor.append(9)
      elif opção == 101:
                  pedido.append('Cachorro-Quente Duplo')
                  total += 11
                  valor.append(11)
      elif opção == 102:
                  pedido.append('X-Egg')
                  total += 12
                  valor.append(12)
      elif opção == 103:
                  pedido.append('X-Salada')
                  total += 13
                  valor.append(13)
      elif opção == 104:
                  pedido.append('X-Bacon')
                  total += 14
                  valor.append(14)
      elif opção == 105:
                  pedido.append('X-Tudo')
                  total += 17
                  valor.append(17)
      elif opção == 200:
                  pedido.append('Refrigerante Lata')
                  total += 5
                  valor.append(5)
      elif opção == 201:
                  pedido.append('Chá Gelado')
                  total += 4
                  valor.append(4)
      else:
            print('\033[31m Opção Invalida! \033[m')
            tantativa = str(input('Gostaria de tentar novamente ? \n [S/N] >> ')).upper()

            if tantativa == 'N':
                  break

      opção2 = str(input('Quer pedir algo mais ? \n [S/N] >> ')).upper()
      print('\033[30m-\033[m' * 50)
      if opção2 == 'N':
        break


quantidade = int(len(pedido))


print('Seu pedido foi :')
for c in range(0, quantidade):

    print(f'{c + 1}ª{pedido[c]}R${valor[c]}')

print('\033[30m-\033[m' * 50)
print('O total do seu pedido foi de R${}'.format(sum(valor)))