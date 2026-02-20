"""
Iteravel -> str , range ,etc
Iteravel -> quem sabe entregar um valor por vez 
next -> me entregue o proximo valor
iter -> me entregue seu iterador 
"""

nome = 'Demetrios' # Iteravel 

# iterador = iter(nome) # Iterador 

# while True:
#     try:
#       letra = next(iterador)
#       print(letra)
#     except StopIteration:
#         break

for letra in nome:
    print(letra)
    

