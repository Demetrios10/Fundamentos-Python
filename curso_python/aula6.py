# coerção de tipos


# o resultado é um float , pois o python converte o numero inteiro para um numero float
print(10 + 10.0)
print(-10 + 20.9)

print(30 + 30)
print("D" + str(10)) # isso gera um erro , pois não é possível concatenar uma string com um numero inteiro
print("D" + str("10")) # isso é possível , pois são duas strings

print(int("1") , type("1"))
print(float(1.7) , type(1.7))
print(type(float("1.7")+ 1))
print(bool("deltas") , type("deltas"))