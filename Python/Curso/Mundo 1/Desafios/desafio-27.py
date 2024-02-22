n = input('Digite seu nome completo:').title().strip()

nome = n.split()

print('prazer em te conhecer!')

print('Seu primeiro nome é {}'.format(nome[0]))

print('Seu Último nome é {}'.format(nome[len(nome)-1]))
