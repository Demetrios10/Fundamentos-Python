#precedencia de operadores

# exemplos de precedencia de operadores
# a ordem de precedencia dos operadores é a seguinte:
# 1. parênteses ()
# 2. exponenciação (**)
# 3. multiplicação (*) e divisão (/)
# 4. adição (+) e subtração (-)


print(10 + 20 * 30) # o resultado é 610 , pois a multiplicação tem precedencia sobre a adição
print((10 + 20) * 30) # o resultado é 900 , pois a adição tem precedencia sobre a multiplicação
print(10 + 20 * 30 - 40) # o resultado é 570 , pois a multiplicação tem precedencia sobre a adição e a subtração
print(10 + 20 * 30 - 40 / 2) # o resultado é 590 , pois a multiplicação tem precedencia sobre a adição e a subtração , e a divisão tem precedencia sobre a adição e a subtração
print(10 + 20 * 30 - 40 / 2 ** 2) # o resultado é 595 , pois a multiplicação tem precedencia sobre a adição e a subtração , e a divisão tem precedencia sobre a adição e a subtração , e a exponenciação tem precedencia sobre a multiplicação e a divisão


conta = 10 + 30 * 10 - 30 / 10 ** 2
print(conta)
# o resultado é 309.7
# pois a multiplicação tem precedencia sobre a adição e a subtração
# , e a divisão tem precedencia sobre a adição e a subtração ,
# e a exponenciação tem precedencia sobre a multiplicação e a divisão


# o resultado é 59 , pois a multiplicação tem precedencia
# sobre a adição e a subtração , e a exponenciação tem precedencia
# sobre a multiplicação e a divisão , e a divisão inteira tem precedencia
# sobre a adição e a subtração
conta_rapida = 20 + 40 * 1 - 8 ** 1 // 3
print("O resultado é de: " + str(conta_rapida))

