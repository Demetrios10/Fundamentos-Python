# Verificação de convidados

while True:
  numero = input('Digite um numero: ')
  nome = input('Digite seu nome: ')
 
  nomes = ['demetrios','jose','amanda','antonio','marcia','quiteria','fabio','domingos','david','josiel']
  lista = ['22','0','35','45','78','99','100','23','43','75']
 
  if numero and nome in nomes and lista:
   print('Numero e nome estão na lista de convidados :)')
  else:
   print('Numero e nome não estão na lista de convidados :(')
    
  sair = input('Quer sair do sistema? [s]im: ').lower().startswith('s')
  if sair is True:
   print('vc saiu!!')
   break
