# Programa que leia valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Uma distância em metros: '))


print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm: ' .format(m, m*100, m*1000))
print('A medida de {}m corresponde a {:.0f}km: ' .format(m, m*1/1000))

# cm = m * 100
# mm = m * 1000
# km = m * 1/1000





