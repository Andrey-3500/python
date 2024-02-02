nome = str(input('Digite seu nome completo: '))

min = nome.lower()

print('seu nome com todas as letras minusculas fica {}'.format(min))

mai = nome.upper()

print('seu nome com todas as letras letras maiusculas fica {}'.format(mai))

nome = nome.split()

total =''.join(nome)

print('seu nome tem {} letras'.format(len(total)))

pri = len(nome[1])

print('seu primeiro nome tem {} letras'.format(pri))
