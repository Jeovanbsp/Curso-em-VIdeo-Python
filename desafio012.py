#Desafio 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#Objetivo : Ler o preço de um produto e calcular o preço com desconto.
#Aprendizado : Uso de variáveis, entrada de dados, operações matemáticas e formatação de strings.

preco = float(input('Digite o preço do produto: R$ '))
desconto = preco * 0.05
preco_final = preco - desconto
print('O Produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(preco, preco_final))