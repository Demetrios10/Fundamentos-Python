"""
Cuidados com dados mutáveis
copiado o valor (imultaveis)
aponta para o mesmo valor na memória (mutavel)
"""

lista = ['luiz','maria']
listas = lista

lista [0] = 'Qualquer coisa'

print(listas)