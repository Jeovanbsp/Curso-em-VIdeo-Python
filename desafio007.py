# Desafio 007 - Curso em Vídeo (Python)
# Objetivo: Calcular a média de duas notas de um aluno.
# Aprendizado: Entrada de float, média aritmética e formatação.

nota1 = float(input('Digite a Primeira Nota: '))
nota2 = float(input('Digite a Segunda Nota: '))
# Cálculo da média
media = (nota1 + nota2) / 2
print('A media entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, media))
# Fim do Desafio 007