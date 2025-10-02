# Desafio 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# Objetivo : Calcular o novo salário com o aumento de 15%  
# Aprendizado : Utilização de variáveis, operações matemáticas e formatação de strings.

salario = float(input('Digite o salário do funcionário: R$ '))
aumento = salario * 0.15
novo_salario = salario + aumento
print('Um funcionario que ganhava R$ {:.2f}, com 15% de aumento, passa a ganhar R$ {:.2f}'.format(salario, novo_salario))