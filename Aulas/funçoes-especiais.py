# Funções lambda (anônimas)
# Sintaxe:
# lambda argumentos: expressão

# # Exemplo 1
# quadrado = lambda x: x ** 2
# for i in range(1,11):
#      print(quadrado(i))
    

# # função que verifica se o numero é par
# par = lambda x: x % 2 == 0
# print(par(9))
 
 
# f_c = lambda f: (f - 23) * 5/9
# print(f_c(100))



# # Função map()
# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x * 2,num))
# print(dobro)

# # convertendo para letras maiusculas 
# palavras = ['Python','Java','C#','JavaScript']
# maiusculas = list(map(str.upper,palavras))
# print(maiusculas)


# # Função Filter()
# # Sintaxe:
# # filter(função,sequencia)
# def numeros_pares(n):
#     return n % 2 == 0
# numeros = [1,2,3,4,5,6,7,8,9,0]
# num_par = list(filter(numeros_pares, numeros))
# print(num_par)

# # extraindo somente numeros impares com função Lambda 
# numeros_variados = [10,20,30,40,50,60,70]
# num_impar = list(filter(lambda x: x % 2 != 0,numeros))
# print(num_impar)


# # Função reduce()
# # Sintaxe 
# # reduce (função, sequencia,valor_inicial)
from functools import reduce

# def mult(x,y):
#     return x * y
# numeross = [1,2,3,4,5,6,7]
# total = reduce(mult,numeross)
# print(total)


# soma cumulativa dos quadrados dos valores , usando expressão lambda
n = [1,2,3,4]
totais = reduce(lambda x,y: x**2 + y**2,n)
print(totais)