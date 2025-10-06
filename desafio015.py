#Desafio : Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
#Objetivo : Calcular o preço total do aluguel de um carro com base na quantidade de dias alugados e na distância percorrida em quilômetros.
#Aprendizado: Uso de variáveis, entrada de dados, operações matemáticas e formatação de strings em Python.

dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foram percorridos? '))
preco = (dia * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(preco))