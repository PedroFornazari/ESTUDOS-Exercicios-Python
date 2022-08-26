nota1 = 0
nota2 = 0
soma = 0
notaFinal = 0

print('EXERCICIO 6')
print('Calcule sua Nota Final aqui: ')

nota1 = float(input('NOTA 1: '))
nota2 = float(input('NOTA 2: '))

soma = nota1 + nota2
notaFinal = soma / 2

print('SUA NOTA FINAL: ', notaFinal)

if(notaFinal >= 7.0):
  print('Você está APROVADO!')
elif(notaFinal >= 3.0 and notaFinal <= 7.0):
  print('Você está de EXAME!')
else:
  print('Você está REPROVADO!')