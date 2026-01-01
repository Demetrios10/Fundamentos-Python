# Lista de alunos em ordem alfabetica 

alunos = []

for i in range(5):
    print('\nDigite os Nomes dos Alunos: ')
    aluno = input()
    alunos.append(aluno)

alunos.sort()

print(f'\nA Lista dos alunos do 3 ano em ordem alfabetica é: ')
for aluno in alunos:
    print(aluno)