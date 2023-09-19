# Programa para ler a altura e largura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária,
# sendo que 1 litro de tinta pinta 2m² de parede

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))

area = l * a
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e tem área de {}m².'.format(l, a, area))
print('Para pintar essa parade você precisa de {}l de tinta'.format(tinta))

