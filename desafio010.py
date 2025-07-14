# Desafio 010 - Curso em Vídeo (Python)
# Objetivo: Converter valor em reais para dólares, com base em uma taxa fixa.
# Aprendizado: entrada float, operações matemáticas simples, formatação.

real = float(input('Digite o valor em reais para converter em Dolar (R$):'))
dolar = 5.00

convertido = real / dolar
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(real, convertido))