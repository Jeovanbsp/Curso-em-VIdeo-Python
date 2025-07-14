# Desafio 008 - Curso em Video (Python)
# Objetivo: Converter metros para centímetros e milímetros
# Aprendizado : Conversão de Unidade com multiplicação simples

metros = float(input('Digite a medida em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print('A medida de {} metros corresponde a {:.0f} centímetros e {:.0f} milímetros.'.format(metros, centimetros, milimetros))