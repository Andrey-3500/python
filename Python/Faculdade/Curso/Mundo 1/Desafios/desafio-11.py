larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg*alt
tin = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.1f}m². \n'
      'Para pintar essa parede, você precisará de {:.1f}l de tinta.'.format(larg, alt, area, tin))