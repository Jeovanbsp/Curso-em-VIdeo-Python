# Desafio 004 - Curso em Vídeo (Python)
# Objetivo: Ler algo pelo teclado e mostrar o tipo primitivo e várias informações sobre ele.
# Aprendizado: uso de type(), isnumeric(), isalpha(), isalnum(), isupper(), islower(), etc.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())