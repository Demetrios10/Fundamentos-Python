# Cores do arco iris 

# Lista Vazia 
cores_arco_iris = []

# Laço executa 5 vezes esse trecho do codigo
for i in range(4):
    print('Digite as cores do seu arco iris: ')
    cores = input()
    cores_arco_iris.append(cores)

# Classifica em ordem alfabetica 
cores_arco_iris.sort()

# ordena em ordem alfabetica 
print(f'As Cores do arco iris em ordem são: ')
for cores in cores_arco_iris:
    print(cores)

