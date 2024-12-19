lar = float(input('Qual a largura da parede em metros : '))
alt = float(input('Qual a altura da parede em metros : '))
area = lar * alt
litros = area / 2
print('A parede com {}m de altura e {}m de largura tem area de {:.2f} m²'.format(lar, alt, area))
print('Voce precisa de {:.2f} litros de tinta'.format(litros))
