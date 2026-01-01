# Cores do arco iris 

cores_arco_iris = []

for i in range(4):
    print('Digite as cores do seu arco iris: ')
    cores = input()
    cores_arco_iris.append(cores)

cores_arco_iris.sort()

print(f'As Cores do arco iris em ordem são: ')
for cores in cores_arco_iris:
    print(cores)

