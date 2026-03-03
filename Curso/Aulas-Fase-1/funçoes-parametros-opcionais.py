
# def contar(num=11,caractere='+'):
#     for i in range(1,num):
#         print(caractere)

# if __name__ == '__main__':
#     contar(8,'@')



x = 5
y = 6
z = 3

def soma_mult(x,y,z = 0):
    if z == 0:
        return x * y
    else:
        return x + y + z
    
if __name__ == '__main__':
    res = soma_mult(x , y, z)
    print(res)