# Sintaxe:
# print(objetos,argumentos)

mensagem = 'Função Print()'
print(mensagem)
print('Aula de Python')


nome = "Demetrios Alves"
print("Esse é o meu nome - " + nome)

sobrenome = 'Alves Da Silva'
print('Meu nome é:  Demetrios', sobrenome)

nome = input("Digite seu Nome: ")
print("Eu - " , nome , "Estou aprendendo Python!!")

print('Imprime a Mensagem e mude de linha')
print('Imprime a mensagem e permaneça na mesma linha', end='')
print(' Continuo na Mesma Linha!')

nome = 'Marcia'
idade = 30
msg_formatada = 'O Nome dela é {0} e ela tem {1} anos'.format(nome,idade)
print(msg_formatada)


nome = 'Demetrios'
peso = 105
msg = f'Olá Meu nome é {nome} e eu peso {peso}'
print(msg)


a = 10
b = 20 
soma = f'A soma de {a} com {b} é igual a {a + b}'
print(soma)


valor = 125.579637
print(f'O valor é {valor:.2f}')

valor = 125.579637
print(f'O valor é \'{valor:.2f}\'')