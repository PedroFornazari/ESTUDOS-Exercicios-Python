numero1 = 0
numero2 = 0
numero3 = 0

print('GRUPO A: EXERCICIO 6')

numero1 = float(input('Número 1: '))
numero2 = float(input('Número 2: '))
numero3 = float(input('Número 3: '))

if(numero1 > numero2 and numero1 > numero3):
  print('MAIOR NÚMERO: ', numero1)
elif(numero2 > numero1 and numero2 > numero3):
  print('MAIOR NÚMERO: ', numero2)
elif(numero3 > numero1 and numero3 > numero2):
  print('MAIOR NÚMERO: ', numero3)
else:
  print("Não existe um Número Maior ÚNICO! 2 deles são iguais, ou os 3 são iguais!")