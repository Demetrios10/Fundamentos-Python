# Set 

planeta_anao = {'Plutão','Ceres','Eris','Haumea','Makemake'}
print(planeta_anao)
# print(len(planeta_anao)) # Quantos numeros tem em um set 
# print('Ceres' in planeta_anao) # Seres esta no set planeta_anao

# for astro in planeta_anao:
#     print(astro.upper()) # imprime tudo em maiusculo 

# astros = ['Lua','Vênus','Sirius','Marte','Lua']
# # print(astros,end='')
# # astros_set = set(astros)
# # print(astros_set)

astros_1 = {'Lua','Vênus','Sirius'}
astros_2 = {'Marte','Cometa de Halley'}

print(astros_1 == astros_2)
print(astros_1 | astros_2) # une os dois conjuntos sem os valores repetidos 
print(astros_1.union(astros_2)) # une os dois conjuntos sem os valores repetidos

print(astros_1 & astros_2)
# print(astros_1.intersection(astros_2))