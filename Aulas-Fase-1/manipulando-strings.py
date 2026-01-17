# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)


# produtos = 'ferro e zinco'
# print('zinco' in produtos) # a palavra zinco esta em produtos 
# print('demetrios' not in produtos) # a palavra demetrios não esta em produtos 

# item = 'paralelepipedo'
# pos = item.find('lele') # encontre a sequencia lele dentro de item 
# print(pos) 

# pos = item.find('pati') # essa sequencia se encontra dentro de item 
# print(pos)

# nome = "demetrios alves da silva"
# print(nome.lower()) # Imprime tudo em minusculo 
# print(nome.upper()) # Imprime tudo em Maiusculo 
# print(nome.capitalize()) # somente a primeira letra da frase fica em maiusculo 
# print(nome.title()) # coloca cada letra de cada palavra em maiusculo 


# nome = 'Demetrios Alves Da Silva'
# novo_nome = nome.replace('Alves','Gomes') # substitui a palavra Alves por Gomes
# print(novo_nome)

# frase = '     ola mundo!  '
# print(frase)
# print(frase.lstrip()) # elimina espaços a esquerda
# print(frase.rstrip()) # elimina espaços a direita 
# print(frase.strip()) # elimina espaços dos dois lados

fruta = 'Laranja'
print(fruta)
print(fruta.rjust(10)) # use 10 espaços para escrever a palavra e alinhe a direita a palavra 
print(fruta.ljust(10)) # use 10 espaços para escrever a palavra e alinhe a esquerda a palavra 
print(fruta.center(10)) # alinhe a palavra ao meio 
print(fruta.center(20,"*")) # alinhe ao centro a palavra e preencha os espaços com esse * caracter 

texto = """
Doc String é uma especie de documentação que podemos inserir dentro de um modulo 
, função ou classe no python , entre outros locais.
  Respeita o deslocamento do texto e é multilinhas 
"""
print(texto)