# Desafio 005 - Curso em Vídeo (Python)
# Objetivo: Ler um número inteiro e mostrar seu antecessor e seu sucessor.
# Aprendizado: uso de operadores aritméticos simples e manipulação de inteiros.

n = int(input('Digite um número inteiro:'))
# Cálculo do antecessor e sucessor
antecessor = n - 1
sucessor = n + 1 
# Exibição do resultado
print('Analisando o número {},seu antecessor é {} e seu sucessor é {}.'.format(n, antecessor, sucessor))