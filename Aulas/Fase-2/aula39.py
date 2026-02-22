"""
Listas em Python 
Tipo list - Mutável 
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizaveis - índices e fatiamento 
Métodos úteis:  append , insert , pop , del , clear , extend , + 
Create , ler , alterar , apagar = lista [i] (CRUD)
"""


lista = [10,20,30,40,50] # criar 
lista[2] = 1000 # alterar 
del lista[1] # apaga indice 2

 # append adiciona ao final da lista 
lista.append(2000)
lista.append(900)
lista.append(500)
lista.append(700)

lista.pop() # remove o ultimo item da lista 

print(lista) # printa toda a lista 
print(lista[1]) # printa indice 1 da lista 
print(lista[0]) # printa indice 0 da lista 

