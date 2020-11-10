Construa um programa que permita que o usuário informe os 3
lados de um triângulo, A, B e C. Apresente para ele o valor
da área do triângulo utilizando a fórmula de Hierão

A = int(input('lado 1:'))
B = int(input('lado 2:'))
C = int(input('lado 3:'))
s = (A + B + C)/2
area = (s*(s-B)*(s-B)*(s-C))**1/2

if A > 0 and B > 0 and C > 0:
  print("Resultado:" , area)
else:
  print("Você é burro")
