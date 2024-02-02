

def ajuda(com):
    help(com)

while True:
    comando = input('Função ou Biblioteca (Digite fim para acabar) > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)