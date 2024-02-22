def leiaDinheiro(msg):
    while True:
        v = input(msg).replace(',','.').strip()
        if v.isalpha() or v == '':
            print(f'Erro: {v} é um preço inválido!')
        else:
            break
    return float(v)
