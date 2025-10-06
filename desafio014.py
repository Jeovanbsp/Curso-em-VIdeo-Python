#Desafio: Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit.
#Objetivo: Converter Celsius para Fahrenheit
#Aprendizado: Utilização de variáveis, entrada de dados, operações matemáticas e formatação de strings.

c = float(input('Informe a temperatura em ºC: '))
f = ((9*c)/5) + 32
print('A Temperatura de {}ºC corresponde a {}ºF!'.format(c, f))