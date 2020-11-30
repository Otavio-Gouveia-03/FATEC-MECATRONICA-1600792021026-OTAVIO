def mostrarUsuario(nome, email, senha):
    print("Usuario:")
    print("Nome:", nome)
    print("EMAIL:", email)
    print("Senha:", senha)
    
def lerNovoUsuario():
    nome = input("Nome:")
    email = input("Email:")
    senha = input("Senha:")
    return nome, email, senha
    
n,c,i = lerNovoUsuario()
mostrarUsuario(n,c,i)

#Menu
def agência_menu():
  print("Ação:")
  print("1 - Transfêrencia")
  print("2 - Saldo")
  print("3 - Sair")

def Transferência(usuário1,valor1,usuário2):
  return usuário1 - valor1
  return usuário2 + valor1
def Saldo (usuário1):
  print(valor_usuário)
def Sair():
  print("Volte Sempre!")

Valor_usuário1 = 3000

#Programa Principal

import os
continuar = True 
while continuar == True:
  agência_menu()
  opcao = int(input("Opção:"))
  if opcao == 1:
    usuário1 = (input("Identifique sua conta:"))
    valor1 = float(input("Valor a ser transferido:"))
    usuário2 = (input("Conta de recebimento:"))
    print("Operação efetuada com sucesso!")
    print(Transferência)
    continuar = print("Deseja realizar outra operação?")
  elif opcao == 2:
    valor_usuário = input("Indique sua conta:")

#Não conseguimos corrigir os erros e dar continuidade!!!
