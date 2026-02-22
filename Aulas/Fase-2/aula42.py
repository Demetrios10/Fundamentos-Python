# cuidados com tipo de dados mutaveis 
# = - copiado o valor (imutaveis)
# = - aponta para o mesmo valor na memoria (mutavel)


lista = ['demetrios','maria']
nomes_completos = lista.copy() # retorna uma nova lista para a segunda lista 

lista[0] = 'Qualquer coisa'

print(lista)
print(nomes_completos)