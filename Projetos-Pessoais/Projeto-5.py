# Programa Para Digitar Nome Selecionar Botão x para sair 
nome = ""

while True:
    print("Digite seu nome: ")
    nome = input()

    if(nome == 'sair' or nome =='SAIR'):
        break
    print(f'Seja Bem_Vindo,{nome}')
print("Até Logo!!")