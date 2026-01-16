# Inscrição de Cliente Exclusivo
print('INSCRIÇÃO DE CLIENTE EXCLUSIVO')

while True:
 nome = input("Digite seu nome: ")
 if nome != "Demetrios":
  print('O cliente não é esse tente novamente!!!!')
  continue
 else:
  print(f'Seja bem vindo {nome} !!')
 if nome == "Demetrios":
  print(f'{nome} Vamos Fazer sua inscrição ?')
  fazer_cadastro = input('Digite [S]im ou [N]ão:')
  if fazer_cadastro == "Sim" or fazer_cadastro == "sim":
   print('Digite Seus Dados')
  else:
   print('voce saiu do sistema!')
   break
 nome_completo = input('Digite seu nome completo:')
 cpf = input('Digite seu cpf:')
 tel = input('Digite seu tel:')
 print('Inscrição Realizada com Sucesso!!')
 break 