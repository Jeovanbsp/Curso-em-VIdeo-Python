#Desafio : Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Objetio : Transformar um número real em inteiro forçando a retirada da parte decimal.
#Aprendizado : Utilização da função int() para converter um número real em inteiro.

num = float(input('Digite um número real: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

#Outra forma de fazer isso é utilizando a biblioteca math e a função floor() que arredonda o número para baixo.

#import math
#num = float(input('Digite um número real: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.floor(num)))
