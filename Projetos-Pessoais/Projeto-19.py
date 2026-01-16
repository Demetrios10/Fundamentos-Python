# Cadastro de Clientes com Cartões Existentes

print('CADASTRO DE CLIENTES COM CARTÕES EXISTENTES')

numero_cartao = input("Digite o numero do seu cartão: ")
match numero_cartao:
    case '0451'| '0562'|'9074'|'9354':
        print("seu cartão esta na lista")
        if numero_cartao == '0451'or numero_cartao =='0562'or numero_cartao =='9074'or numero_cartao =='9354':
            print(f'Seja bem vindo {numero_cartao} !!')
            print('vamos fazer o seu cadastro ?')
            fazer_cadastro = input('Digite [S]im ou [N]ão:')
            if fazer_cadastro == "Sim" or fazer_cadastro == "sim":
               print('Digite Seus Dados')
               nome_completo = input('Digite seu nome completo:')
               cpf = input('Digite seu cpf:')
               tel = input('Digite seu tel:')
               print('Inscrição Realizada com Sucesso!!')
            else:
             print('voce saiu do sistema!')
    case _:
     print("Esse numero de cartão não se encontra na lista!!")

