# Programa Analisando Triângulo v1.0 - ler 3 segmentos e ver se podem ou não formar triângulo

print('=' * 30)
print('Analisador de triângulos')

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')
print('=' * 30)
