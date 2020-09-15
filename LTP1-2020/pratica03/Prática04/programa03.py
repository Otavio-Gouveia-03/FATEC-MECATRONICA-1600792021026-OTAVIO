#Pede para o usuário digitar uma senha e validar ela com a senha secreta
#Cria uma variável para guardar a senha
senha_secreta = '221016'

#Pede para o usuário digitar sua senha
senha = input ('Digite a senha')

#Verificar se a senha do usuário esta correta
if senha == senha_secreta:
  print('Acesso Consedido')
  print('Seja Bem vindo')
else:
  print('Acesso negado')
