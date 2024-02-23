n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1 + n2) / 2

print('Tirando {:.1f} e {:.1f}, a Média do aluno é {:.1f}'.format(n1, n2, media))

if media < 5:
   print('\033[0;31mREPROVADO!')

elif 5 <= media < 6.9:
    print('ficou em \033[0;33mRECUPERAÇÃO!')

else:
    print('ficou ná média, Parabéns! foi \033[0;32mAPROVADO!')