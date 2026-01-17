# Lista: representa uma sequência de valores
# Sintaxe: nome_lista = [valores]


# Uma Lista Comum 
notas = [10,20,33,45,67]
print(notas[1])

# Duas Listas Concatenadas 
notas1 = [12,45,76,89]
notas2 = [33,46,79,20]

resultado = notas1 + notas2
print(resultado)

# Pegando um Valor aleatorio na lista 
nomes = ['Demetrios','Bianca','Renato','Fernando']
print(nomes[3])

# Valores Sequenciais a partir da posição 0 imprime dois valores
print(nomes[0:2])

# Quantos elementos eu tenho em uma lista nomes
print(len(nomes))

# Retorna uma versão ordenada da lista sem modificar a lista 
print(sorted(nomes))

# Reverter os valores de uma lista 
notas = [10,20,33,45,67]
print(sorted(notas,reverse=True))

# Sum que soma todos os valores da minha Lista 
numeros = [100,1000,3000,4500]
print(sum(numeros))

# Min Valor Minimo 
num = [10,1,34,0]
print(min(num))

# Max Valor Maximo 
numeros_maximos = [1300,2300,4300,5700]
print(max(numeros_maximos))

# inserir novo elemento ao final da lista 
numeros_maximos.append(22)
print(numeros_maximos)

# Retirar o Ultimo elemento de uma lista 
numeros_maximos.pop()
print(numeros_maximos)

# Retirar um elemento qualquer especificando a posição do mesmo
numeros_maximos.pop(2)
print(numeros_maximos)

# Insere um item a uma lista 
numeros_maximos.insert(2,11)
print(numeros_maximos)

# Verificar se existe um valor dentro da lista 
print(11 in numeros_maximos)

# Usando for junto com lista 
planetas = ['Mercúrio','Vênus','Marte','Saturno','Urano','Netuno']
for planeta in planetas:
    print(planeta)