# Verificação de dados pessoais

nome = ""
idade = 0

nome = input("Digite seu Nome: ")
idade = int(input("Digite a sua Idade: "))

if(nome == "Demetrios" and idade >= 18):
    print( nome + " Seja Bem Vindo Pode Entrar!!")
else:
    print("Nome Ou Idade Incorretas!!")
    print("Voce não é o Dono Por favor se Identifique!!")
