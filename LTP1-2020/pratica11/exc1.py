#Construa um programa que permita que o usuário informe os 3
#lados de um triângulo, A, B e C. Apresente para ele o valor
#da área do triângulo utilizando a fórmula de Hierão
def semiper(A, B, C):
  return (A + B + C)/2
def area(A, B, C):
  s = semiper(A, B, C)
  return (s*(s-B)*(s-B)*(s-C))**1/2

A = int(input('lado 1:'))
B = int(input('lado 2:'))
C = int(input('lado 3:'))
area_triangulo = area(A, B, C)

print(area triangulo)
