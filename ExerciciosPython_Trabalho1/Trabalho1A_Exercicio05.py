nota1 = 0
nota2 = 0
soma = 0
notaFinal = 0

print('GRUPO A: EXERCICIO 5')
print('Calcule sua Nota Final aqui: ')

nota1 = float(input('NOTA 1: '))
nota2 = float(input('NOTA 2: '))

soma = nota1 + nota2
notaFinal = soma / 2

print('SUA NOTA FINAL: ', notaFinal)

if(notaFinal >= 10.0):
  print('APROVADO COM DISTINÇÃO!')
elif(notaFinal >= 7.0):
  print('APROVADO')
else:
  print('REPROVADO!')