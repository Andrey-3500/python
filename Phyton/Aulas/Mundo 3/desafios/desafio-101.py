import datetime
from datetime import date
def voto(anos):

    if anos < 14:
       return ('NÃO VOTA')

    elif 65 > anos >= 18:
        return ('VOTO OBRIGATORIO')

    else:
        return ('VOTO OPCIONAL')


print('-'*30)
anonasc = int(input('Em que ano nasceu? \n >> '))
idade = date.today().year - anonasc

print(f'Com {idade} anos: {voto(idade)}.')

# 65 opcional