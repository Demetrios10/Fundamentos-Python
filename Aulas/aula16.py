# Operadores Lógicos 
# and (e) - todas as consições precisam ser verdadeiras 


entrada = input('[E]ntrar [S]air: ')
senha = input('Digite a senha: ')
senha_permitida = '12345'

if entrada == 'E' and senha == senha_permitida:
    print('Entrou')
else:
    print('Saiu')
    
    

