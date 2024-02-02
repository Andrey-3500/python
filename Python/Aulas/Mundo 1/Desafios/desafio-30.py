n = float(input('\033[0;35m Digite um numero qualquer:\033[m '))

r = n % 2
print(r)
if r == 0:
    print('{:.0f} é um numero\033[0;34m PAR\033[m'.format(n))
else:
    print('{:.0f} numero é \033[0;34mIMPAR\033[m'.format(n))