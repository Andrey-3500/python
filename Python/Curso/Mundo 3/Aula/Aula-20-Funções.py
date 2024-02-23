# FUNÇÕES -> coisas constantes nos
# programas pode ser criadas funções


# função sem parâmetro

def lin():
    print('-' * 30)
# pular 2 linhas após o def


lin()
print('     CURSO EM VIDEO      ')
lin()
lin()
print('     APRENDA PHYTON      ')
lin()
lin()
print('     GUSTAVO GUANABARA      ')
lin()
print()
print()
# função com parâmetro
def msg(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


msg('CURSO EM VIDEO')
msg('APRENDA PHYTON')
msg('GUSTAVO GUANABARA')
print()
print()
# fução de soma
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)
soma(b=7, a=8)
print()
print()
# desempacotar

def contador(* num):
    print(num)


contador(2, 6, 7)
contador(2, 8, 5, 3, 2, 1)
contador(3, 1)




