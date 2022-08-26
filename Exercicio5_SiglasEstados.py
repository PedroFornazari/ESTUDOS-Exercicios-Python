estado = 'AB'

print('EXERCICIO 5')

estado = str(input('Qual a sigla do estado que você nasceu? '))

if(estado == 'SP'):
  print('Então você é Paulista')
elif(estado == 'RJ'):
  print('Então você é Carioca')
elif(estado == 'MG'):
  print('Então você é Mineiro')
elif(estado == 'RS'):
  print('Então você é Gaúcho')
else:
    print('Então você é dos Outros Estados')