#Desafio: Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit.
#Objetivo: 
#Aprendizado: 

c = float(input('Informe a temperatura em ºC: '))
f = ((9*c)/5) + 32
print('A Temperatura de {}ºC corresponde a {}ºF!'.format(c, f))