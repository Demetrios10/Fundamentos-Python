# Login Com Usuario e Senha
usuario = None
senha = None


while True:
    print("Digite Usuario: ")
    usuario = input()
    print("Digite Senha: ")
    senha = input()

    if((usuario == 'Demetrios' and senha == '95120')):
        break
    print("Usuario ou Senha estão Incorretos!!")
print(f'Voce esta Logado: {usuario}')