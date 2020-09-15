#Operadores da divisão (/) e o resto da divisão (%)
#divisão = 144 / 2
#resto = 144 % 2

#print('Divisão:', divisão)
#print('Resto:', resto)

# Ler um número para ver se ele é par ou impar
numero = int(input('Informe um numero'))
#Calcular o resto da divisao do numero por 2
resto = numero % 2
#Olha para o valor do resto
if resto == 0:
  print(numero, 'é par!')
else:
 print(numero, 'é impar!')
