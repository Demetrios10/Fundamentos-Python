# Lista de alunos em ordem alfabetica 

# Lista Vazia 
alunos = []

# Laço executa 5 vezes esse trecho do codigo
for i in range(5):
    print('\nDigite os Nomes dos Alunos: ')
    aluno = input()
    alunos.append(aluno)

# Classifica em ordem alfabetica 
alunos.sort()

# Ordena em ordem alfabetica 
print(f'\nA Lista dos alunos do 3 ano em ordem alfabetica é: ')
for aluno in alunos:
    print(aluno)