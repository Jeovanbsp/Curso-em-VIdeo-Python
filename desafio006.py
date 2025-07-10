# Desafio 006 - Curso em Vídeo (Python)
# Objetivo: Ler um número e mostrar seu dobro, triplo e raiz quadrada.
# Aprendizado: operadores aritméticos, exponenciação e formatação de float.

num = int(input('Digite um número: '))
# Calculando o dobro, triplo e raiz quadrada
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** 0.5

# Exibindo os resultados formatados
print('O dobro de {} é {}.'.format(num, dobro)
print('O triplo de {} é {}.'.format(num, triplo))
print('A raiz quadrada de {} é {:.2f}.'.format(num, raiz_quadrada))